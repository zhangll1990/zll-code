#!/usr/bin/env python
#encoding:utf-8
from numpy import *
import operator
def createDataset():
    group  = array([[1,1.1],[1,1],[0,0],[0,1]])
    labels = ['A','A','B','B']
    return group ,labels

group,labels = createDataset()
def classify0(inX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sorteDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
            voteIlabel = labels[sorteDistIndicies[i]]
            classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]

print classify0([0.8,0.9],group,labels,3)

print "k 近邻算法 和 k 决策树算法"
