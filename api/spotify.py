from __future__ import print_function
import base64
import json
import requests
# Workaround to support both python 2 & 3
try:
    import urllib.request, urllib.error
    import urllib.parse as urllibparse
except ImportError:
    import urllib as urllibparse

'''
    --------------------- HOW THIS FILE IS ORGANIZED --------------------

    0. SPOTIFY BASE URL
    1. ALBUMS : https://developer.spotify.com/web-api/album-endpoints/
    2. ARTISTS : https://developer.spotify.com/web-api/artist-endpoints/
    3. TRACKS : https://developer.spotify.com/web-api/search-item/
    4. USERS : https://developer.spotify.com/web-api/user-profile-endpoints/
    5. SEARCH : https://developer.spotify.com/web-api/search-item/

'''

# ----------------- 0. SPOTIFY BASE URL ----------------

SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# ------------------ 1. ALBUMS ------------------------
# https://developer.spotify.com/web-api/album-endpoints/

GET_ALBUM_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'albums')  # /<id>

# https://developer.spotify.com/web-api/get-album/
def get_album(album_id):
    url = "{}/{id}".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-several-albums/
def get_several_albums(list_of_ids):
    url = "{}/?ids={ids}".format(GET_ALBUM_ENDPOINT, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-albums-tracks/
def get_albums_tracks(album_id):
    url = "{}/{id}/tracks".format(GET_ALBUM_ENDPOINT, id=album_id)
    resp = requests.get(url)
    return resp.json()

# ---------------- 2. ARTISTS ------------------------
# https://developer.spotify.com/web-api/artist-endpoints/

GET_ARTIST_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'artists')  # /<id>

# https://developer.spotify.com/web-api/get-artist/
def get_artist(artist_id):
    url = "{}/{id}".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-several-artists/
def get_several_artists(list_of_ids):
    url = "{}/?ids={ids}".format(GET_ARTIST_ENDPOINT, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-artists-albums/
def get_artists_albums(artist_id):
    url = "{}/{id}/albums".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-artists-top-tracks/
def get_artists_top_tracks(artist_id, country='US'):
    url = "{}/{id}/top-tracks".format(GET_ARTIST_ENDPOINT, id=artist_id)
    myparams = {'country': country}
    resp = requests.get(url, params=myparams)
    return resp.json()

# https://developer.spotify.com/web-api/get-related-artists/
def get_related_artists(artist_id):
    url = "{}/{id}/related-artists".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url)
    return resp.json()

# ---------------- 3. TRACKS ------------------------
# https://developer.spotify.com/web-api/track-endpoints/

GET_TRACK_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'tracks')  # /<id>

# https://developer.spotify.com/web-api/get-track/
def get_track(track_id):
    url = "{}/{id}".format(GET_TRACK_ENDPOINT, id=track_id)
    resp = requests.get(url)
    return resp.json()

# https://developer.spotify.com/web-api/get-several-tracks/
def get_several_tracks(list_of_ids):
    url = "{}/?ids={ids}".format(GET_TRACK_ENDPOINT, ids=','.join(list_of_ids))
    resp = requests.get(url)
    return resp.json()

# ------------------ 4. USERS ---------------------------
# https://developer.spotify.com/web-api/user-profile-endpoints/

GET_USER_ENDPOINT = '{}/{}'.format(SPOTIFY_API_URL, 'users')

# https://developer.spotify.com/web-api/get-users-profile/
def get_user_profile(user_id):
    url = "{}/{id}".format(GET_USER_ENDPOINT, id=user_id)
    resp = requests.get(url)
    return resp.json()

# ----------------- 5. SEARCH ------------------------
# https://developer.spotify.com/web-api/search-item/

SEARCH_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'search')

# https://developer.spotify.com/web-api/search-item/
def search(search_types, name):
    for st in search_types:
        if st not in ['artist', 'track', 'album', 'playlist']:
            print('%s invalid type' % st)
            return None
    myparams = {'type': search_types}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, params=myparams)
    return resp.json()
