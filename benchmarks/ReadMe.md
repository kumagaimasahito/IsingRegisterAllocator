ベンチマークを作成するには，submoduleにあるLLVMをビルドし，生成されたClangでコンパイルします

`./llvm-project/build/bin/clang++ -O2 -mllvm -regalloc=basic file.cpp`

関数ごとの干渉グラフと仮想レジスタ毎に割り当て可能な物理レジスタ名が出力されます
