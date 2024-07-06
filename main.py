from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
from dotenv import load_dotenv
import os , time , requests , base64 , json

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

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

def download_song(songname):
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
    except: 
        print("Error downloading the video")

def main():
    """ Runs the main script"""
    playlist = get_playlist("2bE0EkxJLOXAMw916ejsOH?si=kCqn5zLbSKaYvZyN-hGIgQ&pi=u-cAfKHu1lRQCr&nd=1&dlsi=48a7505b25ec48f1")
    songs = []
    for song in playlist:
        songs.append((song["track"]["name"]+ " " + song["track"]["artists"][0]["name"]) )
    print(len(songs))
    for song in songs :
        download_song(song)

    # Quit driver
    driver.quit()


if __name__ == "__main__":
    main()