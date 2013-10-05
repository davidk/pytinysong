''' Nose tests for the request code portions

'''

from pytinysong.request import TinySongRequest
from nose.tools import ok_
from private_data import KEY


def test_request_link():
    song = TinySongRequest(api_key=KEY)
    data = song.request_link('Zero 7 - Destiny')
    ok_(data.startswith("http://tinysong.com"))


def test_request_metadata():
    song = TinySongRequest(api_key=KEY)
    data = song.request_metadata('Overseer - Supermoves')
    ok_("Overseer" in data.artist_name or "Supermoves" in data.song_name)


def test_request_metadata_old_property():
    song = TinySongRequest(api_key=KEY)
    data = song.request_metadata('Zero 7 - Destiny')
    ok_(data.ArtistID)
