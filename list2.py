from random import randint
import time


def bubbleSort(roger):
    start = time.time()
    lst = roger
    nElements = len(lst)-1
    order = False
    pointer = ""
    while not order:
        order = True
        for i in range(nElements):
            pointer = ""
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]
                order = False        
                print(lst)
            if not order:
                for z in range (0,i+1):
                    pointer += "  "
                pointer+="^  ^"
                print(pointer)
    end = time.time()   
    elapsed = end - start
    return [lst,elapsed]

def selectionSort(roger):
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

def insertionSort(roger):
    start = time.time()
    alist = roger
    y=0
    z=0
    for i in range(1,len(alist)):
        troca=False
        string = " "
        current = alist[i]
        while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            y=i
            i = i-1
            z=i
            troca = True
            alist[i] = current
        print(alist)
        if(troca):
            for j in range(0,z):
                string+="   "
            string+="^"
            for j in range(0,y):
                string+="   "
            string+="^"
            print(string)
    end = time.time()   
    elapsed = end - start        
    return [alist,elapsed]


vetor = []

for _ in range(10):
	value = randint(0, 10)
	vetor.append(value)

aux = vetor
print(insertionSort(aux))
print("lhul\n")

aux = vetor

print(selectionSort(aux))
aux = vetor
print("lhul\n")

print(bubbleSort(aux))

print("lhul\n")
