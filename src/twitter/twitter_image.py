import csv
import platform
import chromedriver_binary_sync
from scripts.dataloader import count_csv_rows, random_line_numbers
from scripts.image_url import convert_to_publish_urls
from scripts.render import capture_tweet_images


# ツイートURLをランダムで抽出
file_path = "src/twitter/data/urls_orig_date.csv"
row_count = count_csv_rows(file_path)
image_num = 10 # 画像取得数
max_attempts = 100  # 最大試行回数
attempts = 0

# ユニークなURLの種類の数が規定数になるまで繰り返す
unique_urls = set()
while len(unique_urls) < image_num and attempts < max_attempts:
    attempts += 1
    selected_lines = random_line_numbers(row_count, image_num)
    selected_urls = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for line_number, row in enumerate(reader):
            if line_number in selected_lines and len(row) > 0:
                selected_urls.append(row[0])
                unique_urls.add(row[0])

render_urls = convert_to_publish_urls(selected_urls)

# OSに基づいてChromedriverのパスを設定
chromedriver_binary_sync.download(download_dir="./src/twitter/chromedriver/")

if platform.system() == "Windows":
    chromedriver_path = "./src/twitter/chromedriver/chromedriver.exe"
else:
    chromedriver_path = "./src/twitter/chromedriver/chromedriver"


# レンダリング
capture_tweet_images(render_urls, chromedriver_path)
