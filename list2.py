from random import randint
import time

######## ALGORITMOS DE ORDENAÇÃO PARA COMPARAÇÃO DE TEMPO

def bubbleSort(lst): 
    start = time.time()
    order = False
    nElements = len(lst)-1
    while not order:
        order=True
        for i in range(nElements):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i] 
                order = False      
    end = time.time()   
    elapsed = end - start
    return [lst,elapsed]

def selectionSort(lst):
    start = time.time()
    for i in range(len(lst)):
        minPosition = i
        for j in range(i+1, len(lst)):
            if lst[minPosition] > lst[j]:
                minPosition = j   
        temp = lst[i]
        lst[i] = lst[minPosition]
        lst[minPosition] = temp
    end = time.time()   
    elapsed = end - start               
    return [lst,elapsed]

def insertionSort(lst):
    start = time.time()
    for i in range(1,len(lst)):
        current = lst[i]
        while i>0 and lst[i-1]>current:
            lst[i] = lst[i-1]
            i = i-1
            lst[i] = current
    end = time.time()   
    elapsed = end - start        
    return [lst,elapsed]

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

#######ALGORITMOS DE ORDENAÇÃO PARA INDICAÇÃO DO PASSO A PASSO

def PrintBubbleSort(lst):
    start = time.time()
    order = False
    nElements = len(lst)-1
    while not order:
        order = True
        for i in range(nElements):
            pointer = " "
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1],lst[i]  
                order = False     
                print(lst)
                for z in range (0,i):
                    pointer += "   "
                pointer+="^  ^"
                print(pointer)
    end = time.time()   
    elapsed = end - start
    return [lst,elapsed]

def PrintSelectionSort(lst):
    start = time.time()
    for i in range(len(lst)):
        minPosition = i
        string = " "
        troca = False
        for j in range(i+1, len(lst)):
            if lst[minPosition] > lst[j]:
                minPosition = j
                troca=True    
        temp = lst[i]
        lst[i] = lst[minPosition]
        lst[minPosition] = temp
        print(lst)
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
    return [lst,elapsed]

def PrintInsertionSort(lst):
    start = time.time()
    for i in range(1,len(lst)):
        current = lst[i]
        while i>0 and lst[i-1]>current:
            string = " "
            lst[i] = lst[i-1]
            i = i-1
            lst[i] = current
            print(lst)
            for j in range(0,i):
                string+="   "
            string+="^  ^"
            print(string)
    end = time.time()   
    elapsed = end - start        
    return [lst,elapsed]



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