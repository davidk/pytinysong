pytinysong
==========

A Python interface to the Tinysong (Grooveshark backed) service:

    >>> from pytinysong.request import TinySongRequest
    >>> song = TinySongRequest()
    >>> results = song.search('Overseer - Supermoves')
    >>> for song in results:
    ...     print song.ArtistName, '-', song.SongName
    ... 
    Overseer - Supermoves
    Overseer - Supermoves [Animatrix Remix]
    Overseer - Supermoves (Animatrix)

Properties of Song() objects
----------------------------
* Url -- A link to the song on TinySong/Grooveshark
* SongId -- ID of the song retrieved
* SongName -- Name of the song retrieved
* ArtistID -- ID of the artist
* ArtistName -- Name of the artist
* AlbumId -- ID of the album retrieved
* AlbumName -- Name of the album retrieved

Available Methods
-----------------

Where `query` is a string (usually something like the artist name, or the name+song title):

* request_link(query) -- Returns a (string) link to the song
* request_metadata(query) -- Returns a Song() object with the song data
* search(query) -- Returns a list of Song() objects with data on various songs

License
-------

pytinysong is licensed under the WTFPL
