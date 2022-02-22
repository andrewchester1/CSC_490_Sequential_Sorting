import random

a = [7, 5, 2, 1, 3, 4, 6]

def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

@profile
def SelectionSort(arr):
    size = len(arr)
    for i in range(size - 1):
        k = i
        for j in range(i, size):
            print(i)
            if arr[k] > arr[j]:
                k = j
        swap(arr, i, k)
    return arr

@profile
def InsertionSort(arr):
    size = len(arr)
    for i in range(1, size):
        k = i
        v = arr[k]
        while k > 0 and arr[k - 1] > v:
            print(i)
            swap(arr, k - 1, k)
            k = k - 1
    return arr

@profile
def BubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            print(i)
            if arr[j] > arr[j + 1]:
                print(i)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def generateArray(ub, lb, s):
    arr = [0] * s
    tempArr = range(lb, ub + 1)
    for i in range(len(arr)):
        arr[i] = tempArr[i]

    random.shuffle(arr)
    return arr

ub = 100000
lb = 1
s = 100000
arr1 = generateArray(ub, lb, s)

selectionSortArray = SelectionSort(arr1)
insertionSortArray = InsertionSort(arr1)
bubbleSortArray = BubbleSort(arr1)

print('selectionSortArray', selectionSortArray)
print('insertionSortArray', insertionSortArray)
print('bubbleSortArray', bubbleSortArray)
