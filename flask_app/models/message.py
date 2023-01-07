from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash

class Message:
    db_name = "save_the_date"

    def __init__(self,db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.message = db_data['message']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creator = None

# Create a message
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO messages (name, message) 
        VALUES (%(name)s,%(message)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

# Retrieve all messages
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM messages
        ORDER BY messages.created_at DESC;
        """
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_messages = []
        for row in results:
            print(row)
            all_messages.append( cls(row) )
        return all_messages

# # Retrieve a certain message
#     @classmethod
#     def get_one(cls,data):
#         query = "SELECT * FROM messages WHERE id = %(id)s;"
#         results = connectToMySQL(cls.db_name).query_db(query,data)
#         print(results)
#         return cls( results[0] )

# # Update message
#     @classmethod
#     def update(cls, data):
#         query = "UPDATE messages SET message=%(message)s,updated_at=NOW() WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

# # Delete message
#     @classmethod
#     def delete(cls,data):
#         query = "DELETE FROM messages WHERE id = %(id)s;"
#         return connectToMySQL(cls.db_name).query_db(query,data)

# Validation checkpoint for submitted message
    @staticmethod
    def validate_message(message):
        is_valid = True
        if len(message['message']) < 3:
            is_valid = False
            flash("Message must be at least 3 characters.", "message")
        if len(message['message']) > 255:
            is_valid = False
            flash("Message must be less than 255 characters.", "message")
        return is_valid