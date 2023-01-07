from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import answer
from flask_app.models import question

class Question:
    db_name = "save_the_date"

    def __init__(self,db_data):
        self.id = db_data['id']
        self.question = db_data['question']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creator = None

# Create a question
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO questions (question) 
        VALUES (%(question)s);
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        return results

# Retrieve all questions
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM questions
        ORDER BY questions.created_at DESC;
        """
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_questions = []
        for row in results:
            print(row)
            all_questions.append( cls(row) )
        return all_questions

# # Retrieve a certain question
#     @classmethod
#     def get_one(cls,data):
#         query = "SELECT * FROM questions WHERE id = %(id)s;"
#         results = connectToMySQL(cls.db_name).query_db(query,data)
#         print(results)
#         return cls(results[0])

# # Update question
#     @classmethod
#     def update(cls, data):
#         query = """
#         UPDATE questions 
#         SET question=%(question)s,updated_at=NOW() WHERE id = %(id)s;
#         """
#         return connectToMySQL(cls.db_name).query_db(query,data)

# # Delete question
#     @classmethod
#     def delete(cls,data):
#         query = "DELETE FROM questions WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

# Validation checkpoint for submitted question
    @staticmethod
    def validate_question(question):
        is_valid = True
        if len(question['question']) < 5:
            is_valid = False
            flash("Question must be at least 5 characters", "question")
        return is_valid