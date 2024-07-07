
# Spotify Playlist Song Downloader

This Python script downloads songs from your Spotify playlist using Selenium for web automation and the PyTube library for downloading YouTube videos. It interacts with the Spotify API to retrieve playlist tracks and uses YouTube to find and download the corresponding songs.

![Screen Shot 2024-07-06 at 17 31 17](https://github.com/Moe131/playlist-downloader/assets/65834335/848cd35a-f9c1-440a-89b8-22d085ab7385)


## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Google Chrome
- ChromeDriver (compatible with your version of Google Chrome)
- Required Python libraries: `selenium`, `pytube3`, `python-dotenv`, `requests`

You can install the required Python libraries using pip:

```bash
pip install selenium pytube3 python-dotenv requests
```

## Setup

1. **Spotify Developer Account**: Create a Spotify Developer account and register an application to get your `CLIENT_ID` and `CLIENT_SECRET`.

2. **Environment Variables**: Create a `.env` file in the root directory of your project and add your Spotify API credentials:

    ```
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    ```

3. **ChromeDriver**: Download the ChromeDriver executable and place it in your project directory or ensure it's in your system PATH. Update the `executable_path` in the script if necessary.

## Usage

1. Clone or download the repository to your local machine.

2. Place the `.env` file in the root directory of the project.

3. Open a terminal and navigate to the project directory.

4. Run the script:

    ```
    python main.py
    ```

## Script Explanation

### Imports

- `selenium` for web automation.
- `pytube` for downloading YouTube videos.
- `dotenv` for loading environment variables.
- `requests`, `os`, `time`, `base64`, `json` for various tasks such as API requests and data handling.


### Example Usage in Script

Replace the placeholder playlist ID in the `main` function with your own Spotify playlist ID:

```
python main.py
```

Run the script, and it will download the songs to the specified `SAVE_PATH` directory.

### Note

Ensure that ChromeDriver is compatible with your installed version of Google Chrome. You can download the appropriate version from the [ChromeDriver download page](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Disclaimer

This script is intended for personal use only. Ensure you have the right to download and use the content you access. Respect copyright laws and the terms of service of the platforms you interact with.
