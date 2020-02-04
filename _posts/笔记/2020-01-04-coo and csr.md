---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

## `coo_matrix` and `csr_matrix`

> Reference: [稀疏矩阵存储格式总结](https://www.cnblogs.com/xbinworld/p/4273506.html)

### Coordinate（COO）

每一个元素需要用一个三元组来表示，分别是（行号，列号，数值），对应上图右边的一列。这种方式简单，但是记录单信息多（行列），每个三元组自己可以定位，因此空间不是最优。

<img src='https://images0.cnblogs.com/blog/354318/201502/042300488598079.png' width=400/>





### Compressed Sparse Row (CSR)

CSR是比较标准的一种，也需要三类数据来表达：数值，列号，以及行偏移。CSR不是三元组，而是整体的编码方式。数值和列号与COO一致，表示一个元素以及其列号，行偏移表示**某一行的第一个元素在values里面的起始偏移位置**。如上图中，第一行第一个元素1是在values中index是0，第二行元素2在values中index为2，第三行元素5偏移为4，第4行元素6偏移为7。在行偏移的最后补上矩阵总的元素个数，本例中是9。

<img src='https://images0.cnblogs.com/blog/354318/201502/042300502345067.png' width=400px/>

