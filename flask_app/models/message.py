from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask import flash
from flask_app.models import user

class Message:
    db_name = "save_the_date"

    def __init__(self,db_data):
        self.id = db_data['id']
        self.message = db_data['message']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.creator = None

# Create a message
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO messages (message, user_id) 
        VALUES (%(message)s,%(user_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

# Retrieve all messages
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages;"
        results =  connectToMySQL(cls.db_name).query_db(query)
        messages = []
        for row in results:
            messages.append( cls(row) )
        return messages

# Retrieve all messages with creator
    @classmethod
    def get_all_messages_with_creator(cls):
        query = """
        SELECT * FROM messages 
        JOIN users ON messages.user_id = users.id 
        ORDER BY messages.created_at DESC;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        all_messages = []
        for row in results:
            one_message = cls(row)
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
            # Associate the Message class instance with the User class instance by filling in the empty creator attribute in the Message class
            one_message.creator = author
            all_messages.append(one_message)
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