class Song(object):
    Url = None
    SongId = None
    SongName = None
    ArtistID = None
    ArtistName = None
    AlbumId = None
    AlbumName = None

    def __init__(self, data):
        for name, value in data.iteritems():
            setattr(self, name, value)
