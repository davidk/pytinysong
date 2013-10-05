import sys

# for Python2 <-> Python3 interop
try:
    import http.client as httpclient
    import urllib.parse as urlparse
    from urllib.request import urlopen
except ImportError:
    import httplib as httpclient
    import urllib as urlparse

try:
    import simplejson as json
except ImportError:
    import json

TINYSONG_URL= 'tinysong.com'
TINYSONG_API_TYPE = 'json'
TINYSONG_HEADERS = {'Accept': 'application/json', 
                    'User-Agent':'pytinysong' }

class TinySongAPIError(Exception):
    ''' Exception raised when an error with the TinySong API is encountered '''

class TinySongConnectorError(Exception):
    ''' Raised when an error prevents the proper usage of the API '''

class TinySongConnector(object):
    tinysong_methods = { 'single':'/a/',
                         'meta':'/b/',
                         'search':'/s/',
    }

    def __init__(self, api_key=False, debug=False, tinysong_url=TINYSONG_URL, tinysong_api_type=TINYSONG_API_TYPE, tinysong_headers=TINYSONG_HEADERS):
        self.debug = debug
        self.tinysong_url = tinysong_url
        self.tinysong_api_type = tinysong_api_type
        self.tinysong_headers = tinysong_headers
        self.tinysong_api_key = api_key

        if not api_key:
            raise TinySongConnectorError("TinySongConnector requires an API key, please provide it by passing api_key=KEY.")	

    def get(self, query_type, query):
        path = self.build_api_path(query_type, query)
        return self.request('GET', path)

    def build_api_path(self,query_type,query):
        if not query_type in self.tinysong_methods:
            raise TinySongConnectorError("Query type is not supported by the API. Possible options are: %s" % (list(self.tinysong_methods.keys())))

        tinysong_query = self.tinysong_methods[query_type]
        processed_query = urlparse.quote_plus(query)

        return "%s%s?format=%s&key=%s" % (tinysong_query,processed_query,self.tinysong_api_type,self.tinysong_api_key)
    
    def request(self, request_type, path):
        query = httpclient.HTTPConnection(self.tinysong_url)
        query.request(request_type, path, None, self.tinysong_headers)
        result = query.getresponse()
        if result.status != 200:
            raise TinySongAPIError("An error occured at the Tinysong endpoint: %s" % (result.read()))

        data = result.read().decode('utf-8')

        api_data = []
        api_data = json.loads(data) 
        
        result.close()

        if 'error' in api_data:
            raise TinySongAPIError("An error occured at the TinySong endpoint: %s" % (api_data['error']))

        return api_data


