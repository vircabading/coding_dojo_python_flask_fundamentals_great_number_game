import datetime
from flask import Flask, render_template, session, redirect, request

from werkzeug.datastructures import RequestCacheControl
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    if 'num_visits' and 'count' in session:                                                     # If  num_visits key exists
        session['num_visits'] += 1                                                  #   increment num_visits by 1
        session['count'] += 1
        print("Session key num_visits:", session['num_visits'] )
    else:                                                                           # If num_visits key doesn't exist
        session['num_visits'] = 1                                                       #   initialize num_visits to 1
        session['count'] = 1
        print("Session key num_visits:", session['num_visits'] )
    return render_template("index.html")


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