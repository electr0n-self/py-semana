#! /usr/bin/python


import Cookie, pymysql, os
import pages, session


ip = os.environ["REMOTE_ADDR"];

if session.session_check(ip):   
	pages.simple_page("OK!");
else:
    #go to secured area
    pages.login_page();


