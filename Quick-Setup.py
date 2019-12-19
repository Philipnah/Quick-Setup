# We need the requests module to get all the installers from the web.
import requests

# Here we define the urls of the things we need to download
spotify_url = "https://download.scdn.co/SpotifySetup.exe"
spotify_name = "SpotifySetup.exe"

def getInstallers(URL, installer_name):
     r = requests.get(URL, stream = True) 
     
     file_and_location = "installers/" + installer_name

     with open(file_and_location,"wb") as exe: 
          for chunk in r.iter_content(chunk_size=1024): 
          # writing one chunk at a time to pdf file 
               if chunk: 
                    exe.write(chunk)


getInstallers(spotify_url, spotify_name)