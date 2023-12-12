from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
import time


def capture_tweet_images(converted_urls, chromedriver_path):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    for index, render_url in enumerate(converted_urls):
        with webdriver.Chrome(
            service=Service(chromedriver_path), options=options
        ) as driver:
            driver.get(render_url)

            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )

            # ウィンドウサイズ設定
            driver.set_window_size(400, 1600)

            # ページの読み込みを待つ（5秒）
            time.sleep(10)

            # スクロールする高さを設定
            scroll_height = 800
            driver.execute_script(f"window.scrollTo(0, {scroll_height});")

            # スクリーンショットをPNG形式のバイナリデータとして取得
            screenshot_png = driver.get_screenshot_as_png()

            # バイナリデータからPIL.Imageオブジェクトを生成
            img = Image.open(BytesIO(screenshot_png))

            # 画像のサイズ取得
            width, height = img.size

            # 左右ピクセルをカット
            left = 20
            top = 1030
            right = width - 35
            bottom = height
            cropped_img = img.crop((left, top, right, bottom))

            # 加工後の画像を保存
            cropped_img.save(f"src/twitter/pages/images/cropped_screenshot_{index}.png")
