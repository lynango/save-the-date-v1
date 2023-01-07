from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.message import Message
from flask_app.models.question import Question
from flask_app.models.answer import Answer

#Shows the home page
@app.route('/')
def index():
    return render_template('home.html')

#Validation checkpoint for logged in users
@app.route('/home')
def dashboard():                                                                                                                                      
    return render_template("home.html")

#Directs the user to the schedule page
@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

#Directs the user to the photos page
@app.route('/photos')
def photos():
    return render_template('photos.html')

#Directs the user to the wedding party page
@app.route('/wedding-party')
def weddingParty():
    return render_template('wedding_party.html')

#Directs the user to the lodging page
@app.route('/lodging')
def lodging():
    return render_template('lodging.html')

#Directs the user to the guest book page
@app.route('/guest-book')
def guestBook():
    return render_template(
        'guest_book.html',
        all_messages = Message.get_all()
    )

#Directs the user to the FAQS page
@app.route('/faqs')
def faqs():
    return render_template(
        'faqs.html',
        all_questions = Question.get_all(),
        all_answers = Answer.get_all(),
        )

