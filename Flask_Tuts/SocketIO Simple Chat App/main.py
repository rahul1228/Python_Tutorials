from flask import Flask
from flask_socketio import SocketIO, send

# Create/Instantiate Flask App in app var 
app = Flask(__name__) 
app.config['SECRET_KEY'] = 'mysecret' # .config works like a dictionary

#Instantiate socketio and passing in the app
socketio = SocketIO(app) 

# Below = Socketio decorator that listens for an event, in this case on message event
# Then when that event triggers it runs the function under it
@socketio.on('message')
def handleMessage(msg): # Stores message in msg and sends to everyone
	print 'Message: ' + msg # in conlsole just for a check 
	send(msg, broadcast=True) # sends message to anyone on the server at that moment
	# ^ broadcast = true makes send function from socketio send message to all participants in server

# Below routes index.html to the 172.0.0.1:5000 location
# In render_template() fucntion param messages=messages tells index.html that...
# ...messages var here = messages id in index.html
@app.route('/')
def index():
	messages = ['message 1','message 2','message 3'] # dummy default history messages
	return render_template('index.html', messages=messages)

if __name__ == '__main__':
	socketio.run(app) #Runs flask app in a socketio wrapper