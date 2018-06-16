# AdaBoost
A implemention of AdaBoost
#### 集成算法

&emsp;对于K近邻，决策树，朴素贝叶斯，Logistic回归，SVM支持向量机。他们各有优缺点，可以将不同的分类器组合起来，而这种组合结果则被称为集成方法或者元算法。

#### 集成方法的形式

1. 不同算法的集成。

2. 同一算法在不同设置下的集成。

3. 数据集不同部分分配给不同的分类器之后的集成。

#### Bagging-------Boosting

**自举汇聚法(bootstrap aggregating)** : 假设数据集的大小为N，从数据集中有放回抽样N个样本，重复S下，就得到了S个新数据集。每个新数据集中可以有重复值，也可能原始数据集的样本没有在新数据中出现。在S个数据集构建好之后，将某个学习算法分别作用于每个数据集就得到了S个分类器。最终分类器的投票结果由这些子分类器的投票决定。

在这里分析一下：

假设有d个样本，每个样本被选中的概率是 <a href="http://www.codecogs.com/eqnedit.php?latex=\frac{1}{d}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{1}{d}" title="\frac{1}{d}" /></a>

 未被选中的概率为
 <a href="http://www.codecogs.com/eqnedit.php?latex=1-\frac{1}{d}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?1-\frac{1}{d}" title="1-\frac{1}{d}" /></a>  ，

 那么重复采样d次，未被选中的概率为

 <a href="http://www.codecogs.com/eqnedit.php?latex=\lim_{d&space;\to\infty&space;}\left&space;(&space;1-\frac{1}{d}&space;\right&space;)^{d}=\frac{1}{e}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\lim_{d&space;\to\infty&space;}\left&space;(&space;1-\frac{1}{d}&space;\right&space;)^{d}=\frac{1}{e}" title="\lim_{d \to\infty }\left ( 1-\frac{1}{d} \right )^{d}=\frac{1}{e}" /></a>约等于 36.8% ，被选中的概率为 1-36.8%=63.2%

**boosting**  :是使用同一种分类器，运用某种策略，依次串行训练得到不同的分类器，每个新分类器根据已经训练出来的分类器的性能基础上来进行训练。boosting是通过集中关注被已有分类器错分的那些数据来训练新的数据集。 boosting分类的结果是基于所有分类器的加权求和结果。

#### bagging和boosting的区别：

bagging算法的基本分类器的训练集是由原始训练集N，有放回抽取n'<=N个样本，每个基分类器是相互独立的，并列的，因为每个分类器的训练方法是独立的且相同的，所以最后分类器是所有子分类器等权重投票。
boosting算法的不同分类器数据集是同一个训练集，只是在串行训练过程中，分类器 **数据集** 每个样本点的权重是不断变化的，因为分错的样本在接下来的训练中会被关注更多。每个分类器的权重也是不同的。最后的分类器是所有及分类器加权投票的结果。
