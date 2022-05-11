from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Answer:
    db_name = "save_the_date"

    def __init__(self,db_data):
        self.id = db_data['id']
        self.answer = db_data['answer']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creator = None

# Create an answer
    @classmethod
    def save(cls,data):
        query = "INSERT INTO answers (answer, user_id) VALUES (%(answer)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

# Retrieve all answers
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM answers;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        answers = []
        for row in results:
            answers.append( cls(row) )
        return answers

# Retrieve all answers with creator
    @classmethod
    def get_all_answers_with_creator(cls):
        query = "SELECT * FROM answers JOIN users ON answers.user_id = users.id ORDER BY answers.created_at DESC;"
        results = connectToMySQL(cls.db_name).query_db(query)
        all_answers = []
        for row in results:
            one_answer = cls(row)
            user_data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            author = user.User(user_data)
            # Associate the Answer class instance with the User class instance by filling in the empty creator attribute in the Answer class
            one_answer.creator = author
            all_answers.append(one_answer)
        return all_answers

# Retrieve a certain answer
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM answers WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results)
        return cls( results[0] )

# # Update answer
#     @classmethod
#     def update(cls, data):
#         query = "UPDATE answers SET answer=%(answer)s,updated_at=NOW() WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

# # Delete answer
#     @classmethod
#     def delete(cls,data):
#         query = "DELETE FROM answers WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

# Validation checkpoint for submitted answer
    @staticmethod
    def validate_answer(answer):
        is_valid = True
        if len(answer['answer']) < 2:
            is_valid = False
            flash("Answer must be at least 2 characters", "answer")
        return is_valid