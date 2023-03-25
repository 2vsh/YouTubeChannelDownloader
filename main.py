import os
import httplib2
import google_auth_httplib2
from google.oauth2 import service_account
from googleapiclient.discovery import build
from pytube import YouTube
from tqdm import tqdm
import time

def get_channel_videos(channel_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    all_videos = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token,
            type="video",
            fields="nextPageToken,items(id(videoId),snippet(publishedAt,channelId,title,description))"
        )
        response = request.execute()
        all_videos += response["items"]
        
        next_page_token = response.get("nextPageToken")

        if next_page_token is None:
            break

    return all_videos

def download_video(video_id, output_path):
    try:
        yt = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()

        # Progress bar and MB/s counter
        def progress_hook(stream, chunk, bytes_remaining):
            current_time = time.time()
            current_mb = (stream.filesize - bytes_remaining) / (1024 * 1024)
            elapsed_time = current_time - start_time
            speed = current_mb / elapsed_time
            progress_bar.update(len(chunk))
            progress_bar.set_description(f"Speed: {speed:.2f} MB/s")

        start_time = time.time()
        with tqdm(total=stream.filesize, unit='B', unit_scale=True, ncols=100, desc="Downloading", ascii=True) as progress_bar:
            yt.register_on_progress_callback(progress_hook)
            stream.download(output_path)

        print(f"Downloaded {video_id}")
    except Exception as e:
        print(f"Error downloading {video_id}: {e}")

def main():
    # Replace with your YouTube API key
    api_key = "API_KEY_HERE"
    
    # Replace with the desired YouTube channel ID
    channel_id = "UCXuqSBlHAE6Xw-yeJA0Tunw" # To find this, you can use this website: https://commentpicker.com/youtube-channel-id.php#youtube-channel-id

    output_path = "downloads"

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    videos = get_channel_videos(channel_id, api_key)

    for video in videos:
        video_id = video["id"]["videoId"]
        download_video(video_id, output_path)

if __name__ == "__main__":
    main()
