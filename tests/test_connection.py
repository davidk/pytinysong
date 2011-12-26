#!/usr/bin/env python
''' Nose tests for the connection code portions

'''

from pytinysong.connection import TinySongConnector, TinySongConnectorError
from pytinysong.request import TinySongRequest
from nose.tools import eq_, raises, ok_
from private_data import KEY

@raises(TinySongConnectorError)
def test_make_api_path_fail():
    song = TinySongConnector(api_key=KEY) 
    song.build_api_path("invalid_query_type","Cake - The Distance")

def test_request_link():
    song = TinySongRequest(api_key=KEY)
    eq_('http://tinysong.com/IaZs',song.request_link('Samantha James - Maybe Tomorrow'))

def test_request_metadata():
    song = TinySongRequest(api_key=KEY)
    result = song.request_metadata('Kylie - Better Than Today (Bellatrax Remix)')
    eq_(result.url,'http://tinysong.com/IevF')

def test_request_search():
    song = TinySongRequest(api_key=KEY)
    results = song.search('Overseer')
    ok_(len(results) > 0)
    
