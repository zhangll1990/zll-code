#coding:utf-8
import operator
from math import log
import matplotlib.pyplot as plt
import treePlotter


def splitDataSet(dataSet,axis,value):
	retDataSet = []
	for feat in dataSet:
		if feat[axis] == value:
			reducefeat = feat[:axis]
			reducefeat.extend(feat[axis+1:])
			retDataSet.append(reducefeat)
	return retDataSet


def calcShannonEnt(dataSet):
    numEntries = len(dataSet)    #计算数据集中的实例总数
    labelCounts = {}  #创建数据字典，其键值是最后一列的数值
    for featVec in dataSet: #the the number of unique elements and their occurance。  
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys(): labelCounts[currentLabel] = 0    #如果当前键值不存在，则扩展字典并将当前键值加入字典，
        labelCounts[currentLabel] += 1                                              #每一个键值都记录了当前类别的次数
    #使用所有类标签发生的频率计算类别出现的概率，计算香农熵
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2) #log base 2
    return shannonEnt	



def chooseBestFeatureToSplit(dataSet):  #选择最好的数据集划分方式
    numFeature = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    beatFeature = -1
    for i in range(numFeature):
        featureList = [example[i] for example in dataSet] #获取第i个特征所有的可能取值
        uniqueVals = set(featureList)  #从列表中创建集合，得到不重复的所有可能取值
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)  #以i为数据集特征，value为返回值，划分数据集
            prob = len(subDataSet)/float(len(dataSet))   #数据集特征为i的所占的比例
            newEntropy += prob * calcShannonEnt(subDataSet)   #计算每种数据集的信息熵
        infoGain = baseEntropy - newEntropy
        #计算最好的信息增益，增益越大说明所占决策权越大
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.key():
			classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),key = opertor.itemgetter(1),reverse = True)
	return  sortedClassCount


def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet) == 1:
		return majorityCnt(classList)
	beatFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[beatFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[beatFeat])
	featValues = [example[beatFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet,beatFeat,value),subLabels)
	return myTree
	
#下面函数为绘制图形部分
decisionNode = dict(boxstyle = 'sawtooth',fc = '0.8')
leafNode = dict(boxstyle = 'round4',fc = '0.8')
arrow_args = dict(arrowstyle = '<-')

def plotNode(nodeTxt,centerPt,parentPt,nodeType):
	createPlot.ax1.annotate(nodeTxt,xy = parentPt,xycoords = 'axes fraction',xytext = centerPt,textcoords = 'axes fraction',va = "center",ha = 'center',bbox = nodeType,arrowprops = arrow_args)

def createPlot():
	fig = plt.figure(1,facecolor = 'red')
	fig.clf()
	createPlot.ax1 = plt.subplot(111,frameon=False)
	plotNode('a descison node',(0.5,0.1),(0.1,0.5),decisionNode)
	plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
	plt.show()


def classify(inputTree,featLabels,testVec):
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr)
	for key in secondDict.keys():
		if testVec[featIndex] == key:
			if type(secondDict[key]).__name__ == 'dict':
				classLabel = classify(secondDict[key],featLabels,testVec)
			else:
				classLabel = secondDict[key]
	return classLabel


#下面为输出测试部分
myDat = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]

labels = ['no surfacing','flippers']

print splitDataSet(myDat,0,1)

print "________________________________________________________"

print splitDataSet(myDat,0,0)

print "________________________________________________________"

print chooseBestFeatureToSplit(myDat)

print "________________________________________________________"

#tree = createTree(myDat,labels)
tree = treePlotter.retrieveTree(0)

createPlot()

print classify(tree,labels,[0,1])

print "________________________________________________________"

print classify(tree,labels,[1,1])

print "________________________________________________________"

print classify(tree,labels,[1,0])
