# VRCTwitterImageLoader

現在作成中。

このプロジェクトは[Rye](https://rye-up.com/)で管理されています。

```shell
$ git clone https://github.com/VarYUvrc/VRCTwitterImageLoader.git
$ cd VRCTwitterImageLoader
$ rye sync

# local実行テスト
$ rye run python src/VRCTwitterImageLoader/twitter_image.py
```

コード整形にはRUffを採用しています。
```shell
# formatter を実行
$ rye run ruff format .
# linter を実行
$ rye run ruff check . --fix
```