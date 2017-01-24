import uuid
from src.common.database import Database

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        # If id is is None then run uuid4().hex else use existing id
        # uuid() from uuid module creates unique 32 char hexadecimal id, if we dont have one already
        self._id = uuid.uuid4().hex if _id is None else _id

    # Querys for user email in users collection on mongodb
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_one("users",{"email": email})
        if data is not None: # if user email is found
            return cls(**data) # ** means all info in data is returned, so email in this case

    # Querys for user ID in users collection on mongodb
    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("users", {"_id": _id})
        if data is not None:  # if user ID is found
            return cls(**data)  # ** means all info in data is returned, so  user id in this case

    # Check whether a user's email matches the password they sent us
    # If user is found, and if password is correct
    # returns only if password passsed in by user matches user account info from database/ if user.password == password aka login valid
    # else returns False
    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            # Check the password
            return user.password == password
        return False

    def register(self):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass