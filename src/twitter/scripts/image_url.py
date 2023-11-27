import urllib.parse

def convert_to_publish_urls(urls):
    converted_urls = []
    base_url = "https://publish.twitter.com/?"
    for url in urls:
        params = {'query': url, 'widget': 'Tweet'}
        converted_urls.append(base_url + urllib.parse.urlencode(params))
    return converted_urls
