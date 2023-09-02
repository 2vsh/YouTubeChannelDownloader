import os
import time
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs
from pytube import YouTube
from tqdm import tqdm
from googleapiclient.discovery import build


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


def get_channel_name(channel_id, api_key):
    youtube = build("youtube", "v3", developerKey=api_key)
    request = youtube.channels().list(
        part="snippet",
        id=channel_id
    )
    response = request.execute()
    channel_name = response["items"][0]["snippet"]["title"]
    return channel_name


def main():
    api_key = "API_KEY_HERE"  # Replace this with your actual API key
    base_output_path = "downloads"

    if not os.path.exists(base_output_path):
        os.makedirs(base_output_path)

    url = input("Please enter the YouTube URL: ")
    parsed_url = urlparse(url)

    if re.search(r"youtube\.com/channel/", url):
        channel_id = os.path.basename(parsed_url.path)
        channel_name = get_channel_name(channel_id, api_key)
        output_path = os.path.join(base_output_path, channel_name)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        videos = get_channel_videos(channel_id, api_key)

        with ThreadPoolExecutor(max_workers=4) as executor:
            for video in videos:
                video_id = video["id"]["videoId"]
                executor.submit(download_video, video_id, output_path)
    elif re.search(r"youtube\.com/watch", url):
        query_string = parse_qs(parsed_url.query)
        video_id = query_string["v"][0]
        download_video(video_id, base_output_path)
    else:
        print("Invalid URL. Please enter a valid YouTube channel or video URL.")


if __name__ == "__main__":
    main()
