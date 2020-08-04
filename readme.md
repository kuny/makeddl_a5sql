# DDL生成スクリプト

A5:SQL Mk-2形式のエンティティ定義書（エクセルファイル）からDDLを生成するPythonスクリプトです。
このスクリプトを実行するとSQL Server用のDDLが出力されれます。
出力されたスクリプトを実行してSQL Serverにテーブルを作成し、A5:SQL Mk-2でER図をリバース生成することでER図を作成することができます。

## 使用方法

### Python3インストール

下記URLよりパッケージをダウンロードしインストールする。
https://www.python.org/downloads/windows/

### Pythonライブラリインストール

```
> pip install openpyxl

> pip install pyyaml
```

### 環境設定

"config.yml"に読み込むエンティティ定義書と出力するファイルのパスを設定する。

### 実行

```
puthon makeddl.py
```

### TODO

[x] プログレスバー
[ ] インデックス
[ ] 型チェック
[ ] リレーションチェック
[ ] プライマリーキーチェック
[ ] 項目名重複チェック
[ ] 同一プライマリーのリレーション
[ ] _x000D_ 置換