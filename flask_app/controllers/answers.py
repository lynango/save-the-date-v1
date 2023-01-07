from flask import redirect,session,request
from flask_app import app
from flask_app.models.answer import Answer
from flask_app.models.question import Question

# #Process the user's request to reply to a question
# @app.route('/reply',methods=['POST'])
# def reply_back():
#     if 'user_id' not in session:
#         return redirect('/logout')
#     if not Answer.validate_answer(request.form):
#         return redirect('/faqs')
#     data = {
#         "question_id": request.form["question_id"],
#         "answer": request.form["answer"],
#         "user_id": session["user_id"]
#     }
#     Answer.save(data)
#     return redirect('/faqs')
