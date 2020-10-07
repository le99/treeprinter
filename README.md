# treeprinter

A binary tree printer, inspired by michal.kreuzman's solution in java:
https://stackoverflow.com/questions/4965335/how-to-print-binary-tree-diagram

## Installation
```
python3.7 -m pip install treeprinter-le99
```

## Use
```
from treeprinter import printTree
a = {'key': 1, 'left': None, 'right': {'key': 2, 'left': None, 'right': None}}
print(printTree(a))
```