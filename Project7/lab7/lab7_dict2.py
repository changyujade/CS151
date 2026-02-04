file = open('abcs2.txt','r')
letterDict={}

for i in range(26):
    key = file.readline().strip()
    value = key + " "
    for j in range(2):
        value += file.readline().strip() + " "
    letterDict[key] = value 

print(letterDict)

print(len(letterDict.keys()))  # 26
print(list(letterDict.keys())[:5])  # ['a', 'b', 'c', 'd', 'e']
print(letterDict['a'])  # a is for apple
print(letterDict['b'])  # b is for banana
print(letterDict['z'])  # z is for zebra