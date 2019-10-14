import sys
import numpy as np

#Start of Algorithm 1
#Single Sample Perceptron without margin
def ftrain1(dat,lab,wid):
	temp=np.zeros(dat.shape[1])
	wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	while(flag==1):
		flag=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			if(warr<=wid):
				temp+=arr
				flag=1
				wei+=temp
		count+=1
	return wei

def ftest1(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 0
		else:
			print 1

def fper1(train,test):
	wid=0
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	for i in xrange(tr_data.shape[0]):
		if tr_data[i,0]==0:
			tr_data[i,1:]*=-1
	wei=ftrain1(tr_data[:,1:],tr_data[:,0],wid)
	ftest1(wei,tes_data,wid)

#Start of Algorithm 2
#Single Sample Perceptron with margin=100
def ftrain2(dat,lab,wid):
	temp=np.zeros(dat.shape[1])
	wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	while(flag==1):
		flag=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			if(warr<=wid):
				temp+=arr
				flag=1
				wei+=temp
		count+=1
	return wei

def ftest2(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 0
		else:
			print 1

def fper2(train,test):
	wid=100
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	for i in xrange(tr_data.shape[0]):
		if tr_data[i,0]==0:
			tr_data[i,1:]*=-1
	wei=ftrain2(tr_data[:,1:],tr_data[:,0],wid)
	ftest2(wei,tes_data,wid)

#Start of Algorithm 3
#Batch Perceptron without margin
def ftrain3(dat,lab,wid):
	temp=np.zeros(dat.shape[1])
	wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	while(flag==1):
		flag=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			if(warr<=wid):
				temp+=arr
				flag=1
			wei+=temp
		count+=1
	return wei

def ftest3(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 0
		else:
			print 1

def fper3(train,test):
	wid=0
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	for i in xrange(tr_data.shape[0]):
		if tr_data[i,0]==0:
			tr_data[i,1:]*=-1
	wei=ftrain3(tr_data[:,1:],tr_data[:,0],wid)
	ftest3(wei,tes_data,wid)


#Start of Algorithm 4
#Batch Perceptron with margin=100000000
def ftrain4(dat,lab,wid):
	temp=np.zeros(dat.shape[1])
	wei=np.zeros(dat.shape[1])
	flag=1
	count=0
	while(flag==1):
		flag=0
		for i in xrange(dat.shape[0]):
			arr=np.array(dat[i])
			warr=np.dot(arr,wei)
			if(warr<=wid):
				temp+=arr
				flag=1
			wei+=temp
		count+=1
	return wei

def ftest4(wei,dat,wid):
	acc=0
	for i in xrange(dat.shape[0]):
		arr=np.array(dat[i,:])
		warr=np.dot(arr,wei)
		if(warr<=wid):
			print 0
		else:
			print 1

def fper4(train,test):
	wid=100000000
	tr_data=np.loadtxt(open(train), delimiter=",", dtype="int")
	tes_data=np.loadtxt(open(test), delimiter=",", dtype="int")
	for i in xrange(tr_data.shape[0]):
		if tr_data[i,0]==0:
			tr_data[i,1:]*=-1
	wei=ftrain4(tr_data[:,1:],tr_data[:,0],wid)
	ftest4(wei,tes_data,wid)
	
	
def main(train,test):
	fper1(train,test) #Algorithm 1
	fper2(train,test) #Algorithm 2
	fper3(train,test) #Algorithm 3
	fper4(train,test) #Algorithm 4

train = sys.argv[1]
test = sys.argv[2]
main(train,test)