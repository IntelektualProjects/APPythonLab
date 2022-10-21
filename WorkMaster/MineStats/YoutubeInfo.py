from googlesearch import search
import os
from MineStats.config import api_key
import googleapiclient.discovery


class YoutubeInfo:

    def __init__(self):
        self.id = ""

    def youtube_data_retrieval(self, query):
        query = query.replace(' ', '+')
        link = [i for i in search(query, tld="co.in", num=1, stop=1, pause=2)]
        self.id = str(link[0]).replace("https://www.youtube.com/channel/", "")

        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        youtube = googleapiclient.discovery.build(
            "youtube", "v3", developerKey=api_key)

        request = youtube.channels().list(
            part="statistics",
            id=self.id
        )
        response = request.execute()["items"][0]["statistics"]
        return list(zip(response.keys(), response.values()))

