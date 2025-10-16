import os
import vlc

def play_song(player):
    player.play()
    state = player.get_state()
    if state in (vlc.State.Ended, vlc.State.Stopped, vlc.State.Error):
        return False
    else:
        return True

def pause_song(player):
    player.pause()

def stop_playback(player):
    player.stop()

def list_folder(folder):
    index = 1
    song_list = os.listdir(folder)
    for i in song_list:
        print(f"{index}: {i}")
        index += 1
    return song_list

def load_playlist(playlist_file):
    playlist = []
    with open(f"{playlist_file}", "r") as file:
        for line in file:
            song_line = line.split(":")
            playlist.append(song_line[1].strip())
    return playlist

def make_playlist(song_string, playlist_name, song_folder):
    playlist = {}
    split_list = song_string.split(",")
    for item in split_list:
        playlist[item.strip()] = song_folder[int(item) - 1]
    os.makedirs("playlists", exist_ok=True)
    with open(f"playlists/{playlist_name}.txt", "w") as file:
        for item in playlist:
            print(f"{item}: {playlist[item]}", file=file)


def main():
    os.makedirs("songs", exist_ok=True)
    os.makedirs("playlists", exist_ok=True)
    playing = False
    player = None
    while True:

        if playing == True:
            print(f"Currently playing {song}")
            print("1. Pause/play song")
            print("2. Skip/next song")
            print("3. Stop Playback")
            select = input("Choose an option: ")

            if select == "1":
                pause_song(player)
            elif select == "2":
                try:
                    stop_playback(player)
                    song_index += 1
                    song = loaded_playlist[song_index]
                    print(song)
                    player = vlc.MediaPlayer(f"songs/{song}")
                    player.play()
                except IndexError as index:
                    print("End of Playlist")
                    break
            elif select == "3":
                stop_playback(player)
                playing = False

        elif playing == False:


            print("Welcome to the mp3 player!")
            print("1. Load playlist")
            print("2. Make playlist")
            print("3. Quit")
            player_mode = input("Choose an option: ")

            if player_mode == "1":
                print("Playlists: ")
                directory = list_folder("playlists")
                try:
                    current_playlist = directory[int(input("Select a playlist to load: ")) - 1]
                    loaded_playlist = load_playlist(f"playlists/{current_playlist}")
                    song_index = 0
                    song = loaded_playlist[0]
                    song_path = f"songs/{song}"
                    player = vlc.MediaPlayer(song_path)
                    playing = play_song(player)
                except ValueError as value:
                    print("Please enter a valid number")
                except IndexError as index:
                    print("The number you entered has no matching playlist")
                except:
                    print("An error occured")


            elif player_mode == "2":
                os.system("clear")
                song_folder = list_folder("songs")
                song_string = input("Choose what songs to include in your playlist: (e.g. 1, 2, 3) ")
                try:
                    playlist_name = input("Playlist name: ")
                    make_playlist(song_string, playlist_name, song_folder)
                except ValueError as value:
                    print("Error: Please enter a valid song selection")
                except IndexError as index:
                    print("Error: One or more of the song numbers entered has no matching song")
                except:
                    print("An error occured")
                

            elif player_mode == "3":
                break

            else:
                os.system("clear")
                print("Please enter a valid option (1-3)")

if __name__ == "__main__":
    main()