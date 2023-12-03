import csv
import platform
import chromedriver_binary_sync
from scripts.dataloader import count_csv_rows, random_line_numbers
from scripts.image_url import convert_to_publish_urls
from scripts.render import capture_tweet_images


# ツイートURLをランダムで抽出
file_path = "src/twitter/data/urls_orig.csv"
row_count = count_csv_rows(file_path)
selected_lines = random_line_numbers(row_count, 3)

selected_urls = []
with open(file_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for line_number, row in enumerate(reader):
        if line_number in selected_lines:
            selected_urls.append(row[0])

render_urls = convert_to_publish_urls(selected_urls)

# OSに基づいてChromedriverのパスを設定
chromedriver_binary_sync.download(download_dir='./src/twitter/chromedriver/')

if platform.system() == 'Windows':
    chromedriver_path = "./src/twitter/chromedriver/chromedriver.exe"
else:
    chromedriver_path = "./src/twitter/chromedriver/chromedriver"


# レンダリング
capture_tweet_images(render_urls, chromedriver_path)
