from flask import Flask, render_template

# Instaitate/Create flask app
app = Flask(__name__)

#App Route for index.html, '/' indicates the index location
@app.route('/')
def index():
	return '<h1>Hello There!</h1>'

# This browser route for homepage accepts GET & POST methods
# Other params in render_template() function sends those var data to the html file to be used
@app.route('/home', methods=['GET','POST,'])
def home():
	links = ['https://www.youtube.com','https://www.bing.com','https://www.amazon.com']
	return render_template('example.html', myvar='boggboogboo', links=links)

# This page route has a var that can be passed in with browser
# that passed in var can be used in function
@app.route('/page/<place>')
def page(place):
	return '<h1>You are on the '+ place +' page!</h1>'

if __name__ == '__main__':
	app.run(debug=True) # debug=True enables debug mode for non production