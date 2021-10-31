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
        print("Session key num_tries:", session['num_tries'], ":: my_number:", session['my_number'])
    else:                                                                           # If num_visits key doesn't exist
        session['num_tries'] = 1                                                    #   start a new game
        session['my_number'] = random.randint(1,100)                                #   get a random number from 1 to 100
        print("Session key num_tries:", session['num_tries'], ":: my_number:", session['my_number'])
    return render_template("index.html")

@app.route('/game_reset')                                                           # Resets the game
def game_reset():
    del session['num_tries']
    del session['my_number']
    print("::: Game has been RESET :::")
    return redirect('/')                                                            # return to the root after game is reset


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