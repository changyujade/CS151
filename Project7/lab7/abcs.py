file = open('abcs.txt','r')
letterDict={}

abcList=[]
for line in file:
    abcList.append(line.strip())
print(abcList)

for phrase in abcList:
    letterDict[phrase[0]]=phrase[9:]

'''
Alternate Method 
line=file.readline()
letterDict={}
while line!= '':
    text=line.split("is for)
    letterDict[t[0]=line.strip()]
    line = file.readline()
'''

print(len(letterDict.keys()))  # 26
print(list(letterDict.keys())[:5])  # ['a', 'b', 'c', 'd', 'e']
print(letterDict['a'])  # a is for apple
print(letterDict['b'])  # b is for banana
print(letterDict['z'])  # z is for zebra
print(letterDict)

#Task 3d
abcs = ''
for i in letterDict:
    abcs += i
print(abcs)

#Task 3e
words = ''
for i in letterDict:
    words += (letterDict[i])
    words += (' ')

print(words)
