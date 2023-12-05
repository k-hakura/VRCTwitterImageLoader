import urllib.request
import json


def get_tweet_embedcode(tweet_url):
    try:
        with urllib.request.urlopen(
            f"https://publish.twitter.com/oembed?url={tweet_url}"
        ) as url:
            data = json.loads(url.read().decode())
            return data["html"]
    except BaseException:
        return ""
