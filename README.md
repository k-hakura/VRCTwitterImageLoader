# VRCTwitterImageLoader

# How to Use

VRChatのImageLoaderを使用して、下記URLから画像を取得します。
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/screenshot_0.png
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/screenshot_1.png
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/screenshot_2.png
- ...
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/screenshot_9.png

GitHub ActionsによってGitHub Pagesが一日一回更新されます。それにより画像がランダムに変更されます。画像URL自体は固定です。
https://varyuvrc.github.io/VRCTwitterImageLoader/

画像サイズ: 512 x 768 px

# Installation

このプロジェクトは[uv](https://docs.astral.sh/uv/)で管理されています。

```shell
$ git clone https://github.com/VarYUvrc/VRCTwitterImageLoader.git
$ cd VRCTwitterImageLoader
$ uv sync

# local実行テスト
# 事前にPlaywrgithのchromiumのインストールが必要
$ uv run playwright install chromium
$ uv run python src/VRCTwitterImageLoader/twitter_image.py
```

```shell
# formatterを実行
$ uv run ruff format
# linterを実行
$ uv run ruff check --fix
```