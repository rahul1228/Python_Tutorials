import datetime
import uuid
from src.common.database import Database
from src.models.post import Post


class Blog(object):

    # initialization function gets called as soon as object is created.
    # id=None is a var with a default value where None is id's default value
    def __init__(self, author, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
        # If id is is None then run uuid4().hex else use existing id
        # uuid() from uuid module creates unique 32 char hexadecimal id, if we dont have one already
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow()):
        # Post Object
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    created_date=date)
        post.save_to_mongo()

    def get_posts(self):
        # From Post class, called the from_blog() method/function, which returns all posts in blog_id passed in
        # self.id = blog id
        return Post.from_blog(self._id)

    # Saves Blog to mongodb in blogs collection
    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    # Creates/returns Json data for blog based off init params passed
    # returns a dictionary with the blog's data
    def json(self):
        return {
            "author": self.author,
            "title": self.title,
            "description": self.description,
            "_id": self._id
        }

   # @classmethod means that cls = this blog. so u can create a blog object with cls() instead of Blog()
   # it good to use it bc we can change the class's anme witnout having to change the code below.
    # Queries/finds all blog data from mongodb using id passed in, and find_one() fucntion/method from Database
    # returns queried blog data from mongodb in a Blog object
    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={"_id": id})
        # returns Blog Object
        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['_id'])

                #INSTEAD of having cls(author...) blog object above you can code as: cls(**blog_data)
                # Which means all data in blog_data

