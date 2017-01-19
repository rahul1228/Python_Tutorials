import ImageGrab 
import os 
import time 

#Globals
x_pad = 457
y_pad = 240
#-----------------------

def screenGrab():
	box = (x_pad+1,y_pad+1,x_pad+654,y_pad+491) #pixel coordinates for game in screenshot
	im = ImageGrab.grab(box) 
	im.save(os.getcwd() + '\\fullsnap__' + str(int(time.time())) + '.png', 'PNG')

def main():
	screenGrab()

if __name__ == '__main__':
	main()

#Line 1: gives us the basic screen gabbing functionality 
#Line 2: gives us the ability to easily navigate around our operating system's directories
#Line 3: built-in Time module. use this mostly for stamping the current time onto snapshots, but it can be very useful as a timer for bots that need events triggered over a given number of seconds
#Line 6: empty tuple which is a list that cant change once created
#Line 7: grab function from ImageGrab creates full snapshot of screen and returns RGB image to the instance im.
#Line 8: 1stpart calls the save() function on im. The save method takes 2 arguments (file save location, file format)
#Line 8c: 1st argument setssave location by calling os.getcwd() which gets current wor. dir. the code is being run from and return it as a string.
#Line 8c: seconfd part of 1st arg. '\\full_snap__' gives our file simple discriptive name.
#Line 8c: str(int(time.time())) . This takes advantage of Python's built-in Type methods
#Line 8c: time.time() returns the number of seconds since Epoch, which is given as a type Float. Since we're creating a file name we can't have the decimal in there, so we first convert it to an integer by wrapping it in int()
#Line 8c: + '.png' and passing the second argument which is again the extension's type: "PNG"
#Line 10: defines the function main(), and tells it to call the screenGrab() function whenever it's run.
#Line 13: is a Python convention that checks whether the script is top level, and if so allows it to run. Translated, it simply means that that it only executes main() if it is run by itself. Otherwise - if, for instance, it is loaded as a module by a different Python script - it only supplies its methods instead of executing its code.
