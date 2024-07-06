from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

SAVE_PATH = "songs"

def main():
    songname = "Far Away (feat. A$AP Rocky)"
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

    # Quit
    driver.quit()

if __name__ == "__main__":
    main()