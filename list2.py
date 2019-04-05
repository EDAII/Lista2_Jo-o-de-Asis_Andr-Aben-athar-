from random import randint
import time


def PrintBubbleSort(roger):
    start = time.time()
    lst = roger
    nElements = len(lst)-1
    order = False
    while not order:
        order = True
        for i in range(nElements):
            pointer = " "
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]       
                print(lst)
                for z in range (0,i):
                    pointer += "   "
                pointer+="^  ^"
                print(pointer)
    end = time.time()   
    elapsed = end - start
    return [lst,elapsed]

def PrintSelectionSort(roger):
    start = time.time()
    alist = roger
    for i in range(len(alist)):
        minPosition = i
        string = " "
        troca = False
        for j in range(i+1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j
                troca=True    
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp
        print(alist)
        if troca:
            for j in range(0,i):
                string +="   "
            string+="^"
            for j in range(0,minPosition-i):
                string +="  "
            string+="^"
            print(string) 
    end = time.time()   
    elapsed = end - start               
    return [alist,elapsed]

def PrintInsertionSort(roger):
    start = time.time()
    alist = roger
    y=0
    z=0
    for i in range(1,len(alist)):
        troca=False
        current = alist[i]
        while i>0 and alist[i-1]>current:
            string = " "
            alist[i] = alist[i-1]
            i = i-1
            troca = True
            alist[i] = current
            print(alist)
            for j in range(0,i):
                string+="   "
            string+="^  ^"
            print(string)
    end = time.time()   
    elapsed = end - start        
    return [alist,elapsed]



def monkeyCopy(vect, copy):
    for i in range(len(vect)):
        copy.append(vect[i])
    return vect


vetor = []
for i in range(5):
	value = randint(0, 10)
	vetor.append(value)

aux = []
monkeyCopy(vetor,aux)
aux
print(PrintInsertionSort(aux))
aux = []
monkeyCopy(vetor,aux)
aux
print(PrintSelectionSort(aux))
aux = []
monkeyCopy(vetor,aux)
aux
print(PrintBubbleSort(aux))