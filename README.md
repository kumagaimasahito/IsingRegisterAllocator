# IsingRegisterAllocator
私たちは，量子アニーリングを用いてレジスタアロケーションを行う手法を提案します．
提案手法はライブラリとして実装されており，インストールして誰でも試すことができます．

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
この時，Your tokenにはあなた自身のトークンを記述します．

これをしておくと，以降トークンを入力する必要がなくなり，とても便利です．

#### pytest (optionally)
以下のコマンドで，ライブラリのテストを行うようにしています．必ず必要なものではありませんが，インストール後にテストが通れば，問題なくライブラリが使えるはずです．
```
$ python setup.py test
```

## 使い方
以下に，用意した3つのベンチマークについて，レジスタ割り当ての最適化を行うプログラムを示します．
これらのベンチマークはLLVMでレジスタ情報を抽出して作成したものです．

ご自身でベンチマークを作成されたい方は，以下をご参照ください．
https://github.com/kumagaimasahito/IsingRegisterAllocator/blob/main/benchmarks/ReadMe.md

### 1. レジスタ割り当て最適化
QUBOに定式化されたレジスタアロケーションを行うプログラムの説明はこちら
https://github.com/kumagaimasahito/IsingRegisterAllocator/blob/main/gettingStarted/register_allocation.ipynb

### 2. 大規模彩色問題の分割最適化アルゴリズム
量子アニーリングマシンは，扱える量子ビット数が少ないため，大規模な問題を解けない場合があります．
そのような問題に対して，問題を分割して解を求める手法の説明を行います．
https://github.com/kumagaimasahito/IsingRegisterAllocator/blob/main/gettingStarted/splitted_register_allocation.ipynb
