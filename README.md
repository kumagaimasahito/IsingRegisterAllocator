# IsingRegisterAllocator

## インストール
### 1. git clone
```
$ git clone git@github.com:kumagaimasahito/IsingRegisterAllocator.git
$ cd IsingRegisterAllocator
$ pip install .
```

### 2. Amplify トークンの設定
クローンしたレポジトリの中に，.env.sampleというファイルがあります．
これを参考に，.envというファイルを作成し，AMPLIFY_TOKEN="Your token"と書いて保存してください．
これをしておくと，以降トークンを入力する必要がなくなり，とても便利です．

#### pytest (optionally)
以下のコマンドで，ライブラリのテストを行うようにしています．必ず必要なものではありません．
```
$ python setup.py test
```
