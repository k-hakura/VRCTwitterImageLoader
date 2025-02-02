# VRCTwitterImageLoader

X (Twitter)の投稿のうち特定のハッシュタグの投稿を画像としてGitHub Pagesに自動で配信し、日替わりランダムで変更するリポジトリです。

このGitHub Pagesの画像URLは固定のため、例えばVRChatのImage Loaderの仕組みと組み合わせることで、ワールド内でXの投稿を眺めることが可能です。

## 使い方

### GitHub Actionsを用いた完全自動化
1. このプロジェクトをご自身のGitHubプロジェクトとしてForkしてください。
2. `src/VRCTwitterImageLoader/data/urls_orig_date.csv`の要素を空にしてヘッダーだけにし、動作確認のためにURLと日時を10パターン以上記入してください。
3. `src/VRCTwitterImageLoader/x_auto_get_post_urls.py`内の変数`x_hash_tag_str`を任意のハッシュタグに変更してください。
4. X開発者ページにログイン(Freeアカウントでも可)し、BEARER TOKENを発行してください。
5. GitHub ActionsのRepository Secretsに`X_BEARER TOKEN`というKeyで3.で発行したTokenの値を保存してください。
6. 変更をpushすれば完了です。初期設定では、毎週土曜3:00に`urls_orig_date.csv`の中身が更新され、毎日4:00にその中からランダムで10件の投稿が下記のURLに配信されます。
- https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_0.png
- https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_1.png
- https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_2.png
- ...
- https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_9.png
画像URL自体は固定です。画像一覧のサンプル: https://varyuvrc.github.io/VRCTwitterImageLoader/
7. 定時実行を待たずに`.github/workflows`内のCI/CD`スクリプトをGitHub Webページ上で手動実行することも可能です。
8. VRChat UdonのImageLoaderを使用して上記URLから画像を取得することで、ワールド内で動的に更新されるテクスチャとして自由に扱うことができます。画像サイズは 512 x 768 pxです。

### ローカルで動作確認: GitHub Pagesへの画像アップロードは実行されない
このプロジェクトは[uv](https://docs.astral.sh/uv/)で管理されています。事前にインストールしてください。

```shell
$ git clone https://github.com/VarYUvrc/VRCTwitterImageLoader.git
$ cd VRCTwitterImageLoader
$ uv sync

## 0. 日本語フォントのインストール
$ sudo apt-get update
$ sudo apt-get install -y fonts-ipafont

## 1. 画像取得テスト
### 事前にPlaywrgithのchromiumのインストールが必要
$ uv run playwright install chromium
$ uv run python src/VRCTwitterImageLoader/twitter_image.py
### playwrightのエラーが出た場合はエラー文に記載されている必須パッケージを別途インストールする)

## 2. 特定ハッシュタグの投稿URLの自動取得テスト
### 事前にX Developer APIのBEARER TOKENの環境変数への登録が必要
$ export X_BEARER_TOKEN=xxxxxxx
$ uv run python src/VRCTwitterImageLoader/x_auto_get_post_urls.py
```

## Tips
```shell
# formatterを実行
$ uv run ruff format
# linterを実行
$ uv run ruff check --fix
```

## 既知のバグ
画像のレンダリングが失敗した状態で保存されてしまう場合があります。
