pytinysong
==========

[![Build Status](https://travis-ci.org/davidk/pytinysong.png?branch=master)](https://travis-ci.org/davidk/pytinysong)

A Python interface to the Tinysong (Grooveshark backed) service:

    >>> from pytinysong.request import TinySongRequest
    >>> song = TinySongRequest(api_key='z1cx2j1mgk19jm3j')
    >>> results = song.search('Overseer - Supermoves')
    >>> for song in results:
    ...     print(song.artist_name, '-', song.song_name)
    ... 
    Overseer - Supermoves
    Overseer - Supermoves [Animatrix Remix]

About the API key
-----------------
TinySong now requires an API key. Registration is available by visiting the [TinySong](http://www.tinysong.com/api) website.

Song() object properties
------------------------

* url -- A link to the song on TinySong/Grooveshark
* song_id -- ID of the song retrieved
* song_name -- Name of the song retrieved
* artist_id -- ID of the artist
* artist_name -- Name of the artist
* album_id -- ID of the album retrieved
* album_name -- Name of the album retrieved

These properties are also available in CamelCase (similar to the exported JSON keys from Tinysong):

* Url
* SongID
* SongName
* ArtistID
* ArtistName
* AlbumID
* AlbumName

Available Methods
-----------------

Where `query` is a string (usually something like the artist name, or the name+song title):

* request_link(query) -- Returns a (string) link to the song
* request_metadata(query) -- Returns a Song() object with the song data
* search(query) -- Returns a list of Song() objects with data on various songs

License
-------

CC0 Public Domain.
Using it for world domination is (still) allowed. More information [here](http://creativecommons.org/publicdomain/zero/1.0/).
