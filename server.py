from flask_app import app

from flask_app.controllers import messages, questions, routes  #import the controller files here

if __name__ == "__main__":
    app.run(debug=True)


