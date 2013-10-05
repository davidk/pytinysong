class Song(object):
    url = None
    song_id = None
    song_name = None
    artist_id = None
    artist_name = None
    album_id = None
    alumn_name = None

    # Old style CamelCase properties (still supported)
    Url = None
    SongId = None
    SongName = None
    ArtistID = None
    ArtistName = None
    AlbumId = None
    AlbumName = None

    def __init__(self, data):
        for name, value in list(data.items()):
            setattr(self, name, value)
