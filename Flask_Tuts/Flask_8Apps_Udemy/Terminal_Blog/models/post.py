import uuid
from database import Database
import datetime

class Post(object):

    # initialization function gets called as soon as object is created.
    # id=None is a var with a default value where None is id's default value
    # datetime.datetime.utcnow() = from datetime module creates a dateime object with current date
    # So date var also has a default value
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        # If id is is None then run uuid4().hex else use existing id
        # uuid() from uuid module creates unique 32 char hexadecimal id, if we dont have one already
        self.id = uuid.uuid4().hex if id is None else id

   # Saves post data to mongodb
    def save_to_mongo(self):
       Database.insert(collection='posts', data=self.json())

   # Creates/returns Json data for blog post based off init params passed
    # returns a dictionary with the posts data
    def json(self):
       return {
           'id': self.id,
           'blog_id': self.blog_id,
           'author': self.author,
           'content': self.content,
           'title': self.title,
           'created_date': self.created_date
       }

    # @classmethod means that cls = this post. so u can create a post object with cls() instead of Post()
    # it good to use it bc we can change the class's anme witnout having to change the code below.
    # Quieries a p_id and returns post info from mongodb using find_one() from Database class
    # *Finds post info using id passed in
    # returns Post() object
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        # Post Object
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    # Quieries a blog_id and finds pymongo cursor corresponding to that blog_id
    # Then for each post found corresponding to that cursor, is put in a list var called post
    # returns list called post which has all the posts found in steps above
    # *Finds all posts that are in the blog_id passed in
    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]