'''
    This code was based on these repositories,
    so special thanks to:
        https://github.com/datademofun/spotify-flask
        https://github.com/drshrey/spotify-flask-auth-example

'''

from flask import Flask, request, redirect, render_template
from src import spotify

app = Flask(__name__)

# ----------------------- AUTH API PROCEDURE -------------------------


@app.route("/auth")
def auth():
    print spotify.AUTH_URL
    return redirect(spotify.AUTH_URL)


@app.route("/callback/")
def callback():
    auth_token = request.args['code']
    print auth_token
    auth_header = spotify.authorize(auth_token)

    # get profile data
    profile_data = spotify.get_users_profile(auth_header)

    # get user playlist data
    # playlist_data = spotify.get_users_playlists(auth_header)

    # get user top artists
    # top_artists = spotify.get_users_top(auth_header, 'artists')

    # get user recently played
    # recently_played = spotify.get_users_recently_played(auth_header)

    print profile_data
    return render_template("profile.html",
                           user=profile_data)
                    #       playlists=playlist_data["items"],
                    #       top_artists=top_artists,
                    #       recently_played=recently_played)

# -------------------------- API REQUESTS ----------------------------


@app.route("/")
def index():
    return render_template('index.html')


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


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True, port=spotify.PORT)
