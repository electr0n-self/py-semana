""" semana - Web Session Management Module

    Author: Natalia Guaraldi
    Date: 2015
    Version: 0.1.0

"""

import Cookie, random, string, os


class Session(object):
    """ Session object."""

    def __init__(self, user_ip, domain, expiration):
        self.valid = True
        self.user_ip = user_ip
        # Generate SID
        sid = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(45))
        self.sid = sid
        # Create session in db
        # Create cookie
        cookie = Cookie.SimpleCookie()
        cookie['SID'] = self.sid
        cookie['domain'] = domain
        cookie['expiration'] = expiration
        self.cookie = cookie

    def start(self):
        """ Start session. """
        # Start db
        pass

    def check(self):
        """ Check if session is still valid."""
        self.close()
        return False

    def close(self):
        """ Finish the session. """
        # Update db
        # Close db connection
        pass


class SessionCookie(Cookie.SimpleCookie):
    """ Session cookie. """

    def __init__(self, sid, domain, expiration):
        pass


def check_cookie():
    """ REMOVE THIS
    Check if client has a cookie and, if so, returns it."""
    cookie_string = os.environ.get('HTTP_COOKIE')

    if cookie_string:
        cookie = Cookie.SimpleCookie()
        cookie.load(cookie_string)
        return cookie
    else:
        return ""

