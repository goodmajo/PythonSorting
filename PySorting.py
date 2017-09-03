'''PySorting.py'''
# A little collection of sorting algos written in python. These functions can take in lists or numpy arrays.
# Joel Goodman - joelrgoodman@gmail.com - 2017

import numpy
import math
from statistics import median

'''Some Requiured Functions...'''

def Merge(left, right):
    mergedList = [None] * (len(left) + len(right))
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mergedList[k] = left[i]
            i += 1
        else:
            mergedList[k] = right[j]
            j += 1
        k +=1

    while i < len(left):
        mergedList[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        mergedList[k] = right[j]
        j += 1
        k += 1

    return mergedList

'''Sorting Functions'''
# Stupid Sort!
def StupidSort(aList, returnAList = True):
    # If the user gives a numpy array, convert it to a list
    arrayFlag = False
    if type(aList) == numpy.ndarray:
        aList = aList.tolist()
        arrayFlag = True

    sortedList = [None] * len(aList)

    for i in range(0, len(aList)):
        currentMinIndex = aList.index(min(aList))
        sortedList[i] = aList[currentMinIndex]
        del aList[currentMinIndex]

    # Convert the list back to an array, if necessary
    if arrayFlag == True and returnAList == False:
        sortedList = numpy.array(sortedList)

    return sortedList

# Insertion Sort
def InsertionSort(aList, returnAList = True):
    # If the user gives a numpy array, convert it to a list
    arrayFlag = False
    if type(aList) == numpy.ndarray:
        aList = aList.tolist()
        arrayFlag = True

    for j in range(1, len(aList)):
        key = aList[j]
        i = j - 1
        while i > -1 and aList[i] > key:
            aList[i + 1] = aList[i]
            i -= 1
        aList[i + 1] = key

        # Convert the list back to an array, if necessary
        if arrayFlag == True and returnAList == False:
            aList = numpy.array(aList)

    return aList

# Merge Sort
def MergeSort(aList, returnAList=True):
    # If the user gives a numpy array, convert it to a list
    arrayFlag = False
    if type(aList) == numpy.ndarray:
        aList = aList.tolist()
        arrayFlag = True

    if len(aList) > 1:
        left = aList[0:math.floor(len(aList) / 2)]
        right = aList[math.floor(len(aList) / 2): len(aList)]
        left = MergeSort(left)
        right = MergeSort(right)
        sortedList = Merge(left, right)
    else:
        sortedList = aList

    if arrayFlag == True and returnAList == False:
        sortedList = numpy.array(aList)

    return sortedList

'''Bubble Sort'''
def BubbleSort(aList, returnAList = True):
    # If the user gives a numpy array, convert it to a list
    arrayFlag = False
    if type(aList) == numpy.ndarray:
        aList = aList.tolist()
        arrayFlag = True

    n = len(aList)
    while n > 0:
        m = 0
        for i in range(1, len(aList)):
            if aList[i - 1] > aList[i]:
                aList[i - 1], aList[i] = aList[i], aList[i - 1]
                m = i
        n = m

    if arrayFlag == True and returnAList == False:
        aList = numpy.array(aList)

    return aList

'''Quick Sort'''
def QuickSort(aList, returnAList = True):
    # If the user gives a numpy array, convert it to a list
    arrayFlag = False
    if type(aList) == numpy.ndarray:
        aList = aList.tolist()
        arrayFlag = True

    left = []
    center = []
    right = []

    if len(aList) > 1:
        pivotIndex = min( range(len(aList)), key = lambda i: abs(aList[i] - median(aList)))

        for i in range(0, len(aList)):
            if aList[i] < aList[pivotIndex]:
                left.append(aList[i])
            elif aList[i] > aList[pivotIndex]:
                right.append(aList[i])
            else:
                center.append(aList[i])
        left = QuickSort(left)
        center = QuickSort(center)
        right = QuickSort(right)

        aList = left + center + right

    if arrayFlag == True and returnAList == False:
        aList = numpy.array(aList)

    return aList