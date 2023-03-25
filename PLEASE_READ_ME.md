# YouTube Video Downloader
### This is a simple Python script to download all videos from a specified YouTube channel using the YouTube API v3 and the PyTube library.

### Features
Downloads all videos from a specified YouTube channel
Shows a progress bar and download speed (MB/s) during the download process
Downloads the highest resolution MP4 video available

### Requirements
Python 3.x

A YouTube API key (you can obtain one from the Google Developer Console)

The following Python libraries:

google-auth
google-auth-httplib2
google-api-python-client
pytube
tqdm

### To install the required libraries, run the following command in the directory you have main.py in:
pip install google-auth google-auth-httplib2 google-api-python-client pytube tqdm

### Usage
Replace the API_KEY_HERE placeholder with your YouTube API key:
api_key = "API_KEY_HERE"

Replace the channel_id variable with the desired YouTube channel ID. You can find the channel ID easily using a website like https://commentpicker.com/youtube-channel-id.php#youtube-channel-id. 
channel_id = "UCXuqSBlHAE6Xw-yeJA0Tunw" (This is LTT's Channel)

Optionally, change the output_path variable to specify a different download directory:
output_path = "downloads"

## Run the script:
python main.py (Or double click the main.py program) 

The script will download all videos from the specified channel and save them in the downloads directory (or the specified directory) as MP4 files.
