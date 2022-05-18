from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import message
from flask_app.models import question

class User:
    db_name = "save_the_date"

    def __init__(self, data):
        self.id = data['id']
        self.password = data['password']
        self.messages = []
        self.questions = []
        self.answers = []

# Retrieve/display a certain user
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        return cls(results[0])

# Finds the secret password
    @classmethod
    def get_by_password(cls,data):
        query = "SELECT * FROM users WHERE password = %(password)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        if len(results) < 1:
            return False
        return cls(results[0])

# Finds user by id
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls(results[0])
