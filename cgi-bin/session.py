#!/usr/bin/python

import time, cgi, cgitb, pymysql, Cookie, random, string, os
import pages 




##################################
# Functions
##################################


def session_login(ip, email, password):
	cookie = '';

	#Check if login is successful
	db = pymysql.connect(host="127.0.0.1", unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='qanda')

	cursor = db.cursor();

	sql = "SELECT COUNT(idUsers) FROM Users WHERE Users.email = '%s' AND Users.password = '%s'" % (email, password);

	try:
	    cursor.execute(sql);
	    dataq = cursor.fetchall();
	except:
	    print("Error reading data from db.");


	# Create session and send cookie 

	if dataq[0][0]:

	    # Create session id and store in db
	    sid = generate_sid();
	    sql = "INSERT INTO Session (session_id, session_ip, Users_idUsers, session_last_access) VALUES ('%s', '%s', 1, 1)" % (sid, ip);

	    try:
		cursor.execute(sql);
		db.commit();
	    except:
		print "error writing to qanda.Session";

	    # Create a cookie
	    cookie = create_cookie(sid);

	# Close connection to database
	cursor.close();
	db.close();

	return cookie;


def session_check(ip):
	#Checks if there is an open session	
	if check_cookie():
		cookie = get_cookie();
		sid = cookie["SID"].value
		# Open db connection
		try:
			db = pymysql.connect(host="127.0.0.1", unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='qanda')
		except:
			print "Error opening db";

		cursor = db.cursor();
		# Check session id and client's ip
		sql = "SELECT COUNT(session_id) FROM Session WHERE Session.session_id = '%s' AND Session.session_ip = '%s'" % (sid, ip);
		#try:
		cursor.execute(sql);
		session_check = cursor.fetchall();
		#except:
		 #   print("Error reading data from db.");
		# Close db connection
		cursor.close();
		db.close();
		if session_check[0][0]:
			return True;			
	return False;





def check_cookie():
	# Check if client has a cookie
	return os.environ.get('HTTP_COOKIE')


def get_cookie():
	# Server gets client's cookie
	cookie = Cookie.SimpleCookie();
	cookie_string = check_cookie();
	cookie.load(cookie_string);
	return cookie;	


def create_cookie(sid):
	# Create cookie for server to send
	cookie = Cookie.SimpleCookie();
	cookie["SID"] = sid
	return cookie
	

def generate_sid():
	sid = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(45));
	return sid;
