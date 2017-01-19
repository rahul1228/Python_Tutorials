import random

def msg(room):
	if room['msg'] == '': # if bunny has never entered this room
		return "You have entered the " + room['name'] + '.'
	else:
		return room['msg']

# Below, This is a function that checks to see if user inputted direction is valid.
def get_choice(room,dir): 
	if dir == 'N':
		choice = 0
	elif dir == 'E':
		choice = 1
	elif dir == 'S':
		choice = 2
	elif dir == 'W':
		choice = 3
	else:
		return -1

	if room['directions'][choice] == 0: # this checks to see if bunny is trying to go forward into a wall
		return 4
	else:
		return choice

def main():
	dirs = (0,0,0,0) # default direction tuple (N,E,S,W)

	# Create all 6 six Rooms using dictionaries
	entrance = {'name':'Entrance Way','directions':dirs,'msg':''}
	livingroom = {'name':'Livingroom','directions':dirs,'msg':''}
	hallway = {'name':'Hallway','directions':dirs,'msg':''}
	kitchen = {'name':'Kitchen','directions':dirs,'msg':''}
	diningroom = {'name':'Diningroom','directions':dirs,'msg':''}
	family_room = {'name':'Family Room','directions':dirs,'msg':''}
 
	# Below we are setting the values for the 'directions' key in the Room dicts. above.
	# Directions are tuples: Rooms to the (N,E,S,W).
	# Also shows in what directions the bunny can go in each room. 0 = bunny cant go there/wall with no door
	entrance['directions'] = (kitchen,livingroom,0,0)
	livingroom['directions'] = (diningroom,0,0,entrance)
	hallway['directions'] = (0,kitchen,0,family_room)
	kitchen['directions'] = (0,diningroom,entrance,hallway)
	diningroom['directions'] = (0,0,livingroom,kitchen)
	family_room['directions'] = (0,hallway,0,0)

	# Rooms where Rah's basket might be
	rooms = [livingroom,hallway,kitchen,diningroom,family_room] # rooms contains all 6 dictionaries from above
	rooms_with_eggs = random.choice(rooms) # picks random room from rooms list above using random.choice() fucntion
	eggs_delivered = False
	room = entrance # Bunny starts game in the entrance room
	print "Welcome Bunny! Can you find Rah\'s basket?"
	print "------------------------------------------"

	#---------------------Main Game Loop-------------------------
	while True:
		if eggs_delivered and room['name'] == 'Entrance Way': #if delivered eggs and found entrance
			print 'You have delivered the eggs and returned to the entrance. ' + 'You can now leave. Congrats!'
			break;
		elif not eggs_delivered and room['name'] == rooms_with_eggs['name']: # if bunny is in the room with eggs but hasn't delivered yet
			eggs_delivered = True
			print (msg(room) + ' There\'s the basket and Rah is sleeping ' + 'right next to it! You have delivered the eggs. ' + 'Now get out quick!') # since room['msg'] is still blank msg(room) returns just the current room name
			room['msg'] = ('You are back in the ' + room['name'] + '! You already delivered the eggs. ' + 'Get out of here before Rah wakes up!') # set this room['msg'] to this new cutom message letting u know u been here already and delivered last time.
		else: # else we are in some other room that doesn't have eggs/basket in it.
			print msg(room) # using msg() function
			room['msg'] = 'You are back in the ' + room['name'] # sets room['msg']

		# Below code is where user input on bunny direction is taken.
		# After input is give by user, it check to see if user has input valid directions for bunny
		# After it checks for direction validation, it will then check to see if bunny is facing a a wall with no door
		# If bunny is facing wall w/ no door and user inputs N which = 0 IN get_choice() function
		# then it will say you cant go there, 
		# otherwise stuck = false and bunny goes to that room the user specified/ room = room['directions']['user inputted choice']
		stuck = True 
		while stuck: 
			dir = raw_input("Which direction do you want to go: N,E,S, or W? ").upper() #1st User interaction
			choice = get_choice(room,dir)
			if choice == -1:
				print "Please enter N,E,S, or W: "
			elif choice == 4: 
				print "You cannot go in that direction. "
			else:
				room = room['directions'][choice] # BUNNY GOES TO ROOM USER SPECIFIED
				stuck = False



main()