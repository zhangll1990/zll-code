
#encoding:utf-8
from numpy import *
def loadDataSet():
	dataMat = []; labelMat = []
	fr = open('testSet.txt')
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0,float(lineArr[0]),float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat,labelMat


def sigmoid(inX):
	return 1.0/(1 + exp(-inX))


def gradAscent(dataMatIn,classLabels):
	dataMatrix = mat(dataMatIn)
	labelMat = mat(classLabels).transpose()
	m,n = shape(dataMatrix)
	alpha = 0.001
	mayCycles = 500
	weights = ones((n,1))
	for k in range(mayCycles):
		h = sigmoid(dataMatrix * weights)
		error = (labelMat - h)
		weights = weights + alpha * dataMatrix.transpose() * error
	return weights

def plotBestFit(wei):
	import matplotlib.pyplot as plt
	weights = wei.getA()
	dataMat,labelMat = loadDataSet()
	dataArr = array(dataMat)
	n = shape(dataArr)[0]
	xcord1 = []; ycord1 = []
	xcord2 = []; ycord2 = []
	for i in range(n):
		if int(labelMat[i]) == 1:
			xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
		else:
			xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
	fig = plt.figure()
	ax = fig.add_supplot(111)
	ax.scatter(xcord1,ycord1,s = 30,c = 'red',marker = 's')
	ax.scatter(xcord2,ycord2,s = 30,c = 'green')
	x = arange(-3.0,3.0,0.1)
	y = (-weights[0] - weights[1]*x)/weights[2]  # 为什么 y 轴 是这样, 因为 0 是这两类函数的分类，
	#而需要分的类是 2 类。所以正确的分开以后，应该是存在 0 = w*x0 + w1 * x1 + w2 * x2的，又 x0 = 1
	ax.plot(x,y)
	plt.xlabel('X1');plt.ylabel('X2');
	plt.show()
	

def stocGradAscent(dataMatrix,classLabels,numIter = 150):
	m,n = shape(dataMatrix)
	weights = ones(n)
	for j in range(numIter):
		dataIndex = range(m)
		for i in range(m):
			alpha = 4 / (1.0 + j + i) + 0.01
			randIndex = int(random.uniform(0,len(dataIndex)))
			#h = sigmoid(sum(dataMatrix[randIndex] * weights))
			h = sigmoid(dataMatrix[randIndex] * weights)
			error = classLabels[randIndex] - h
			weights = weights + alpha * error * dataMatrix[randIndex]
			del(dataIndex[randIndex])
	return weights

def classifyVector(inX,weights):
	prob = sigmoid(sum(inX * weights))
	if prob > 0.5 :
		return 1
	else:
		return 0

def colicTest():
	frTrain = open('houseTraining.txt')
	frTest = open('houseTest.txt')
	trainingSet = []; trainingLabels = []
	for line in frTrain.readlines():
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		trainingSet.append(lineArr)
		trainingLabels.append(float(currLine[21]))
	trainWeights = stocGradAscent(array(trainingSet),trainingLabels,500)
	errorCount = 0 ; numTestVec = 0.0
	for line in frTest.readlines():
		numTestVec += 1.0
		currLine = line.strip().split('\t')
		lineArr = []
		for i in range(21):
			lineArr.append(float(currLine[i]))
		if int(classifyVector(array(lineArr),trainWeights)) != int(currLine[21]):
			errorCount += 1
	errorRate = (float(errorCount)/numTestVec)
	print 'the error rate of theis test is %f' %errorRate
	return errorRate


def multTest():
	numTests = 10; errorSum = 0.0
	for k in range(numTests):
		errorSum += colicTest()
	print "after %d iterations the average error rate is %f" %(numTests,errorSum/float(numTests))



dataArr,labelMat = loadDataSet()
#weights = gradAscent(dataArr,labelMat)

print multTest()

#print stocGradAscent(array(dataArr),labelMat)

#print weights
#print weights.getA()     # getA() 函数 和 不加 getA 是有区别的，区别是，一个是矩阵，一个是 array，
#两者 主要区别是 numpy里面arrays遵从逐个元素的运算 不会当成矩阵去乘， matrix 是矩阵的乘。

