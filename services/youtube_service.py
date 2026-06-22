from googleapiclient.discovery import build
from config import Config


class YouTubeService:

    def __init__(self):

        self.youtube = build(
            "youtube",
            "v3",
            developerKey=Config.YOUTUBE_API_KEY
        )

    def search(self, query, max_results=5):

        request = self.youtube.search().list(

            q=query,

            part="snippet",

            maxResults=max_results,

            type="video"

        )

        response = request.execute()

        videos = []

        for item in response["items"]:

            videos.append({

                "title": item["snippet"]["title"],

                "channel": item["snippet"]["channelTitle"],

                "thumbnail": item["snippet"]["thumbnails"]["high"]["url"],

                "video_id": item["id"]["videoId"],

                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"

            })

        return videos
