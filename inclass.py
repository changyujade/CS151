def countdown(n):
    if n <= 0:
        return 0
    else:
        print(n)
        return countdown(n-1)


def countdown2(n):
    print(n)
    if n>1:
        countdown2(n-1)
    print(n)

#countdown2(5)
'''
l = [5,3,6,7]
'''

def sumlist(l):
    total = 0
    for i in l:
        total += i
    return total

def rec_sumlist(sublist):
    if len(sublist)==0:
        return 0
    else:
        return sublist[0]+rec_sumlist(sublist[1:])


'''
print(sumlist(l))
print(rec_sumlist(l))
'''


