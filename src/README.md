## Interacting with the API 

[Full list of Spotify endpoints](https://developer.spotify.com/web-api/endpoint-reference/)

~ spotify.py ~ is a simple Python API that allows you to use Spotify API without worring about HTTP Requests, and other little things.  
It works perfectly for requests that doesn't need Oath, I'm still working on a simpler way to make this work better for Oath as well.  

If you don't want to use Oauth just make oath = False in the first line of the code.  

## Examples

Supposing that you are in the same folder of the spotify.py file:

~~~py
import spotify
results = spotify.search('artist', 'Lady Gaga')
~~~

`results` is a [this nest dictionary](https://api.spotify.com/v1/search?q=lady%20gaga&type=artist).

~~~py
# to get the artists it self
artists = results['artists']['items']
for a in artists: print a['name'], a['followers']['total']
~~~

