ベンチマークを作成するには，submoduleにあるLLVMをビルドし，生成されたClangでコンパイルします．
干渉グラフの出力はregallocbasicを改変して出力させているため，アロケータを指定する必要があります．

`./llvm-project/build/bin/clang++ -O2 -mllvm -regalloc=basic file.cpp`

関数ごとの干渉グラフと仮想レジスタ毎に割り当て可能な物理レジスタ名が出力されます
干渉グラフ: interference_(mangle).out
割り当て可能な物理レジスタ: allocatablereg_(mangle).out
