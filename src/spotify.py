import base64
import json
import requests
import urllib

'''
    --------------------- HOW THIS FILE IS ORGANIZED --------------------

    0. SPOTIFY BASE URL
    1. USER AUTHORIZATION
    2. ARTISTS
    3. SEARCH
    4. USER RELATED REQUETS

'''

# ----------------- 0. SPOTIFY BASE URL ---------------- #

SPOTIFY_API_BASE_URL = 'https://api.spotify.com'
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# ----------------- 1. USER AUTHORIZATION ---------------- #

# spotify endpoints
SPOTIFY_AUTH_BASE_URL = "https://accounts.spotify.com/{}"
SPOTIFY_AUTH_URL = SPOTIFY_AUTH_BASE_URL.format('authorize')
SPOTIFY_TOKEN_URL = SPOTIFY_AUTH_BASE_URL.format('api/token')

# client keys
CLIENT = json.load(open('conf.json', 'r+'))
CLIENT_ID = CLIENT['id']
CLIENT_SECRET = CLIENT['secret']

# server side parameter
# * fell free to change it if you want to, but make sure to change in
# your spotify dev account as well *
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8081
REDIRECT_URI = "{}:{}/callback/".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

# https://developer.spotify.com/web-api/authorization-guide/
auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

URL_ARGS = "&".join(["{}={}".format(key, urllib.quote(val))
                    for key, val in auth_query_parameters.iteritems()])
AUTH_URL = "{}/?{}".format(SPOTIFY_AUTH_URL, URL_ARGS)

'''
    This function must be used with the callback method present in the
    ../app.py file.
'''


def authorize(auth_token):

    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }

    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))

    headers = {"Authorization": "Basic {}".format(base64encoded)}

    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload,
                                 headers=headers)

    # tokens are returned to the app
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]

    # use the access token to access Spotify API
    auth_header = {"Authorization": "Bearer {}".format(access_token)}
    return auth_header

# ---------------- 2. ARTISTS ------------------------ #


# spotify endpoints
GET_ARTIST_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'artists')  # /<id>
RELATED_ARTISTS_ENDPOINT = "{}/{}".format(GET_ARTIST_ENDPOINT,
                                          'related-artists')
ARTISTS_TOP_TRACKS_ENDPOINT = "{}/{}".format(GET_ARTIST_ENDPOINT, 'top-tracks')


# https://developer.spotify.com/web-api/get-artist/
def get_artist(artist_id):
    url = "{}/{id}".format(GET_ARTIST_ENDPOINT, id=artist_id)
    resp = requests.get(url)
    return resp.json()


# https://developer.spotify.com/web-api/get-related-artists/
def get_related_artists(artist_id):
    url = RELATED_ARTISTS_ENDPOINT.format(id=artist_id)
    resp = requests.get(url)
    return resp.json()


# https://developer.spotify.com/web-api/get-artists-top-tracks/
def get_artist_top_tracks(artist_id, country='US'):
    url = ARTISTS_TOP_TRACKS_ENDPOINT.format(id=artist_id)
    myparams = {'country': country}
    resp = requests.get(url, params=myparams)
    return resp.json()


# ----------------- 3. SEARCH ------------------------ #

# spotify endpoints
SEARCH_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'search')


# https://developer.spotify.com/web-api/search-item/
def search(search_type, name):
    if type not in ['artists', 'tracks', 'albums', 'playlists']:
        print 'invalid type'
        return None
    myparams = {'type': search_type}
    myparams['q'] = name
    resp = requests.get(SEARCH_ENDPOINT, params=myparams)
    return resp.json()

# ------------------ 4. USER RELATED REQUETS  ---------- #


# spotify endpoints
USER_PROFILE_ENDPOINT = "{}/{}".format(SPOTIFY_API_URL, 'me')
USER_PLAYLISTS_ENDPOINT = "{}/{}".format(USER_PROFILE_ENDPOINT, 'playlists')
USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT = "{}/{}".format(
    USER_PROFILE_ENDPOINT, 'top')  # /<type>
USER_RECENTLY_PLAYED_ENDPOINT = "{}/{}/{}".format(USER_PROFILE_ENDPOINT,
                                                  'player', 'recently-played')


# https://developer.spotify.com/web-api/get-users-profile/
def get_users_profile(auth_header):
    url = USER_PROFILE_ENDPOINT
    resp = requests.get(url, headers=auth_header)
    return resp.json()


# https://developer.spotify.com/web-api/get-a-list-of-current-users-playlists/
def get_users_playlists(auth_header):
    url = USER_PLAYLISTS_ENDPOINT
    resp = requests.get(url, headers=auth_header)
    return resp.json()


# https://developer.spotify.com/web-api/get-users-top-artists-and-tracks/
def get_users_top(auth_header, type):
    if type not in ['artists', 'tracks']:
        print 'invalid type'
        return None
    url = "{}/{type}".format(USER_TOP_ARTISTS_AND_TRACKS_ENDPOINT, type=type)
    print url
    resp = requests.get(url, headers=auth_header)
    return resp.json()


# https://developer.spotify.com/web-api/web-api-personalization-endpoints/get-recently-played/
def get_users_recently_played(auth_header):
    url = USER_RECENTLY_PLAYED_ENDPOINT
    resp = requests.get(url, headers=auth_header)
    return resp.json()
