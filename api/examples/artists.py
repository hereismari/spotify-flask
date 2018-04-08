from __future__ import print_function
import sys

sys.path.append('../')

import spotify

# lets first search for an artist... I really like Michael Jackson, lets search for it

results = spotify.search(['artist'], 'Michael Jackson')

# results is a nest dictionary
# if you want to see with your eyes...
print(results)

# lets see the results and choose the first result as our correct artist
# with enough info probably spotify api will rank what you're looking for
# correcty
print('Search results:')
print('-------------------------------------------------------')
artists = results['artists']['items']
for a in artists: print('%s, popularity: %s' % (a['name'], a['popularity']))
print()
print()

# WE HAVE THE ARTIST :D! And now we can make more awesome things with it
artist_id = artists[0]['id']

# I want to know more about this artist... let me ask spotify
artist_info = spotify.get_artist(artist_id)
print('Info about Michael Jackson:')
print('--------------------------------------------------------')
print('name:', artist_info['name'])
print('populariy:', artist_info['popularity'])
print('num. followers:', artist_info['followers']['total'])
print()
print()

print('Albums')
print('--------------------------------------------------------')
for album in spotify.get_artists_albums(artist_id)['items']:
    print(album['name'])
print()
print()

print('Top Tracks')
print('--------------------------------------------------------')
for track in spotify.get_artists_top_tracks(artist_id)['tracks']:
    print(track['name'])
print()
print()

print('Related Artists')
print('--------------------------------------------------------')
for ra in spotify.get_related_artists(artist_id)['artists']:
    print(ra['name'])



