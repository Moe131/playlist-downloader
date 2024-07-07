
# Spotify Playlist Song Downloader

This application allows you to download songs from a Spotify playlist by searching and downloading them from YouTube. It uses the Spotify API to fetch the playlist details and Selenium for navigating YouTube to download the songs using `pytube`.

![Screen Shot 2024-07-07 at 01 07 30](https://github.com/Moe131/playlist-downloader/assets/65834335/3631cd60-918f-47e1-a9a6-243c483b1163)


## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your version of Google Chrome)
- Required Python libraries: `selenium`, `pytube3`, `python-dotenv`, `requests` 


## Installation

1. Clone the repository:

    ```
    git clone https://github.com/moe131/playlist-downloader.git
    cd playlist-downloader
    ```

2. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

3. Set up your Spotify API credentials:
   
    - Create a `.env` file in the root directory of your project.
    - Add your Spotify API credentials to the `.env` file:

      ```
      CLIENT_ID=your_spotify_client_id
      CLIENT_SECRET=your_spotify_client_secret
      ```

4. Download and set up ChromeDriver:
   
    - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    - Place the ChromeDriver executable in the project directory or set its path in the code.


## Usage

1. Run the application:

    ```
    python downloader.py
    ```

2. In the GUI:
    - Enter the URL of the Spotify playlist you want to download.
    - Click "Browse" to select the directory where you want to save the downloaded songs.
    - Click "Start Download" to begin downloading songs.


### Note

Ensure that ChromeDriver is compatible with your installed version of Google Chrome. You can download the appropriate version from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Disclaimer

This script is intended for personal use only. Ensure you have the right to download and use the content you access. Respect copyright laws and the terms of service of the platforms you interact with.
