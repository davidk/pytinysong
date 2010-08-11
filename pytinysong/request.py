#!/usr/bin/env python
''' pytinysong -- Python interface to the Tinysong API

'''

from connection import TinySongConnector
from structs import Song

class TinySongRequest(object):
    def __init__(self, debug=False):
        self.tinysong = TinySongConnector(debug=debug)

    def request_link(self, query):
        return self.tinysong.get('single',query) 

    def request_metadata(self, query):
        return Song(self.tinysong.get('meta',query))

    def search(self, query):
        songs = []
        for entry in self.tinysong.get('search',query):
            songs.append(Song(entry))
        return songs
