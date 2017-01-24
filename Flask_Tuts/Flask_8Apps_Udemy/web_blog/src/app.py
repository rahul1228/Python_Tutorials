from flask import Flask

# Create Flask app object
app = Flask(__name__) #__name__ = __main__

@app.route('/') # local host/ base site/ default location/ www.mysite.com/api/
def hello_method():
    return "Hello, ya bish!"

if __name__ == "__main__":
    app.run()