# spotify-flask

Here you'll find a very straightforward way to request data from Spotify API using flask with templates. Or just use the [Python
API](http://github.com/mari-linhares/spotify-flask/api/) to make the requests for your application.

I'm creating this repository because I have not found a full (or almost full) implementation of a Flask app using Spotify API, altough
https://github.com/datademofun/spotify-flask and https://github.com/drshrey/spotify-flask-auth-example have some nice work, and I'm
grateful for these repositories :smile:!

![Image](https://github.com/mari-linhares/spotify-flask/blob/master/imgs/profile.png?raw=true)

## How can I run it?

1. Follow [this tutorial](https://developer.spotify.com/web-api/tutorial/) to create your own Spotify App.
   Add "http://127.0.0.1:8081/callback/" as a redirect URI  

2. Create a file named **conf.json** in this folder with the exact same structure of the conf_example.json file  

3. Run python app.py to see a application using the code present here :bowtie:

## What facilities does this application offers?

 * Support to a complete example (that you can use as base for your own project) of an application using Flask to talk to Spotify API  
 * [Python API](https://github.com/mari-linhares/spotify-flask/tree/master/api) that makes very simple to use Spotify API in your Python code
