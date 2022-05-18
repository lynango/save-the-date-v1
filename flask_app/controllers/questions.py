from flask import redirect,session,request, flash
from flask_app import app
from flask_app.models.question import Question
from flask_app.models.user import User

#Process the user's request to ask a new question
@app.route('/ask/question',methods=['POST'])
def ask_question():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Question.validate_question(request.form):
        return redirect('/faqs')
    data = {
        "question": request.form["question"],
        "user_id": session["user_id"]
    }
    Question.save(data)
    return redirect('/faqs')

# #Process the user's request to delete their question.
# @app.route('/delete/question/<int:id>')
# def delete_question(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     Question.delete(data)
#     return redirect('/faqs')

# #Process the user's request to update their question 
# @app.route('/edit/question',methods=['POST'])
# def editQuestion():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Question.validate_question(request.form):
#         return redirect('/edit/question/<int:id>')
#     data = {
#         "question": request.form["question"],
#         "id": request.form['id']
#     }
#     Question.update(data)
#     return redirect('/faqs')