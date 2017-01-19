
class Post(object):

    def __init__(self, blog_id, title, content, author, date, p_id): # initialization function gets called as soon as object is created.
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.p_id = p_id

   # Saves post data to mongodb
   def save_to_mongo(self):
       Database.insert(collection='posts', data=self.json())

   # Creates/returns Json data for blog post based off init params passed
   def json(self):
       return {
           'p_id': self.p_id,
           'blog_id': self.blog_id
           'author': self.author
           'content': self.comtent
           'title': self.title
           'date': self.created_date
       }

