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
telegram_url = "https://telegram.org/dl/desktop/win"
telegram_name = "tsetup.1.8.15.exe"
tor_url = "https://www.torproject.org/dist/torbrowser/9.0.2/torbrowser-install-win64-9.0.2_en-US.exe"
tor_name = "torbrowser-install-win64-9.0.2_en-US.exe"
nordVPN_url = "https://downloads.nordcdn.com/apps/windows/10/NordVPN/latest/NordVPNSetup.exe"
nordVPN_name = "NordVPNSetup.exe"
arduino_url = "https://www.arduino.cc/download_handler.php"
arduino_name = "arduino-1.8.10-windows.exe"
bitdefender_url = "https://download.bitdefender.com/windows/bp/agent/en-us/bitdefender_online.exe"
bitdefender_name = "bitdefender_online.exe"
flux_url = "https://justgetflux.com/dlwin.html"
flux_name = "flux-setup.exe"
evernote_url = "https://cdn1.evernote.com/win6/public/Evernote_6.22.3.8816.exe"
evernote_name = "Evernote_6.22.3.8816.exe"

# Now we set all the variables up in an array matching by url the name
Installers = [
     spotify_url,
     spotify_name,
     discord_url,
     discord_name,
     firefox_url,
     firefox_name,
     vsc_url,
     vsc_name,
     telegram_url,
     telegram_name,
     tor_url,
     tor_name,
     nordVPN_url,
     nordVPN_name,
     arduino_url,
     arduino_name,
     bitdefender_url,
     bitdefender_name,
     flux_url,
     flux_name,
     evernote_url,
     evernote_name
]

def getInstallers(URL, installer_name):
     r = requests.get(URL, stream = True) 
     
     file_and_location = "installers/" + installer_name

     with open(file_and_location, "wb") as exe: 
          for chunk in r.iter_content(chunk_size=1024): 
          # writing one chunk at a time to pdf file 
               if chunk: 
                    exe.write(chunk)


i = 0
while i < len(Installers):
     # Specify url first then the name
     getInstallers(Installers[i], Installers[i + 1])
     i = i + 2