#!/usr/bin/env python
# encoding:utf-8
import operator
from knn import classify0
from numpy import zeros
from numpy import array
from numpy import shape
from numpy import tile
import matplotlib
import matplotlib.pyplot as plt
def file2matrix(filename):
	fr = open(filename)
	arrayLines = fr.readlines()
	numberLines = len(arrayLines)
	returnMat = zeros((numberLines,3))
	classLabelVector = []
	index = 0
	for line in arrayLines:
		line = line.strip()
		listFormLine = line.split('\t')
		returnMat[index,:] = listFormLine[0:3]
		classLabelVector.append(int(listFormLine[-1]))
		index += 1
	return returnMat,classLabelVector

dataMat,dataLabels = file2matrix('dateset.txt')
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.scatter(dataMat[:,1],dataMat[:,2],15.0 * array(dataLabels),15.0*array(dataLabels))
#ax.scatter(dataMat[:,0],dataMat[:,1],15.0 * array(dataLabels),15.0*array(dataLabels))
#plt.show()



#如下函数提供的是归一化特征值，因为计算两个样本之间的距离时候，飞行距离是主要影响因素，但是在客户看来，三个因素同等重要，所以引入归一化操作
def autoNorm(dataSet):
	minval = dataSet.min(0)
	maxval = dataSet.max(0)
	ranges = maxval - minval
	normdataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minval,(m,1))
	normDataSet = normDataSet/tile(ranges,(m,1))
	print normDataSet
	return normDataSet,ranges,minval

#print autoNorm(dataMat)

def dateClassTest():
	hoRatio = 0.10
	datingDataMat,datingLabels = file2matrix('dateset.txt')
	normMat,ranges,minval = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:],normMat[numTestVecs:m,:],datingLabels[numTestVecs:m],3)
		print "the classifier came back with : %d ,the real answer is : %d" %(classifierResult,datingLabels[i])
		if (classifierResult != datingLabels[i]): errorCount += 1.0
	print "the total error rate is : %f" %(errorCount/float(numTestVecs))

#dateClassTest()
def classPerson():
	resultList = ['not at all','in small doses','in lagre doses']
	percentTats = float(raw_input("percentage of time spent playing videos games?"))
	ffMiles = float(raw_input("frequent filter miles earnen per year?"))
	iceCream = float(raw_input("liters of ice cream consumed per years?"))
	DataMat,DataLabels = file2matrix('dateset.txt')
	normMat,ranges,minVals = autoNorm(DataMat)
	inArr = array([ffMiles,percentTats,iceCream])
	classifierResult = classify0((inArr - minVals)/ranges,normMat,DataLabels,3)
	print "you will probably like this person:"  , resultList[classifierResult - 1]

classPerson()
