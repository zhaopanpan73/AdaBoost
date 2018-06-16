from numpy import *
import AdaBoost
datMat,classLabels=AdaBoost.loadSimpData()
# D=mat(ones((5,1))/5)
# print(AdaBoost.buildingStump(datMat,classLabels,D))
classEstArr=AdaBoost.adaBoostTrainDS(datMat,classLabels,10)
print(AdaBoost.adaClassify([[5,5],[0,0]],classEstArr))
