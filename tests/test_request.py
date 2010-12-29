#!/usr/bin/env python
''' Nose tests for the request code portions

'''

from pytinysong.request import TinySongRequest
from nose.tools import eq_, ok_

def test_request_link():
    song = TinySongRequest()
    data = song.request_link('Zero 7 - Destiny')
    eq_('http://tinysong.com/93I',data)

def test_request_metadata():
    song = TinySongRequest()
    data = song.request_metadata('Overseer - Supermoves')
    eq_('Overseer',data.artist_name)

def test_request_metadata_old_property():
    song = TinySongRequest()
    data = song.request_metadata('Zero 7 - Destiny')
    eq_(1654,data.ArtistID)
