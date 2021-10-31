from math import trunc
import random
from flask import Flask, render_template, session, redirect, request

from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    if 'num_tries' in session:                                                     # If  num_visits key exists
        session['num_tries'] += 1
    else:                                                                           # If num_visits key doesn't exist
        session['num_tries'] = 1                                                    #   start a new game
        session['my_number'] = random.randint(1,100)                                #   get a random number from 1 to 100
        session['message'] = "start"
        session['color'] = 'none'
    print("Session key num_tries:", session['num_tries'], ":: my_number:", session['my_number'])
    return render_template("index.html")

@app.route('/game_reset')                                                           # Resets the game
def game_reset():
    del session['num_tries']
    del session['my_number']
    print("::: Game has been RESET :::")
    return redirect('/')                                                            # return to the root after game is reset

@app.route('/get_guess', methods=['POST'])
def get_guess():
    session['number_guess'] = request.form['number_guess']                          # get the input string from the form
    if session['number_guess'].isnumeric():                                         # check if the input value is a number
        session['number_guess'] = int(session['number_guess'])
        session['input_error'] = False
        if session['number_guess'] == session['my_number']:                             # Check if player guessed the number correctly
            session['message'] = f"You got it!  The number was {session['my_number']}"
            session['color'] = "mediumseagreen"
        else:
            if session['number_guess'] < session['my_number']:
                session['message'] = "Too Low!"
                session['color'] = "indianred"
            else:
                session['message'] = "Too High!"
                session['color'] = "indianred"
            if session['num_tries'] >= 5:
                session['message']="GAME OVER!"
                session['color'] = "black"
    else:
        session['number_guess'] = 50
        session['input_error'] = True
        session['message'] = "That was a Poor Guess!"
        session['color'] = 'indianred'


    # if request.form['number_guess'] != "":
    #     session['number_guess'] = int(request.form['number_guess'])
    #     session['input_error'] = 0
    # else:
    #     session['number_guess'] = 50
    #     session['input_error'] = 1
    print("Got number guess of:", session['number_guess'], "from form post :: Message:", session['message'])
    return redirect("/")

# @app.route('/increment_by', methods=['POST'])
# def increment_by():

#     return redirect("/")

# **** Ensure that if the user types in any route other than the ones specified, 
#           they receive an error message saying "Sorry! No response. Try again ****
@app.errorhandler(404) 
def invalid_route(e): 
    return "Sorry! No response. Try again."

if __name__=="__main__":   
    app.run(debug=True)    