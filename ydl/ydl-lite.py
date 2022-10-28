import subprocess
import os


"""
	YouTube Downloader used to download the best quality 
	audio, 
	video,
	Playlist of audio files,
	Playlist of video files
	from a URL belonging to https://www.youtube.com/
	
	Started working on : 21-06-2017
	Done by : Jaivarsan B
	email : jaiimmortal@gmail.com


	Project was done as a hobby, with no intention to violate any copyrights.
	
"""


def video_link():
    return input('Enter a valid URL from YouTube ')


def playlist_link():
    return input('Enter a valid entire playlist link from YouTube ')


def quality_input():
    quality = ['240', '360', '480', '720']
    print("\nPlease select quality")
    userInput = int(input(
        '\n\t[1] 240p \n\t[2] 360p \n\t[3] 480p \n\t[4] 720p \n\t[5] Default (best available quality)\n'))
    if userInput == 5:
        return ""
    else:
        return '-f "bestvideo[height<={q}]+bestaudio/best[height<={q}]"'.format(q=quality[userInput-1])


def main():

    try:

        choice = int(input(
            'Enter \n\t[1] Video \n\t[2] Playlist of video files \n\t[3] Audio \n\t[4] Playlist of audio files\n'))

        if choice == 1:
            url = video_link()
            subprocess.call('youtube-dl  -o "Video downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --no-warnings {quality} "{url}"'.format(
                quality=quality_input(), url=url), shell=True)
            print('\n\nThe process is over and your file is probably residing in ' +
                  os.getcwd() + '/Video downloads from youtube-dl')

        elif choice == 2:
            url = playlist_link()
            subprocess.call('youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --newline --no-warnings {quality} "{url}"'.format(
                quality=quality_input(), url=url), shell=True)
            print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')

        elif choice == 3:
            url = video_link()
            subprocess.call(
                'youtube-dl -f 251 -o "Audio downloads from youtube-dl/%(title)s.%(ext)s" -q --no-playlist --extract-audio --audio-format mp3 --xattrs --embed-thumbnail --audio-quality 0 --no-warnings "{url}"'.format(url=url), shell=True)
            print('\n\nThe process is over and your file is probably residing in ' +
                  os.getcwd() + '/Audio downloads from youtube-dl')

        elif choice == 4:
            url = playlist_link()
            subprocess.call(
                'youtube-dl -i -o "%(playlist)s/%(playlist_index)s.%(title)s.%(ext)s" --yes-playlist --extract-audio --audio-format mp3 --xattrs --embed-thumbnail --audio-quality 0 --no-warnings "{url}"'.format(url=url), shell=True)
            print('\n\nThe process is over and currently residing in the current working directgory with the name of the folder same as that of playlist!')

    except Exception as e:
        print(e)


if __name__ == "__main__":

    main()
