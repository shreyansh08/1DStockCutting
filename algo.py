import numpy as np
import matplotlib.pyplot as plt
import sys

def bestFit(weight,capacity):
    wastage = 0
    numberOfBins = 0
    capacity = int(capacity)
    # bin_rem = capacity
    n = np.size(weight)

    bin_rem = [0] * n

    for i in range(np.size(weight)):
        minVal = capacity+1
        idx = 0
        for j in range(numberOfBins):
            if(bin_rem[j] >= weight[i] and bin_rem[j]-weight[i]<minVal):
                idx = j
                minVal = bin_rem[j] - weight[i]
        if minVal==capacity+1:
            bin_rem[numberOfBins] = capacity - weight[i]
            numberOfBins+=1
        else:
            bin_rem[idx] -= weight[i]

    for i in range(numberOfBins):
        wastage += bin_rem[i]
    return wastage,numberOfBins


def nextFit(weight,capacity):
    wastage = 0
    numberOfBins = 0
    capacity = int(capacity)
    bin_rem = capacity

    for i in range(np.size(weight)):
        if weight[i] > bin_rem:
            wastage += bin_rem
            numberOfBins += 1
            bin_rem = capacity - weight[i]
        else:
            bin_rem -= weight[i]
    wastage += bin_rem
    return wastage,numberOfBins


sys.stdin = open('output1.txt','r')
testCases = int(input())
wastageArrNext = []
binsArrNext = []
wastageArrBest = []
binsArrBest = []
for i in range(testCases):
    print("current case:" + str(i))
    len,orders = (input()).split(' ')
    temp = input().split(' ')
    temp = np.array(temp)
    arr = []
    for i in range(np.size(temp)):
        arr.append(int(temp[i]))
    arr = np.array(arr)
    waste,cnt = nextFit(arr,len)
    wastageArrNext.append(waste)
    binsArrNext.append(cnt)

    waste,cnt = bestFit(arr,len)
    wastageArrBest.append(waste)
    binsArrBest.append(cnt)

# space = np.linspace(1,50,50)
# plt.figure()
# plt.subplot(121)
# plt.title('Wastage in Next Fit')
# plt.plot(space,wastageArrNext)

# plt.subplot(122)
# plt.title('Wastage in Best Fit')
# plt.plot(space,wastageArrBest)

# plt.savefig('wastage.png')

# plt.figure()
# plt.subplot(121)
# plt.title('Number of Bins in Next Fit')
# plt.plot(space,binsArrNext)

# plt.subplot(122)
# plt.title('Number of Bins in Best Fit')
# plt.plot(space,binsArrBest)

# plt.savefig('bins.png')
# plt.show()

# analyses
#  wastage average
wastageArrBest = np.array(wastageArrBest)
wastageArrNext = np.array(wastageArrNext)
print("Average wastage in Best Fit: " + str(np.mean(wastageArrBest)))
print("Average wastage in Next Fit: " + str(np.mean(wastageArrNext)))


# bins average
binsArrBest = np.array(binsArrBest)
binsArrNext = np.array(binsArrNext)
print("Average bins in Best Fit: " + str(np.mean(binsArrBest)))
print("Average bins in Next Fit: " + str(np.mean(binsArrNext)))

