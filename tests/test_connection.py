#!/usr/bin/env python
''' Nose tests for the connection code portions

'''

from pytinysong.connection import TinySongConnector, TinySongConnectorError
from pytinysong.request import TinySongRequest
from nose.tools import eq_, raises, ok_

@raises(TinySongConnectorError)
def test_make_api_path_fail():
    song = TinySongConnector() 
    song.build_api_path("invalid_query_type","Cake - The Distance")

def test_request_link():
    song = TinySongRequest()
    eq_('http://tinysong.com/93I',song.request_link('Zero 7 - Destiny'))

def test_request_metadata():
    song = TinySongRequest()
    result = song.request_metadata('FC Kahuna - Hayling')
    eq_(result.Url,'http://tinysong.com/mTqQ')

def test_request_search():
    song = TinySongRequest()
    results = song.search('Overseer')
    ok_(len(results) > 0)
    
