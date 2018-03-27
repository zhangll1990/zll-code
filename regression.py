#!/usr/bin/env python
from numpy import *
import matplotlib.pyplot as plt
def loadDataSet(filename):
	numFeat = len(open(filename).readline().split('\t')) - 1
	dataMat = []; labelMat = []
	fr = open(filename)
	for line in fr.readlines():
		lineArr = []
		curlLine = line.strip().split('\t')
		for i in range(numFeat):
			lineArr.append(float(curlLine[i]))
		dataMat.append(lineArr)
		labelMat.append(float(curlLine[-1]))
	return dataMat,labelMat

def standRegres(xArr,yArr):
	xMat = mat(xArr);yMat = mat(yArr).T
	xTx = xMat.T*xMat
	if linalg.det(xTx) == 0.0:
		print 'this matrix is singular,cannot do inverse'
		return 
	ws = xTx.I * (xMat.T*yMat)
	return ws

def lwlr(testPoint,xArr,yArr,k=1.0):
	xMat = mat(xArr);yMat = mat(yArr).T
	m = shape(xMat)[0]
	weights = mat(eye((m)))
	for j in range(m):
		diffMat = testPoint - xMat[j,:]
		weights[j,j] = exp(diffMat*diffMat.T/(-2.0*k**2))
	xTx = xMat.T * (weights * xMat)
	if linalg.det(xTx) == 0.0:
		print 'this matrix is cannot be inverse'
		return 
	ws = xTx.I * (xMat.T * (weights * yMat))
	return testPoint * ws

def lwlrTest(testArr,xArr,yArr,k =1.0):
	m = shape(testArr)[0]
	yHat = zeros(m)
	for i in range(m):
		yHat[i] = lwlr(testArr[i],xArr,yArr,k)
	return yHat

xArr,yArr = loadDataSet('ex0.txt')
ws = standRegres(xArr,yArr)
print ws

yMat = mat(yArr)
xMat = mat(xArr)
yHat = xMat*ws

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xMat[:,1].flatten().A[0],yMat.T[:,0].flatten().A[0])
xCopy = xMat.copy()
xCopy.sort(0)
yHat = xCopy*ws
ax.plot(xCopy[:,1],yHat)
plt.show()

yHat = xMat*ws
print corrcoef(yHat.T,yMat)

print lwlr(xArr[0],xArr,yArr,1.0)
print lwlr(xArr[0],xArr,yArr,0.002)
print lwlrTest(xArr,xArr,yArr,0.003)


#srtInd = xMat[:,1].argsort(0)
#xSort = xMat[srtInd][:,0,:]
#
#fig = plt.figure()
#ax = fig.add_subplot(111)
#ax.plot(xSort[:,1],yHat[srtInd])
#
#ax.scatter(xMat[:,1].flatten().A[0],mat(yArr).T.flatten().A[0],s=2,c='red')
#plt.show()
