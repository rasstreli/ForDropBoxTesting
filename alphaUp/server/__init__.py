__author__ = 'pavel'
import httplib
import simplejson
import urllib

class RESTClient(object):
    """

    """

    def __init__(self, host,port):
        self.host = host
        self.port = port

    def request(self, method, url, post_params = None, headers = None, raw_response = None):
        body = None
        params = post_params or {}
        headers = headers or {}
        if params:
            body = urllib.urlencode(params)
        if body:
            headers['Content-type'] = "application/x-www-form-urlencode"

        conn = httplib.HTTPConnection(self.host,self.port)
        conn.request(method, url, body)
        if raw_response:
            return conn.getresponse()
        else:
            resp = RESTResponse(conn.getresponse())
            conn.close()
        return resp



class RESTResponse(object):
    """

    """

    def __init__(self, http_resp):
        self.http_response = http_resp
        self.status  = http_resp.status
        self.reason  = http_resp.reason
        self.body    = http_resp.read()
        self.headers = dict(http_resp.get_headers())

        try:
            self.data = simplejson.load(self.body)
        except ValueError:
            self.data = None