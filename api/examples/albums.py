from __future__ import print_function
import sys

sys.path.append('../')

import spotify

# lets first search for an album... I really like Currents from Tame Impala, lets search for it

results = spotify.search(['album'], 'Currents')

# results is a nest dictionary
# if you want to see with your eyes...
print(results)

# lets see the results and choose the first result as our correct album
# with enough info probably spotify api will rank what you're looking for
# correcty
print('Search results:')
print('-------------------------------------------------------')
albums = results['albums']['items']
for a in albums:
    print('%s by %s' % (a['name'], a['artists'][0]['name']))
print()
print()

# WE HAVE THE ALBUM :D! And now we can make more awesome things with it
album_id = albums[0]['id']

# I want to know more about this album... let me ask spotify
album_info = spotify.get_album(album_id)
print('Info about Currents by Tame Impala')
print('--------------------------------------------------------')
print('name:', album_info['name'])
print('release date:', album_info['release_date'])
print('populariy:', album_info['popularity'])
print()
print()

print('Tracks')
print('--------------------------------------------------------')
for track in spotify.get_albums_tracks(album_id)['items']:
    print(track['name'])

