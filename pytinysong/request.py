#!/usr/bin/env python
''' pytinysong -- Python interface to the Tinysong API

'''

from .connection import TinySongConnector
from .structs import Song

class TinySongRequest(object):
    tinysong_api_map = { 'Url': 'url',
                         'SongID': 'song_id',
                         'SongName': 'song_name',
                         'ArtistID': 'artist_id',
                         'ArtistName': 'artist_name',
                         'AlbumID': 'album_id',
                         'AlbumName': 'album_name',
    }

    def __init__(self, api_key=False, debug=False):
        self.tinysong = TinySongConnector(api_key=api_key, debug=debug)

    def __map_api_methods(self, results):
        # Older methods are kept mapped for backwards compatibility
        for key,data in list(results.items()):
            results[self.tinysong_api_map[key]] = data 
        return results

    def request_link(self, query):
        return self.tinysong.get('single',query) 

    def request_metadata(self, query):
        return Song(self.__map_api_methods(self.tinysong.get('meta',query)))

    def search(self, query):
        songs = []
        for entry in self.tinysong.get('search',query):
            songs.append(Song(self.__map_api_methods(entry)))
        return songs
