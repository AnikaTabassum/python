from random import seed
from random import randint
from math import ceil
import math
from random import shuffle
import random
class knn:
    def __init__(self):
        "do "

    def processInput(self):

        global cnt
        global obj
        with open("heber.txt", 'r') as f:
            for txt in f:
                x = txt.split(",")
                # print(txt)
                dataSet.insert(cnt, x)
                cnt = cnt + 1
        #print(dataSet)
        self.testSet(cnt)

    def testSet(self,cnt):
        testset=ceil(cnt/10.0)
        random.Random(10).shuffle(dataSet)
        k=0
        tempData = list()
        while k<10:
            tempData.extend(testData)
            testData.clear()
            i=0
            idx=k*testset

            while i < testset:
                if i+idx>=cnt:
                    break
                testData.insert(i, dataSet[idx+i])
                i = i + 1
            index=(i*k)+testData.__len__()
            i=0
            j=0
            trainData.clear()
            while index+i < cnt:

                trainData.insert(j, dataSet[index+i])
                i = i + 1
                j=j+1
            trainData.extend(tempData)

            self.calculate()
            k=k+1
            #print(trainData)
            #print(testData)

    def calculate(self):
        locals()
        totalaccuracy=0
        cnta = 0
        len=trainData.__len__()
        k=0
        while k<testData.__len__():
            i = 0
            resultList.clear()
            while i < len:
                j = 0
                res = 0.0
                while j < 3:
                    result = float(testData[k][j]) - float(trainData[i][j])
                    res += result ** 2
                    j = j + 1
                res = math.sqrt(res)
                indexList = (res, trainData[i][3], testData[k][3])
                resultList.append(indexList)
                resultList.insert(i, indexList)
                i = i + 1
            resultList.sort()
            a1 = int(resultList[0][1])
            a2 = int(resultList[1][1])
            a3 = int(resultList[2][1])
            acr=self.selectClass(a1, a2, a3)
            self.f_measure(acr)
            if acr == int(resultList[0][2]):
                cnta = cnta + 1
            k = k + 1
        self.countAccuracy(cnta)


    def selectClass(self,a1,a2,a3):
        cnt1 = 0
        cnt2 = 0
        if a1==1:
            cnt1=cnt1+1
        if a2==1:
            cnt1=cnt1+1
        if a3==1:
            cnt1=cnt1+1
        if a1==2:
            cnt2=cnt2+1
        if a2==2:
            cnt2=cnt2+1
        if a3==2:
            cnt2=cnt2+1

        if cnt1 > cnt2:
            finalClass=1
        else:
            finalClass=2

        return finalClass;


    def countAccuracy(self,acr):
        accuracy=acr/testData.__len__()
        acrList.append(accuracy)
        if acrList.__len__()==10:
            self.avgAcr()

    def avgAcr(self):
        ans=0.0
        i=0
        while i <acrList.__len__():
            ans=ans+acrList[i]
            i=i+1
        ans=ans/10.0
        print("Average accuracy: "+str(ans))

    def f_measure(self,predicted_class):

        global tp,tn,fn,fp, cn1
        if predicted_class==1 and int(resultList[0][2])==1:
            tp=tp+1
        elif predicted_class==1 and int(resultList[0][2])==2:
            fp=fp+1
        elif predicted_class == 2 and int(resultList[0][2]) == 1:
            tn = tn + 1
        elif predicted_class == 2 and int(resultList[0][2]) == 2:
            fn = fn + 1

        cn1=cn1+1
        '''
        if cn1==cnt:
            print("F-measures")
            print(tp)
            print(fp)
            print(fn)
            print(tn)
        '''

    def precision(self):
        global precision
        precision=tp/(tp+fp)
        print("precision "+str(precision))
        #print(precision)

    def recall(self):
        global recall
        recall = tp / (tp + fn)
        print("recall "+ str(recall))
        #print(recall)

    def f1(self):
        f1=2*((precision*recall)/(precision+recall))
        print(f1)

dataSet = list()
trainData = list()
testData=list()
resultList= list()
acrList=list()
tp=fp=fn=tn=cn1=cnt=0
precision=recall=0.0
d = knn().processInput()
d=knn().precision()
knn().recall()
knn().f1()

