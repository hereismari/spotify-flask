# YDL
## YouTube Downloader (Synchronous)

A Python script to download Audio, Video and  Playlist of audio and video files just by providing the URL and get them at the best quality.

### For Asynchrnous go [here](https://github.com/greed2411/YDL/tree/ydl-async)

Tested and developed on ***Windows 7 32-bit SP1***, ***Ubuntu GNOME 16.04 LTS***, ***Ubuntu 16.10*** and ***macOS Sierra 10.12.5***

### Command Line Programs Used
  * `youtube-dl` - Used to download the file from the internet
  * `ffmpeg` - Used for postprocess data, i.e., to convert file from .webm to .mp3 format

For Light weight script without error handling, run `ydl-lite.py`, you can skip the unnecessary library installations that way. But, you can't do monkey error testing with it.

### Libraries used on Py 3.6.1 Anaconda, works with other py3 versions and distributions for `ydl.py` and `ydl-windows.py`.
  * [subprocess](https://docs.python.org/3/library/subprocess.html#older-high-level-api) - For running commands from python.
  * [os](https://docs.python.org/3/library/os.html) - to get the current working directory.
  * [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) - For making GET methods
  * [urllib.error](https://docs.python.org/3/library/urllib.error.html#module-urllib.error) - For considering URLError
  * [sys](https://docs.python.org/3/library/sys.html) - For exiting out of the script
  * [bs4](http://beautiful-soup-4.readthedocs.io/en/latest/) - For scraping content while the user is connected to the internet or not, in case of wifi-connected , but not logged in
  * [lxml](http://lxml.de/#download) - For parsing the HTML document
  
  If you don't have either of the last two packages install them using,
  
  ```pip installation
  pip install bs4
  ```
  
  and 
  
  ```pip installation
  pip install lxml
  ```
  ***If you don't have pip3 or pip go or dunno which one to use go [here](https://stackoverflow.com/a/6587528)***
  
### Steps to follow for installing dependencies
  * On Windows 
     1. Install `youtube-dl` via cmd
        
        ```youtube-dl installation
        pip install youtube-dl
        ```
     2. Install `ffmpeg` from [here](http://ffmpeg.zeranoe.com/builds/) and the [instructions](http://www.wikihow.com/Install-FFmpeg-on-Windows)
     
     3. And important thing : Move the contents of ffmpeg/bin/ to the location where `youtube-dl.py` is present as described in the [issue](https://stackoverflow.com/a/42745019)
     
     4. Run the script `ydl-windows.py` via cmd
     
   * On Ubunutu or similar Distros
      1. Install `youtube-dl` via terminal
      
         ```youtube-dl installation
         pip install youtube-dl
         ```
      2. Install `ffmpeg`
      
         ```ffmpeg installation
         sudo apt-get install ffmpeg
         ```
      3. Run the scrpipt `ydl.py` in the terminal or the lightweight version `ydl-lite.py`.
    
    * On macOS
      1. Install `youtube-dl` via terminal
         
            ```youtube-dl installation
         brew install youtube-dl
         ```
      2. Install `ffmpeg`
      
         ```ffmpeg installation
         brew install ffmpeg
         ```
      3. Run the scrpipt `ydl.py` in the terminal or the lightweight version `ydl-lite.py`.
      
       ### Possible errors: 
      
         It sometimes asks you to install 'pyattr' or the 'xattr' module, even GNU's 'attr' module by throwing an error

         Simple solution : 

         ```
         pip install xattr
         ```
      
### References
  * [wikiHow to Install FFmpeg on Windows](http://www.wikihow.com/Install-FFmpeg-on-Windows) - Helped me.
  * [Installing FFmpeg on all kind of environments](https://github.com/adaptlearning/adapt_authoring/wiki/Installing-FFmpeg)
  * [extract audio with youtube-dl on windows](https://stackoverflow.com/a/42745019) - Hack for the [issue](https://github.com/NixOS/nixpkgs/issues/5236) 
  * [YouTube download using youtube-dl embedded with Python - 2017](http://www.bogotobogo.com/VideoStreaming/YouTube/youtube-dl-embedding.php) pretty useful summary of important stuff mentioned from [youtube-dl's documentation](https://github.com/rg3/youtube-dl)
  * [Improper documentation for Python](https://github.com/rg3/youtube-dl/blob/master/youtube_dl/YoutubeDL.py) - You are all alone on the sea to understand the code and try if you want to use the package 'youtube_dl' , gave up trying to use the classes.
  * for format conversion and extracting audio followed [this](http://www.slashgeek.net/2016/06/24/5-youtube-dl-tips-might-not-know/)
  
### Screenshots

![Youtube link of playlist for audio downloads URL](/../screenshots/4.png?raw=true "Ubuntu")

![Youtube link of playlist for audio downloads done](/../screenshots/3.png?raw=true "macOS")

### Facts you may love

1. Your downloads resume, if your laptop falls asleep or enters sleep mode, assuming the terminal is still left open.
2. In case of network error or out of storage, if you establish the connection back or clear someother storage for the sake of playlist, restart the script with the same link at the same location. It resumes downloading from the place where it left, instead of downloading the entire playlist again from the beginning. 
3. If you are concerned about the data usage like every other Indian (incl myself), don't worry quality control is present for video and video playlist downloads.

### Contributor(s)

Thanks [@MINOSai](https://github.com/MINOSai) for quality control.
