from flask import redirect,session,request
from flask_app import app
from flask_app.models.message import Message

#Process the user's request to leave a message
@app.route('/leave/message',methods=['POST'])
def leave_message():
    if not Message.validate_message(request.form):
        return redirect('/guest-book')
    data = {
        "name": request.form["name"],
        "message": request.form["message"]
    }
    Message.save(data)
    return redirect('/guest-book')