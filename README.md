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
この時，Your tokenにはあなた自身のトークンを記述します．取り扱いにはご注意ください．

これをしておくと，以降トークンを入力する必要がなくなり，とても便利です．

#### pytest (optionally)
以下のコマンドで，ライブラリのテストを行うようにしています．必ず必要なものではありません．
```
$ python setup.py test
```

## 使い方
### 1. レジスタ割り当て最適化
https://github.com/kumagaimasahito/IsingRegisterAllocator/blob/main/gettingStarted/register_allocation.ipynb

### 2. 大規模彩色問題の分割最適化アルゴリズム
