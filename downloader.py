from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
from dotenv import load_dotenv
import os , time , requests , base64 , json
from tkinter import *
from tkinter import filedialog  , ttk



load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

SAVE_PATH = "songs"

def get_token():
    """ Gets Spotfiy access token by making POST request"""
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"
    header = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = { "grant_type" : "client_credentials" }
    result = requests.post(url, headers=header, data=data)
    json_result = json.loads(result.content)
    return json_result["access_token"]

def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}

def get_playlist(playlist_id):
    """ Gets the song names in a playlist """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    token = get_token()
    header = get_auth_header(token)
    result = requests.get(url, headers=header)
    json_result = json.loads(result.content)
    return json_result["tracks"]["items"]

def download_song(driver ,songname):
    """ Uses selenium to search a song in Youtube and
      downloads it in the SAVE_PATH"""
    # Open Youtube search for a song
    driver.get("https://www.youtube.com/results?search_query="+ songname.replace(" ","+"))
    # Find the song URL
    WebDriverWait(driver, 20).until(
       EC.presence_of_element_located((By.ID,"video-title"))
    )
    link = driver.find_element(By.ID,"video-title")
    url = link.get_attribute("href")
    # Download the song
    try: 
        YouTube(url).streams.first().download(output_path=SAVE_PATH)
        print(f'{songname} downloaded successfully!')
    except Exception as e: 
        print(f"Error downloading {songname}: {e}")
    
    progress_var.set(progress_var.get() + 1)
    progress_bar.update()
    progress_label.config(text=f"Downloaded {progress_var.get()} of {total_songs} songs")

def get_directory():
    global SAVE_PATH
    SAVE_PATH = filedialog.askdirectory()
    path_label.config(text=SAVE_PATH)

def download_playlist():
    global total_songs
    # My playlist url :https://open.spotify.com/playlist/2bE0EkxJLOXAMw916ejsOH?si=kCqn5zLbSKaYvZyN-hGIgQ&pi=u-cAfKHu1lRQCr&nd=1&dlsi=48a7505b25ec48f1
    playlist_id = playlist_input.get().split("/")[-1]
    playlist = get_playlist(playlist_id)
    songs = []
    for song in playlist:
        songs.append((song["track"]["name"]+ " " + song["track"]["artists"][0]["name"]) )
    
    total_songs = len(songs)
    progress_var.set(0)
    progress_bar["maximum"] = total_songs
    progress_label.config(text=f"Downloaded 0 of {total_songs} songs")

    # Set up Chromedriver to download pages from Youtube
    options = webdriver.ChromeOptions()
    options.add_argument("headless") # used to hide browser openning on screen
    service = Service(executable_path="./chromedriver")
    driver = webdriver.Chrome(service=service , options=options)
    for song in songs :
        download_song(driver,song)
    # Quit driver
    driver.quit()

def main():
    """ Runs the main script"""
    global path_label, playlist_input, progress_bar, progress_var, progress_label

    window = Tk()
    window.title("Playlist Downloader")
    window.geometry("600x350")
    window.resizable(False, False)  # Disable window resizing

    frm = Frame(window, relief=RIDGE, borderwidth=2, padx=20, pady=20)
    frm.pack(expand=True)

    # Playlist URL input
    input_frame = Frame(frm)
    input_frame.pack(pady=10)
    Label(input_frame, text="Download your Spotify playlists ", font=("Helvetica", 14)).pack(padx=10,pady=10)
    Label(input_frame, text="Playlist URL:", font=("Helvetica", 14)).pack(side=LEFT, padx=10)
    playlist_input = Entry(input_frame,font=("Helvetica", 12), width=45)
    playlist_input.pack(side=LEFT, padx=10)

    # Browse button and path label
    browse_frame = Frame(frm)
    browse_frame.pack(pady=10)
    Label(browse_frame, text="Save folder:", font=("Helvetica", 14)).pack(side=LEFT, padx=10)
    path_label = Label(browse_frame, text="",width=33, font=("Helvetica", 12))
    path_label.pack(side=LEFT,pady= 10, padx=10)
    Button(browse_frame, text="Browse", command=get_directory, font=("Helvetica", 12)).pack(side=LEFT, padx=10)

    # Start Download button
    Button(frm, text="Start Download", command=download_playlist, font=("Helvetica", 12)).pack(pady=10)

    # Progress bar and label
    progress_var = IntVar()
    progress_bar = ttk.Progressbar(frm, orient=HORIZONTAL, length=400, mode='determinate', variable=progress_var)
    progress_bar.pack(pady=20)
    
    progress_label = Label(frm, text="", font=("Helvetica", 12))
    progress_label.pack(pady=10)

    window.mainloop()



if __name__ == "__main__":
    main()