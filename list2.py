def bubbleSort(lst):
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
    return lst

def selectionSort(alist):
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
    return alist

def insertionSort(alist):
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
    return alist

insertionSort([1,5,4,2,3])

selectionSort([1,5,4,2,3])

bubbleSort([1,5,4,2])

