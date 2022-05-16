from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.message import Message
from flask_app.models.question import Question
from flask_app.models.answer import Answer
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

#Shows the front page
@app.route('/')
def index():
    return render_template('front_page.html')

#Process user's request to register
@app.route('/register',methods=['POST'])
def register():
    if not User.registration(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect('/home')

#Process user's request to login
@app.route('/login',methods=['POST'])
def login():
    data = {"email": request.form['email']} 
    user_with_email = User.get_by_email(data) 
    if user_with_email == False:
        flash("Invalid Email/Password","login") 
        return redirect('/')
    if not bcrypt.check_password_hash(user_with_email.password, request.form['password']): 
        flash("Invalid Email/Password","login") 
        return redirect('/')
    session['user_id'] = user_with_email.id
    return redirect('/home') 


#Validation checkpoint for logged in users
@app.route('/home')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')  # ->Checks to see if the user had login or not. If not, the user is redirected to the front page.
    data ={
        'id': session['user_id']    # ->If the user had login, the user is directed to the home page
    }
    one_user = User.get_one(data)                                                                                                                                              
    return render_template("home.html", current_user = one_user)

#Process user's request to logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

#Directs the user to the schedule page
@app.route('/schedule')
def schedule():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('schedule.html')

#Directs the user to the photos page
@app.route('/photos')
def photos():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('photos.html')

#Directs the user to the wedding party page
@app.route('/wedding-party')
def weddingParty():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('wedding_party.html')

#Directs the user to the lodging page
@app.route('/lodging')
def lodging():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('lodging.html')

#Directs the user to the guest book page
@app.route('/guest-book')
def guestBook():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    messages = Message.get_all_messages_with_creator()
    return render_template(
        'guest_book.html',
        all_messages = messages
    )

# Directs the user to the edit page to edit question
@app.route('/edit/question/<int:id>')
def edit_question(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template(
        "edit_question.html",
        edit=Question.get_one(data),
        user=User.get_by_id(user_data)
        )

#Directs the user to the FAQS page
@app.route('/faqs')
def faqs():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    questions = Question.get_all_questions_with_creator()
    all_answers = Answer.get_all_answers_with_creator()
    return render_template(
        'faqs.html',
        all_questions = questions,
        user=User.get_by_id(user_data),
        all_answers = all_answers,
        )

# Directs the user to the reply_question page to reply to question
@app.route('/reply/question/<int:id>')
def show_question(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    all_answers=Answer.get_one(data),
    # print("**********all answers type = ",type(all_answers))
    print("**********all answers = ",all_answers)
    for answer in all_answers:
        # print("**********answer type = ",type(answer))
        print("**********answer = ",answer)
    return render_template(
        "reply_question.html",
        question = Question.get_one(data),
        user=User.get_by_id(user_data),
        all_answers=all_answers,
        )

