import sys
import os
import random

class Player:
	# __init__() function means INSTANTIATE. 
	# This function runs when the Player class is called.
	# In this case it sets all the Player's variables/attributes
	def __init__(self, name): 
		self.name = name
		self.maxhealth = 100
		self.health = self.maxhealth
		self.attack = 10
		self. gold = 0
		self.pots = 0

class Goblin:
	def __init__(self, name):
		self.name = name
		self.maxhealth = 50
		self.health = self.maxhealth
		self.attack = 5
		self.goldgain = 10 # How much gold player gets after killing goblin

GoblinIG = Goblin("Goblin") # Goblin object instance

class Zombie:
	def __init__(self, name):
		self.name = name
		self.maxhealth = 70
		self.health = self.maxhealth
		self.attack = 7
		self.goldgain = 15 # How much gold player gets after killing goblin

ZombieIG = Zombie("Zombie") # Zombie object instance

def main():
	os.system('cls') # clears console/terminal of any prior text/data
	print "Welcome to The Text Adventure Game!\n"
	print "1) Start"
	print "2) Load"
	print "3) Exit"
	option = raw_input("--> ") 
	# raw_input only takes input as a string so in IF below u see "1"
	if option == "1":
		start()
	elif option == "2":
		pass
	elif option == "3":
		sys.exit() # from sys library/package/module
	else:
		main()

def start(): 
	os.system('cls') # clears console/terminal of any prior text/data
	print "Hello, what is your name?:"
	option = raw_input("--> ")
	global PlayerIG # makes PlayerIG in a global Player object to be used by other functions
	PlayerIG = Player(option) 
	# ^PlayerIG object created using Player class. Giving the player a name here
	start1()

def start1():
	os.system('cls') # clears console/terminal of any prior text/data
	print "Hello %s. How are you?" % PlayerIG.name
	print "Attack: %i" % PlayerIG.attack
	print "Gold: %i" % PlayerIG.gold
	print "Potions: %i" % PlayerIG.pots
	print "Health: %i/%i \n" % (PlayerIG.health,PlayerIG.maxhealth)
	print "1) Fight"
	print "2) Store"
	print "3) Save"
	print "4) Exit"
	option = raw_input("--> ")
	if option == "1":
		prefight()
	elif option == "2":
		store()
	elif option == "3":
		pass
	elif option == "4":
		sys.exit()
	else:
		start1()

def prefight():
	global enemy # setting enemy variable to be global so other functions can use it.
	enemynum = random.randint(1,2)
	if enemynum == 1:
		enemy = GoblinIG # Goblin object stored in enemy
	else:
		enemy = ZombieIG # Zombie object stored in enemy
	fight()

def fight():
	os.system('cls') 
	print "%s   vs   %s" % (PlayerIG.name, enemy.name)
	print "%s Health: %i/%i | %s Health: %d/%d" % (PlayerIG.name,PlayerIG.health,PlayerIG.maxhealth,enemy.name,enemy.health,enemy.maxhealth)
	print "Potions: %i\n" % PlayerIG.pots
	print "1) Attack"
	print "2) Drink Potion"
	print "3) Run"
	option = raw_input("--> ")
	if option == "1":
		attack()
	elif option == "2":
		drinpot()
	elif option == "3":
		run()
	else:
		fight()

def attack():
	os.system('cls') # clears terminal
	PAttack = random.randint(PlayerIG.attack/2,PlayerIG.attack)
	EAttack = random.randint(enemy.attack/2,enemy.attack)
	if PAttack == PlayerIG.attack/2:
		print "You missed!"
	else:
		enemy.health -= PAttack
		print "Hit! You delt %i damage." % PAttack
	option = raw_input('')
	os.system('cls') # clears terminal




def drinkpot():
	pass

def run():
	pass

def store():
	pass


main()


