from numpy import *

def loadSimpData():
    datMat = matrix([[ 1. ,  2.1],
        [ 2. ,  1.1],
        [ 1.3,  1. ],
        [ 1. ,  1. ],
        [ 2. ,  1. ]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat,classLabels

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    numFeat = len(open(fileName).readline().split('\t')) #get number of fields
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr =[]
        curLine = line.strip().split('\t')
        for i in range(numFeat-1):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat,labelMat

# 树桩分类器
def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    """
    
    :param dataMatrix:   输入数据集
    :param dimen:   所要划分数据集的哪一个维度
    :param threshVal:   划分的阈值
    :param threshIneq:   划分的方式: 树桩左右的类别设定
    :return: 
    """
    retArray=ones((shape(dataMatrix)[0],1))
    if threshIneq=='lt':
        retArray[dataMatrix[:,dimen]<=threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen]>threshVal]= -1.0
    return retArray


# 遍历dimen,threshVal,threshIneq所有可能的输入值，找到数据集上的最佳单层决策树
def buildingStump(dataArr,labels,D):
    dataMatrix=mat(dataArr)
    labels=mat(labels).T
    nSamples,nAttr=shape(dataMatrix)

    numSteps=10.0  # 在特征所有可能值上遍历的次数
    bestStump={}  # 依次存储最佳单层决策树的相关信息
    bestClassEst=mat(zeros((nSamples,1)))  # 当前决策树所产生的分类结果

    minError=inf

    # 遍历大法来也
    for i in range(nAttr):
        rangeMin=dataMatrix[:,i].min()
        rangeMax=dataMatrix[:,i].max()
        stepSize=(rangeMax-rangeMin)/numSteps  # 在当前特征可能值上遍历的步长
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt','gt']:
                threshVal=(rangeMin+float(j)*stepSize)
                predictionVals=stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr=mat(ones((nSamples,1)))
                errArr[predictionVals==labels]=0
                weightedError=D.T*errArr
                print("split: dim %d ,thresh %.2f ,thresh inequal : %s ,the weight error is %.3f" % (i,threshVal,inequal,weightedError))
                if weightedError<minError:
                    minError=weightedError
                    bestClassEst=predictionVals.copy()
                    bestStump['dim']=i
                    bestStump['thresh']=threshVal
                    bestStump['ineq']=inequal
    return bestStump,minError,bestClassEst  # 最佳分类器的划分结果-1,1组成的

def adaBoostTrainDS(dataArr,labels,numIt=40):
    weakClassArr=[] # 用来存储分类器
    nSamples=shape(dataArr)[0]
    D=mat(ones((nSamples,1))/nSamples)  # 训练样本初始化权重
    dynamicClassEst=mat(zeros((nSamples,1)))  # 分类器动态分类结果 ,初始化的值不重要
    for i in range(numIt):
        bestStump,error,classEst=buildingStump(dataArr,labels,D)
        print("D: ",D.T)
        # 计算分类器权值
        alpha=float(0.5*log((1.0-error)/max(error,1e-6)))
        bestStump['alpha']=alpha
        weakClassArr.append(bestStump)
        # 更新权值
        expon=multiply(-alpha*mat(labels).T,classEst)  # 对应元素相乘
        D=multiply(D,exp(expon))
        D=D/D.sum()
        dynamicClassEst+=alpha*classEst
        print("dynamicClassEst : " ,dynamicClassEst.T)
        dynamicError=multiply(sign(dynamicClassEst)!=mat(labels).T,ones((nSamples,1)))
        errRate=dynamicError.sum()/nSamples
        print("total error:" ,errRate)
        # 循环退出的条件
        if errRate==0:
            break
    return  weakClassArr


# 用AdaBoost进行分类
def adaClassify(dataToClass,classifierArr):
    """
    :param dataToClass:  进行分类的样本
    :param classifierArr:  训练好的基学习器
    :return:  分类结果
    """
    dataMatrix=mat(dataToClass)
    nSamples=shape(dataMatrix)[0]
    dynamicClassEst=mat(ones((nSamples,1)))
    for i in range(len(classifierArr)):
        classEst=stumpClassify(dataMatrix,classifierArr[i]['dim'],classifierArr[i]['thresh'],classifierArr[i]['ineq'])
        dynamicClassEst+=classifierArr[i]['alpha']*classEst
        print("classEst:",dynamicClassEst)
    return  sign(dynamicClassEst)