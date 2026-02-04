
def reverseString(word):
    if len(word) == 0:
        return ""
    else: 
        #return reverseString(word[1:]+word[0])
        return word[-1] + reverseString(word[:-1])

def search(list,value):
    if value in list:
        return list.index(value)
    else:
        return -1

def search_rec(list,value,count = 0):
    if len(list) == 0:
        return -1
    elif list[0]== value:
        return count
    else:
        return search_rec(list[1:],value,count+1)

def binarySearch(list,value):
    list = list.sort()
    if len(list) = 

print(search_rec('word','o'))