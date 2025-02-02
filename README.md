# VRCTwitterImageLoader

X (Twitter)の投稿のうち、特定のハッシュタグの投稿をリストにまとめ、そのリストから日替わりランダムで任意の数の投稿を選び、GitHub Pagesに画像として自動で配信するプログラムです。

このGitHub Pagesの画像URLは固定のため、例えばVRChatのImage Loadingの仕組みと組み合わせることで、ワールド内でXの投稿を眺めることが可能です。

**すべての動作はGitHub上で完結しているため、サーバを個人で建てる必要がありません。**

Xの投稿をリストに収集する頻度と収集数は、Xの開発者アカウントのグレードに依存します。2025年2月現在、無料プランは100回/月に制限されています。

使用例：https://x.com/Ring_Say_rip/status/1731264158828753358
- ワールド制作の知識が必要です。Image Loadingについて: [Image Loading | VRChat](https://creators.vrchat.com/worlds/udon/image-loading/)

ランダムではなく新着順に投稿を選ぶことも可能です。
- [twitter_image.py](src/VRCTwitterImageLoader/twitter_image.py)の中身をコメントアウトすることで[ランダム/新着]を選択

## 使い方

### GitHub Actionsを用いた完全自動化
1. このプロジェクトをご自身のGitHubプロジェクトとしてForkしてください。
1. URLリストである[urls_orig_date.csv](src/VRCTwitterImageLoader/data/urls_orig_date.csv)を自身の収集対象のXの投稿のURLに変更してください。動作するためには少なくとも10件の投稿が必要です。
1. [x_auto_get_post_urls.py](src/VRCTwitterImageLoader/x_auto_get_post_urls.py)内の変数`x_hash_tag_str`を収集対象のハッシュタグに変更してください。
1. [X開発者ページ](https://developer.twitter.com/en/portal/dashboard)にログイン(Freeアカウントでも可)し、BEARER TOKENを発行してください。
1. GitHub ActionsのRepository Secretsに`X_BEARER_TOKEN`というKeyで、4.で発行したTokenの値を保存してください。
1. 下記の操作で、リポジトリのGitHub ActionsにPull Requestの権限を付与してください。
    - 「Settings」→「Actions」→「General」に移動
    - 「Workflow permissions」セクションで以下を設定:
    - Read and write permissionsを選択
    - Allow GitHub Actions to create and approve pull requestsにチェック
1. 変更をpushすれば完了です。初期設定では、毎週土曜3:00に`urls_orig_date.csv`の中身が更新され、毎日4:00にその中からランダムで10件の投稿が下記のURLに配信されます。
    - https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_0.png
    - https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_1.png
    - https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_2.png
    - ...
    - https://{アカウント名}.github.io/VRCTwitterImageLoader/images/screenshot_9.png
        - 画像はスクリプト実行ごとに上書き変更されますが、画像URLは常に固定です。画像一覧のサンプル: https://varyuvrc.github.io/VRCTwitterImageLoader/
        - 画像数を変更したい場合は、[twitter_image.py](src/VRCTwitterImageLoader/twitter_image.py)の`image_num`の値と、[index.html](src/VRCTwitterImageLoader/pages/index.html)の中身を変更してください。
1. 定時実行を待たずに`.github/workflows`内のCI/CD`スクリプトをGitHub Webページ上で手動実行することも可能です。
1. VRChat UdonのImageLoaderを使用して上記URLから画像を取得することで、ワールド内で動的に更新されるテクスチャとして自由に扱うことができます。画像サイズは 512 x 768 pxです。
1. 「`urls_orig_date.csv`の中身の更新」は勝手には行われず、masterブランチへのPull Requestで通知されます。内容に問題がなければMergeしてください。

### ローカルで動作確認（GitHub Pagesへの画像アップロードは実行されません）
このプロジェクトはパッケージマネージャ[uv](https://docs.astral.sh/uv/)で管理されています。事前にインストールしてください。

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
画像のレンダリングが失敗した状態で保存されてしまう場合があります。現在は失敗時に3回まで再トライするようになっています。

## その他
不具合報告などの手順は[CONTRIBUTING](CONTRIBUTING.md)をご確認ください。
