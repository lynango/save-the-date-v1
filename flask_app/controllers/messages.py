from flask import redirect,session,request
from flask_app import app
from flask_app.models.message import Message
from flask_app.models.user import User

#Process the user's request to leave a message
@app.route('/leave/message',methods=['POST'])
def leave_message():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Message.validate_message(request.form):
        return redirect('/guest-book')
    data = {
        "message": request.form["message"],
        "user_id": session["user_id"]
    }
    Message.save(data)
    return redirect('/guest-book')