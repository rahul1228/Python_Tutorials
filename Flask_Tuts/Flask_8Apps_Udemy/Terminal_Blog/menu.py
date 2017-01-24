from database import  Database
from models.blog import Blog


class Menu(object):

    # Ask user for author name
    # Check if they've already got an account
    # If not, prompt them to create one
    def __init__(self):
        self.user = raw_input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print "Welcome back, {}".format(self.user)
        else:
            self._prompt_user_for_account()

    # Query's blogs collection in mongodb for an author, using self.user user input
    # Used find_one() function/method which querys a collection in mongodb
    # if author has a blog/account self.user = blog
    # returns True meaning we have a blog and  now an account
    # else if author name has no blogs/account then returns False
    def _user_has_account(self):
        blog = Database.find_one(collection='blogs', query={'author': self.user})
        if blog is not None:
            # from_mongo function from Blog class finds blog according to id and stores in self.user_blog
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        title = raw_input("Enter blog title: ")
        description = raw_input("Enter blog description: ")
        # Blog Object created
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    # Menu
    def run_menu(self):
        read_or_write = raw_input("Do you want to read (R) or write (W) blogs? ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
        elif read_or_write == 'W':
            self.user_blog.new_post()
        else:
            print "Thank you for blogging!"

    # Lists all blogs in a collection
    # prints blog id, title, and author from said blog
    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={}) # empty query query's all blogs in collection
        for blog in blogs:
            print "ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author'])

    # Lets user pick a blog to read posts in, by passing in blog id
    # Gets all posts from said blog
    # prints date, title, and post info from said blog
    def _view_blog(self):
        blog_to_see = raw_input("Enter the ID of the blog you'd like to read: ")
        # from_mongo function from Blog class finds blog according to id and stores in blog var
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts() # gets all posts from blog
        for post in posts:
            print ("Title: {}\n Post:\n {}".format(post['title'], post['content']))








