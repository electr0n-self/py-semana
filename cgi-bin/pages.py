#! /usr/bin/python


def simple_page(message):
    print "Content-Type: text/html; charset=utf-8\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>Simple Page</title>"
    print "</head>"
    print "<body>"
    print "<h2>Hello again!"
    print "<p>'%s'</p>" % (message)
    print "</body>"
    print "</html>"


def login_page():
    print "Content-Type: text/html; charset=utf-8\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>LOGIN</title>"
    print "</head>"
    print "<body>"
    print "<h2>This should be a LOGIN page.</h2>"
    print "<p>You must login again.</p>"
    print "</body>"
    print "</html>"


def secure_area_page(email, password, cookie=''):
    if cookie:
	print cookie; 
    print "Content-Type: text/html; charset=utf-8\r\n\r\n"
    print "<html>"
    print "<head>"
    print "<title>LOGIN</title>"
    print "</head>"
    print "<body>"
    print "<h2>Hello, %s %s</h2>" % (email, password)
    print "<p>Login successful. We've sent you a cookie.</p>"
    print "<a href='securearea.py'>Next</a>"
    print "</body>"
    print "</html>"


