__author__ = 'pavel'
import urllib2
from alphaUp.dropbox import client, session
from alphaUp.settings import ACCESS_TYPE, APP_KEY, APP_SECRET

sess = session.DropboxSession(APP_KEY,APP_SECRET,ACCESS_TYPE)
def login(url_authorize):
    

