print("""
	--------------------Welcome To Contact List--------------------
	
	---------------------------------------------------------------""")

def displayuserinfo(userinfo):
	print("+++++++++++++++++++++++++++++++++++++++++++++++++")
	print("-------------------------------------------------")
	print("!! Match found for: ",userinfo[0],"",userinfo[1],"!!")
	print("First Name: ",userinfo[0])
	print("Last Name: ",userinfo[1])
	print("Address: ",userinfo[2])
	print("Email: ",userinfo[3])
	print("Ph # : ",userinfo[4])
	print("-------------------------------------------------")
	return

firstname = ""
lastname = ""
entryfound = ""

#--------------Getting User Input----------------
while firstname != "quit":
	firstname = raw_input("Enter the person's First Name (quit to end):")
	firstname = firstname.lower()

	if firstname == "quit":
		break
	else:
		lastname = raw_input("Enter ther person's Last Name:")
		lastname = lastname.lower()
		#----Checking/Searching Contact List------------
		contactlist = open("C:/Users/rahul/Desktop/PYTHON PROJECTS/Tutorials/Searchable Contact List/db.txt")
		
		for line in contactlist:
			userinfo = line.split('|')
			if ((userinfo[0].lower() == (firstname or firstname.lower)) and (userinfo[1].lower() == (lastname or lastname.lower))):
				entryfound = True
				break
			else:
				entryfound = False
				continue #if false it continues to search the list/for loop
	#---------Display Data--------------------------
	if entryfound == False:
		print "!!Sorry, that person doesnt exist!!"
	else:
		displayuserinfo(userinfo)
	contactlist.close()
	entryfound = ""




