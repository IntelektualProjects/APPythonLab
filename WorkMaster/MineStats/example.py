# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
from MineStats.config import api_key
import os
import googleapiclient.discovery


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=api_key)

    request = youtube.channels().list(
        part="statistics",
        id="UC24-XPATP4CeviFJ8SLiF8A"
    )


if __name__ == "__main__":
    main()
