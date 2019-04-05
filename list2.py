from random import randint
import time



def bubbleSort(roger):
    start = time.time()
    lst = roger
    nElements = len(lst)-1
    while not order:
        for i in range(nElements):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]       
    end = time.time()   
    elapsed = end - start
    return [lst,elapsed]

def selectionSort(roger):
    start = time.time()
    alist = roger
    for i in range(len(alist)):
        minPosition = i
        for j in range(i+1, len(alist)):
            if alist[minPosition] > alist[j]:
                minPosition = j   
        temp = alist[i]
        alist[i] = alist[minPosition]
        alist[minPosition] = temp
    end = time.time()   
    elapsed = end - start               
    return [alist,elapsed]

def insertionSort(roger):
    start = time.time()
    alist = roger
    for i in range(1,len(alist)):
        current = alist[i]
        while i>0 and alist[i-1]>current:
            alist[i] = alist[i-1]
            i = i-1
            alist[i] = current
    end = time.time()   
    elapsed = end - start        
    return [alist,elapsed]

def sortTime(funcao,n):
    relacao = []
    for i in range(n):
        vetor = []
        for j in range(i):
            value = randint(0, 10)
            vetor.append(value)
        tempo = funcao(vetor)
        relacao.append([tempo[1],i])
    return relacao

sortTime(insertionSort,10)


def PrintBubbleSort(roger):
    start = time.time()
    lst = roger
    nElements = len(lst)-1
    while not order:
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
        current = alist[i]
        while i>0 and alist[i-1]>current:
            string = " "
            alist[i] = alist[i-1]
            i = i-1
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