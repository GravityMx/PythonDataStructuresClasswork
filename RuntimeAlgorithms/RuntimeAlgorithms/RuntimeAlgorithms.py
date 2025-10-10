import random
import time
from enum import Enum


class SearchType(Enum):
    LINEAR = 1
    ITERBINARY = 2
    RECURSIVEBINARY = 3

minValue = 0
maxValue = 500000

def IterativeLinearSearch(array, findTarget):
    
    for i in (array):
        if (i == findTarget):
            return True

    return False

def IterativeBinarySearch(array, findTarget):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == findTarget):
            return True
        elif (array[mid] < findTarget):
            low = mid + 1
        else:
            high = mid - 1
    return False

def RecursiveBinarySearch(array, findTarget, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low > high:
        return False

    mid = (low + high) // 2
    if array[mid] == findTarget:
        return True
    elif array[mid] < findTarget:
        return RecursiveBinarySearch(array, findTarget, mid + 1, high)
    else:
        return RecursiveBinarySearch(array, findTarget, low, mid - 1)

def GenerateRandomizedArray(length, rangeHigh, rangeLow=0):
    
    array = [0] * length
    
    for i in range(len(array)):
        array[i] = random.randint(rangeLow, rangeHigh)

    return array

def PerformLinearTrial(array):

    startTime = time.perf_counter()
    IterativeLinearSearch(array, random.randint(minValue, maxValue))
    return time.perf_counter() - startTime

def PerformIteratorBinaryTrial(array):

    startTime = time.perf_counter()
    IterativeBinarySearch(array, random.randint(minValue, maxValue))
    return time.perf_counter() - startTime
    
def PerformRecursiveBinaryTrial(array):

    startTime = time.perf_counter()
    RecursiveBinarySearch(array, random.randint(minValue, maxValue))
    return time.perf_counter() - startTime

def PerformTestTrials(arrayLength, type, numOfTrials=5):
    
    runningTotal = 0
    catagoryName = ""
    
    arrayOfArrays = [GenerateRandomizedArray(arrayLength, maxValue, minValue) for _ in range(numOfTrials)]

    if (type == SearchType.LINEAR):
        for i in arrayOfArrays:
            runningTotal += PerformLinearTrial(i) # Left Off here
        runningTotal /= numOfTrials
        catagoryName = "linear trials"
    else:
        # For Binary seaches, a sorting step is required, once done one, sorting does not need to happen again until the array is modified
        for i in arrayOfArrays:
            i.sort()
        
        if (type == SearchType.ITERBINARY):
            for i in arrayOfArrays:
                runningTotal += PerformIteratorBinaryTrial(i)
            runningTotal /= numOfTrials
            catagoryName = "iterative binary trials"
        else: # If the type is Recersive Binary
            for i in arrayOfArrays:
                runningTotal += PerformRecursiveBinaryTrial(i)
            runningTotal /= numOfTrials
            catagoryName = "recursive binary trials"

            
    print("This set of", numOfTrials, catagoryName, "over an array of size", arrayLength, "had an average clear time of: ", f"{runningTotal:.12f}")
    
        
# Main code block

PerformTestTrials(5000, SearchType.LINEAR, 5)
PerformTestTrials(5000, SearchType.ITERBINARY, 5)
PerformTestTrials(5000, SearchType.RECURSIVEBINARY, 5)

PerformTestTrials(50000, SearchType.LINEAR, 5)
PerformTestTrials(50000, SearchType.ITERBINARY, 5)
PerformTestTrials(50000, SearchType.RECURSIVEBINARY, 5)

PerformTestTrials(100000, SearchType.LINEAR, 5)
PerformTestTrials(100000, SearchType.ITERBINARY, 5)
PerformTestTrials(100000, SearchType.RECURSIVEBINARY, 5)

PerformTestTrials(150000, SearchType.LINEAR, 5)
PerformTestTrials(150000, SearchType.ITERBINARY, 5)
PerformTestTrials(150000, SearchType.RECURSIVEBINARY, 5)

PerformTestTrials(1000000, SearchType.LINEAR, 5)
PerformTestTrials(1000000, SearchType.ITERBINARY, 5)
PerformTestTrials(1000000, SearchType.RECURSIVEBINARY, 5)


# Test Cases

# newArray = [1, 2, 3, 4, 5, 6, 7] 
# newArray.sort() 

# print(IterativeLinearSearch(newArray, 5)) # Should be True
# print(IterativeLinearSearch(newArray, 8)) # Should be False
# print(RecursiveBinarySearch(newArray, 6)) # Should be True
# print(RecursiveBinarySearch(newArray, 0)) # Should be False
# print(RecursiveBinarySearch(newArray, 2)) # Should be True
# print(RecursiveBinarySearch(newArray, 9)) # Should be False