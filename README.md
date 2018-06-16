# AdaBoost
A implemention of AdaBoost
#### 集成算法

&emsp;对于K近邻，决策树，朴素贝叶斯，Logistic回归，SVM支持向量机。他们各有优缺点，可以将不同的分类器组合起来，而这种组合结果则被称为集成方法或者元算法。

#### 集成方法的形式

1. 不同算法的集成。

2. 同一算法在不同设置下的集成。

3. 数据集不同部分分配给不同的分类器之后的集成。

#### Bagging-------Boosting
自举汇聚法(bootstrap aggregating): 假设数据集的大小为N，从数据集中有放回抽样N个样本，重复S下，就得到了S个新数据集。每个新数据集中可以有重复值，也可能原始数据集的样本没有在新数据中出现。在这里分析一下：

假设有d个样本，每个样本被选中的概率是
 <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{d}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{d}" title="\frac{1}{d}" /></a>   ，未被选中的概率为 <a href="http://www.codecogs.com/eqnedit.php?latex=1-\frac{1}{d}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?1-\frac{1}{d}" title="1-\frac{1}{d}" /></a>  ，
 那么重复采样d次，未被选中的概率为 <a href="http://www.codecogs.com/eqnedit.php?latex=\lim_{d&space;\to\infty&space;}\left&space;(&space;1-\frac{1}{d}&space;\right&space;)^{d}=\frac{1}{e}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\lim_{d&space;\to\infty&space;}\left&space;(&space;1-\frac{1}{d}&space;\right&space;)^{d}=\frac{1}{e}" title="\lim_{d \to\infty }\left ( 1-\frac{1}{d} \right )^{d}=\frac{1}{e}" /></a>
 约等于 36.8%    ，
 被选中的概率为 1-36.8%=63.2%