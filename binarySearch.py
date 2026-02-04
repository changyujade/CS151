def binarySearch(sList, value):
    subList=sList
    index = 0
    while len(subList)>0:
        middle = len(subList)//2
        middleValue = subList[middle]
        if (value < middleValue):
            #continue search on the left half
            subList = subList[:middle]
            #index += middle
            #return index
        elif (value > middleValue):
            subList = subList[middle+1:]
            index += middle+1 #something wrong with adding the middle
            return index
        else:
            return index + middle
        return -1

myList100 = list(range(100))
print(binarySearch(myList100,90))