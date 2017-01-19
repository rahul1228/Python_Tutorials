from flask import Flask

# Instaitate/Create flask app
app = Flask(__name__)

#App Route for index.html, '/' indicates the index location
@app.route('/')
def index():
	return '<h1>Hello There!</h1>'

# This browser route for homepage accepts GET & POST methods
@app.route('/home', methods=['GET','POST,'])
def home():
	return '<h1>You are on the home page!</h1>'

# This page route has a var that can be passed in with browser
# that passed in var can be used in function
@app.route('/page/<place>')
def page(place):
	return '<h1>You are on the '+ place +' page!</h1>'

if __name__ == '__main__':
	app.run(debug=True) # debug=True enables debug mode for non production