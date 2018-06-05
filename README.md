# spotify-flask

Spotify-Flask is a very straightforward way to request data from Spotify API using flask with templates. You can also just use the [Python API](http://github.com/mari-linhares/spotify-flask/api/) to make requests for your application.

I've created this repository because I couldn't find a full implementation of a Flask app using Spotify API, altough
https://github.com/datademofun/spotify-flask and https://github.com/drshrey/spotify-flask-auth-example have some nice work!

![Image](https://github.com/mari-linhares/spotify-flask/blob/master/imgs/profile.png?raw=true)

## Run it

1. Follow [this tutorial](https://developer.spotify.com/web-api/tutorial/) to create your own Spotify App. Then add "http://127.0.0.1:8081/callback/" as a redirect URI.  

2. Create a file named **conf.json** in this folder with the exact same structure of the conf_example.json file.  

3. Run python app.py to see an application using the code present here :bowtie:.

## What facilities this application offers?

 * Support to a complete example (that you can use as base for your own project) of an application using Flask to talk to the Spotify API.  
 * [Python API](https://github.com/mari-linhares/spotify-flask/tree/master/api) that makes very simple to use Spotify API in your Python code.
