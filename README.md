# Breadth First Search (BFS)

このリポジトリは **幅優先探索（Breadth First Search, BFS）** を
Pythonで実装したサンプルです。

BFSはグラフ探索アルゴリズムの一つで、
スタート地点から近いノードを順番に探索していきます。

---

## アルゴリズムの特徴

・キュー（Queue）を使用して探索する
・最短経路を見つけることができる
・計算量は **O(V + E)**

---

## このプログラムについて

このノートブックでは、
迷路（Maze）を例にして BFS を使った探索を行っています。

```text
S = スタート
G = ゴール
0 = 通路
1 = 壁
```

BFSを使用して **スタートからゴールまでの最短距離** を求めます。

---

## 使用技術

* Python
* NumPy
* collections.deque

---

## 実行方法

```bash
pip install numpy
```

その後

```
BFS.ipynb
```

をJupyter Notebookで実行してください。

---

## 参考

Breadth First Search は
グラフ探索アルゴリズムの基本であり、

・迷路探索
・最短経路問題
・AI探索アルゴリズム

などに利用されます。
