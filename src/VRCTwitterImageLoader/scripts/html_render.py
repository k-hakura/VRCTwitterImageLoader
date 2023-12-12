import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
from io import BytesIO
from scripts.image_url import get_tweet_embedcode


def save_html_as_png(
    converted_urls, chromedriver_path, file_name="src/twitter/temp/tweet.html"
):
    for index, render_url in enumerate(converted_urls):
        html_content = get_tweet_embedcode(render_url)

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(html_content)

        # WebDriverのServiceオブジェクトを作成
        service = Service(chromedriver_path)

        # WebDriver設定（ヘッドレスモードでブラウザを起動）
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(service=service, options=options)

        # Open the local HTML file
        local_url = "file://" + os.path.abspath(file_name)
        driver.get(local_url)

        # ウィンドウサイズ設定
        driver.set_window_size(400, 1600)

        # Give some time for the tweet to load completely
        time.sleep(20)

        # スクリーンショットをPNG形式のバイナリデータとして取得
        screenshot_png = driver.get_screenshot_as_png()

        # バイナリデータからPIL.Imageオブジェクトを生成
        img = Image.open(BytesIO(screenshot_png))

        # 画像のサイズ取得
        width, height = img.size

        # 下のピクセルをカット
        left = 0
        top = 0
        right = width
        bottom = height - 800
        cropped_img = img.crop((left, top, right, bottom))

        # 加工後の画像を保存
        cropped_img.save(f"src/twitter/pages/images/cropped_screenshot_{index}.png")

        # Close the browser
        driver.quit()

    return
