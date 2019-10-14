import sys
import numpy as np

#Starting of Algorithm 1
#Single Sample Perceptron with margin=10 and Relaxation Algorithm
def ftrain1(dat,lab,wid):
	wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	while(count<1000):
		cou=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			its=np.dot(arr,arr)
			if(warr<=wid):
				wei+=((wid-warr)*arr)/its
		count+=1
	return wei

def ftest1(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		dat[i,0]=1
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 2
		else:
			print 4

def fper1(train,test):
	wid=10
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	si=tr_data.shape[1]-1
	for i in xrange(tr_data.shape[0]):
		tr_data[i,0]=1
		if tr_data[i,si]==2:
			tr_data[i,0:si]*=-1
	wei=ftrain1(tr_data[:,0:si],tr_data[:,si],wid)
	ftest1(wei,tes_data,wid)

#Starting of Algorithm 2
#Modified Perceptron Algorithm
def ftrain2(dat,lab,wid):
	wei=np.zeros(dat.shape[1])
	minw=wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	minv=1000000
	epo=0
	while(count<10000):
		cou=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			its=np.dot(arr,arr)
			if(warr<=wid):
				wei+=((wid-warr)*arr)/its
				cou+=1
		if(minv>cou):
			minv=cou
			minw=wei
			epo=count+1
		count+=1
	return minw

def ftest2(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		dat[i,0]=1
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 2
		else:
			print 4

def fper2(train,test):
	wid=10
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	si=tr_data.shape[1]-1
	for i in xrange(tr_data.shape[0]):
		tr_data[i,0]=1
		if tr_data[i,si]==2:
			tr_data[i,0:si]*=-1
	wei=ftrain2(tr_data[:,0:si],tr_data[:,si],wid)
	ftest2(wei,tes_data,wid)
	
	
def main(train,test):
	fper1(train,test) #Algorithm 1
	fper2(train,test) #Algorithm 2

train = sys.argv[1]
test = sys.argv[2]
main(train,test)