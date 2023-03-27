import PySimpleGUI as sg
from ytmusicapi import YTMusic
import vlc
import pafy
import pyaudio
import time

sg.theme("DarkGreen4")
ytmusic = YTMusic()

layout = [
        [sg.Text("Youtube-Music-MusicMusic-Player")],
        [sg.Text("Enter the Title (maybe with the Artist) here:"), sg.InputText()],
        [sg.Button("Play!"), sg.Button("Pause") ,sg.Button("Stop")],
        [sg.Text(key="-Playing-")]
]

window = sg.Window("Youtube Music-Musicplayer", icon="Icon.ico", element_justification='c').Layout(layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Play!":
        search = ytmusic.search(values[0], "songs", None, 1, False)
        info = search[0]
        Link = "https://youtube.com/watch?v=" + info['videoId']
        Title = info['title']
        Time = info['duration_seconds']
        for item in search:
            for data_item in item['artists']:
                Artist = str(data_item['name'])
                break
            break
        window["-Playing-"].update(f"Playing {Title} by {Artist}")
        video = pafy.new(Link)
        beste = video.getbestaudio()
        spielen = beste.url
        media = vlc.MediaPlayer(spielen)
        media.play()
    elif event == "Pause":
        if media.is_playing() == 1:
            media.set_pause(1);
            window["-Playing-"].update(f"Paused {Title} by {Artist}")
        elif media.is_playing() == 0:
            media.set_pause(0);
            window["-Playing-"].update(f"Playing {Title} by {Artist}")
    elif event == "Stop":
        media.stop()
        window["-Playing-"].update("Playing Nothing")
    elif media.is_playing() == 1:
        pass
    elif media.is_playing() == 0:
        time.sleep(Time + 5)
        media.stop()
        window["-Playing-"].update("Playing Nothing")

window.close()
