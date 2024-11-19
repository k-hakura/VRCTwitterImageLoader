import urllib.request
import json


def get_tweet_embedcode(tweet_url):
    """
    指定されたツイートURLから埋め込みHTMLコードを取得
    """
    try:
        with urllib.request.urlopen(
            f"https://publish.twitter.com/oembed?url={tweet_url}"
        ) as url:
            data = json.loads(url.read().decode())
            return data["html"]
    except Exception as e:
        print(f"Error fetching embed code for {tweet_url}: {e}")
        return ""
