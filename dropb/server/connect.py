__author__ = 'pavel'
import mechanize
import urllib2
from dropbox import clients, session
from settings import ACCESS_TYPE, APP_KEY, APP_SECRET

sess = session.DropboxSession(APP_KEY,APP_SECRET,ACCESS_TYPE)
class Connection(object):
    email = ""
    password = ""
    root_ns = ""
    token = ""
    browser = None

    def __init__(self,email,password):
        self.email = email
        self.password = password

    def login(self):


