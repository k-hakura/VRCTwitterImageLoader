import os
from playwright.sync_api import sync_playwright
from scripts.image_url import get_tweet_embedcode


def save_html_as_png(
    converted_urls, file_name="src/VRCTwitterImageLoader/temp/tweet.html"
):
    """
    ツイート埋め込みHTMLをレンダリングしてPNG形式で保存
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for index, render_url in enumerate(converted_urls):
            html_content = get_tweet_embedcode(render_url)

            if not html_content:
                continue

            # HTMLファイルに保存
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(f"""
                <html>
                <head>
                    <script async src="https://platform.twitter.com/widgets.js"></script>
                </head>
                <body>
                    {html_content}
                </body>
                </html>
                """)

            # ローカルHTMLファイルを読み込む
            local_url = "file://" + os.path.abspath(file_name)
            page.goto(local_url, wait_until="networkidle")

            # JavaScriptが完全に実行されるまで待機
            page.wait_for_timeout(3000)  # 3秒待機

            # ページサイズを動的に調整
            page.set_viewport_size({"width": 512, "height": 768})

            # JavaScriptが完全に実行されるまで待機
            page.wait_for_timeout(10000)  # 10秒待機

            # スクリーンショットを保存
            screenshot_path = (
                f"src/VRCTwitterImageLoader/pages/images/screenshot_{index}.png"
            )
            page.screenshot(path=screenshot_path, full_page=True)

            print(f"Screenshot saved to {screenshot_path}")

        # ブラウザを閉じる
        browser.close()
