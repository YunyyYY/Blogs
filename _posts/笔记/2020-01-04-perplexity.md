---
layout: review
permalink: /:categories/:title/
category: Notes
tag: 笔记
---

## Perplexity 困惑度

> Reference: [CSDN Perplexity(困惑度)](https://blog.csdn.net/jiaqiang_ruan/article/details/77989459)



### 概率分布的困惑度

离散概率分布的困惑度定义为：
$$
2^{H(p)}, \hspace.5cm H(p) = -\sum_{x} p(x) \log _{2} p(x)
$$
$H(p)$是概率分布$p$的熵，$x$是样本点。因此一个随机变量$X$的困惑度是定义在$X$的概率分布上的（$X$所有可能取值）。

困惑度是信息熵的指数。



### 概率模型的困惑度

用一个概率模型$q$去估计真实概率分布$p$，可以通过**测试集**中的样本来定义这个概率模型的困惑度。
$$
b^{-\frac{1}{N}\sum_{i=1}^{N} \log _{b} q\left(x_{i}\right)} 
$$
其中测试样本$x_1$, $x_2$, …, $x_N$是来自于真实概率分布$p$的观测值，$b$通常取2。因此，低的困惑度表示$q$对$p$拟合的越好，当模型$q$看到测试样本时，它会不会感到那么“困惑”。