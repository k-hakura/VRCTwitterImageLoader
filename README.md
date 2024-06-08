# VRCTwitterImageLoader

# How to Use

VRChatのImageLoaderを使用して、下記URLから画像を取得します。
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/cropped_screenshot_0.png
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/cropped_screenshot_1.png
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/cropped_screenshot_2.png
- ...
- https://varyuvrc.github.io/VRCTwitterImageLoader/images/cropped_screenshot_9.png

GitHub ActionsによってGitHub Pagesが一日一回更新されます。それにより画像がランダムに変更されます。画像URL自体は固定です。
https://varyuvrc.github.io/VRCTwitterImageLoader/

# Installation

このプロジェクトは[Rye](https://rye-up.com/)で管理されています。

```shell
$ git clone https://github.com/VarYUvrc/VRCTwitterImageLoader.git
$ cd VRCTwitterImageLoader
$ rye sync

# local実行テスト
$ rye run python src/VRCTwitterImageLoader/twitter_image.py
```

```shell
# formatterを実行
$ rye fmt
# linterを実行
$ rye lint
# linterを実行して自動的に修正
$ rye lint --fix
```