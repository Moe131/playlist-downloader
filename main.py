from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

def main():
    songname = "Far Away (feat. A$AP Rocky)"
    # Open Youtube search for a song
    driver.get("https://www.youtube.com/results?search_query="+ songname.replace(" ","+"))

    # Find the song and click on it
    WebDriverWait(driver, 20).until(
       EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,songname))
    )
    link = driver.find_element(By.PARTIAL_LINK_TEXT,songname)
    link.click()
    time.sleep(10)

    # Quit
    driver.quit()

if __name__ == "__main__":
    main()