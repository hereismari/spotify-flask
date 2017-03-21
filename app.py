'''
    This code was based on these repositories,
    so special thanks to:
        https://github.com/datademofun/spotify-flask
        https://github.com/drshrey/spotify-flask-auth-example

'''

import base64
from flask import Flask, request, redirect, g, render_template
import json
import requests
import urllib

from src import spotify

app = Flask(__name__)

# ------------------------- CONF VARIABLES ---------------------------

# client keys
CLIENT = json.load(open('conf.json', 'r+'))
CLIENT_ID = CLIENT['id']
CLIENT_SECRET = CLIENT['secret']

# spotify urls
SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

# server side parameter
# * fell free to change it if you want to, but make sure to change in
# your spotify dev account as well
CLIENT_SIDE_URL = "http://127.0.0.1"
PORT = 8080
REDIRECT_URI = "{}:{}/callback/".format(CLIENT_SIDE_URL, PORT)
SCOPE = "playlist-modify-public playlist-modify-private"
STATE = ""
SHOW_DIALOG_bool = True
SHOW_DIALOG_str = str(SHOW_DIALOG_bool).lower()

# ----------------------- AUTH API PROCEDURE -------------------------

# https://developer.spotify.com/web-api/authorization-guide/
auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    # "state": STATE,
    # "show_dialog": SHOW_DIALOG_str,
    "client_id": CLIENT_ID
}

@app.route("/auth")
def auth():
    # authorization
    url_args = "&".join(["{}={}".format(key,urllib.quote(val)) for key,val in auth_query_parameters.iteritems()])
    auth_url = "{}/?{}".format(SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)

@app.route("/callback/")
def callback():
    # requests refresh and access tokens
    auth_token = request.args['code']
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": REDIRECT_URI
    }
    base64encoded = base64.b64encode("{}:{}".format(CLIENT_ID, CLIENT_SECRET))
    headers = {"Authorization": "Basic {}".format(base64encoded)}
    post_request = requests.post(SPOTIFY_TOKEN_URL, data=code_payload, headers=headers)

    # tokens are returned to the app
    response_data = json.loads(post_request.text)

    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]

    # use the access token to access Spotify API
    authorization_header = {"Authorization":"Bearer {}".format(access_token)}

    # get profile data
    user_profile_api_endpoint = "{}/me".format(SPOTIFY_API_URL)
    profile_response = requests.get(user_profile_api_endpoint, headers=authorization_header)
    profile_data = json.loads(profile_response.text)

    # get user playlist data
    playlist_api_endpoint = "{}/playlists".format(profile_data["href"])
    playlists_response = requests.get(playlist_api_endpoint, headers=authorization_header)
    playlist_data = json.loads(playlists_response.text)

    # combine profile and playlist data to display
    display_arr = [profile_data] + playlist_data["items"]
    return render_template("profile.html", sorted_array=display_arr)

# -------------------------- API REQUESTS ----------------------------

@app.route("/")
def index():
    return render_template('index.html')

# ---------------- search --------------------------

@app.route('/search/')
def search():

    try:
        search_type = request.args['search_type']
        name = request.args['name']
        return make_search(search_type, name)
    except:
        return render_template('search.html', search_item='')

@app.route('/search/<search_type>/<name>')
def search_item(search_type, name):
    return make_search(search_type, name)

def make_search(search_type, name):
    if search_type not in ['artist', 'album', 'playlist', 'track']:
        return render_template('index.html')

    data = spotify.search(search_type, name)
    api_url = data[search_type + 's']['href']
    items = data[search_type + 's']['items']

    return render_template('search.html',
                            name=name,
                            results=items,
                            api_url=api_url,
                            search_item=search_type)

@app.route('/artist/<id>')
def artist(id):
    artist = spotify.get_artist(id)

    if artist['images']:
        image_url = artist['images'][0]['url']
    else:
        image_url = 'http://placecage.com/600/400'

    tracksdata = spotify.get_artist_top_tracks(id)
    tracks = tracksdata['tracks']

    related = spotify.get_related_artists(id)
    related = related['artists']

    return render_template('artist.html',
                            artist=artist,
                            related_artists=related,
                            image_url=image_url,
                            tracks=tracks)


if __name__ == "__main__":
    app.run(debug=True,port=PORT)
