# We need the requests module to get all the installers from the web.
import requests

# Here we define the urls of the things we need to download
spotify_url = "https://download.scdn.co/SpotifySetup.exe"
spotify_name = "SpotifySetup.exe"
discord_url = "https://discordapp.com/api/download?platform=win"
discord_name = "DiscordSetup.exe"
firefox_url = "https://download.mozilla.org/?product=firefox-stub&os=win&lang=en-US"
firefox_name = "Firefox Installer.exe"
vsc_url = "https://aka.ms/win32-x64-user-stable"
vsc_name = "VSCodeUserSetup-x64-1.41.1.exe"

# Now we set all the variables up in an array matching by url the name
Installers = [
     spotify_url,
     spotify_name,
     discord_url,
     discord_name,
     firefox_url,
     firefox_name,
     vsc_url,
     vsc_name

]

def getInstallers(URL, installer_name):
     r = requests.get(URL, stream = True) 
     
     file_and_location = "installers/" + installer_name

     with open(file_and_location,"wb") as exe: 
          for chunk in r.iter_content(chunk_size=1024): 
          # writing one chunk at a time to pdf file 
               if chunk: 
                    exe.write(chunk)


# Amount of installers needed times two
i = 0

while i < len(Installers):
     # Specify url first then the name
     getInstallers(Installers[i], Installers[i + 1])
     i = i + 2