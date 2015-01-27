#!/usr/bin/python

import time, cgi, cgitb, pymysql, Cookie, random, string, os
import pages, session 



# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
email = form.getvalue('email')
#email = cgi.escape(email);

password = form.getvalue('password')
#password = cgi.escape(password);



# Get client's ip
ip = os.environ["REMOTE_ADDR"];


#Check if there is a valid session
if session.session_check(ip):
	pages.secure_area_page(email, password);

else:
	# Try to login
	cookie = session.session_login(ip, email, password);

	if cookie:
		pages.secure_area_page(email, password, cookie);
	else:
		pages.login_page();
	



