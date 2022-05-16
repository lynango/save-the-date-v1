from flask import redirect,session,request
from flask_app import app
from flask_app.models.answer import Answer
from flask_app.models.question import Question
from flask_app.models.user import User

#Process the user's request to reply to a question
@app.route('/reply',methods=['POST'])
def reply_back():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Answer.validate_answer(request.form):
        return redirect('/faqs')
    data = {
        "question_id": request.form["question_id"],
        "answer": request.form["answer"],
        "user_id": session["user_id"]
    }
    Answer.save(data)
    return redirect('/faqs')


##Process the user's request to delete their answer.
#@app.route('/delete/answer/<int:id>')
#def delete_answer(id):
#    if 'user_id' not in session:
#        return redirect('/logout')
#    data = {
#        "id":id
#    }
#    Answer.delete(data)
#    return redirect('/faqs')
#
##Process the user's request to update their answer 
#@app.route('/edit/answer',methods=['POST'])
#def edit_answer():
#    if 'user_id' not in session:
#        return redirect('/logout')
#    if not Answer.validate_answer(request.form):
#        return redirect('/edit/answer/<int:id>')
#    data = {
#        "answer": request.form["answer"],
#        "id": request.form['id']
#    }
#    Answer.update(data)
#    return redirect('/faqs')