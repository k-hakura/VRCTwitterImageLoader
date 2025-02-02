# src/VRCTwitterImageLoader/scripts/html_render.py
import os
import urllib.request
import json
from playwright.sync_api import sync_playwright


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


def is_tweet_rendered(page):
    """
    ツイートのレンダリング状況を、ツイートコンテナ（<blockquote class="twitter-tweet">）の高さで判定する。
    例として高さが50px以上ならレンダリング成功と判断する。
    """
    try:
        # 少し待ってからツイートコンテナの高さを評価
        return page.evaluate("""() => {
            const container = document.querySelector('.twitter-tweet');
            if (!container) return false;
            return container.getBoundingClientRect().height > 50;
        }""")
    except Exception as e:
        print("Error evaluating tweet container:", e)
        return False


def save_html_as_png(
    converted_urls, file_name="src/VRCTwitterImageLoader/temp/tweet.html"
):
    """
    ツイート埋め込みHTMLをレンダリングしてPNG形式で保存
    ※もともとの待機タイミングを基本とし、レンダリング完了しているかを
      ツイートコンテナの高さで判定し、不具合の場合は再試行する。
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        for index, render_url in enumerate(converted_urls):
            html_content = get_tweet_embedcode(render_url)
            if not html_content:
                print(f"ツイートの埋め込みコード取得に失敗しました: {render_url}")
                continue

            # HTMLファイルに書き出し
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

            # ローカルHTMLファイルのパスを生成
            local_url = "file://" + os.path.abspath(file_name)

            # レンダリング完了の再試行（最大3回）
            max_attempts = 3
            attempt = 0
            rendered = False

            while attempt < max_attempts and not rendered:
                print(f"[{render_url}] Attempt {attempt+1} / {max_attempts}")
                page.goto(local_url, wait_until="networkidle")

                # もともとのコードと同様に、JavaScript実行待機
                page.wait_for_timeout(3000)  # 初回待機（3秒）
                page.set_viewport_size({"width": 512, "height": 768})
                page.wait_for_timeout(10000)  # レンダリング完了待機（10秒）

                if is_tweet_rendered(page):
                    rendered = True
                    print("レンダリングが正常に完了しました。")
                else:
                    attempt += 1
                    print(f"レンダリング未完了。再試行 {attempt}/{max_attempts} ...")
                    page.reload(wait_until="networkidle")
                    page.wait_for_timeout(3000)

            if not rendered:
                print(
                    f"最大試行回数({max_attempts})に達しましたが、レンダリングが完了しませんでした: {render_url}"
                )

            # スクリーンショットの保存
            screenshot_path = (
                f"src/VRCTwitterImageLoader/pages/images/screenshot_{index}.png"
            )
            page.screenshot(path=screenshot_path, full_page=True)
            print(f"Screenshot saved to {screenshot_path}")

        browser.close()
