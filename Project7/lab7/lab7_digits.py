file = open('digits.txt','r')

''' # L2a
text = []
for line in file:
    text.append(line.strip())
    text += ' '
oneLine = file.readline()
result = ''.join(text)
print(result)
'''
#L2b
text = file.read()
text1 = text.split()
result ="\n".join(text1)
print(result)

#L2c
f=open("digit2.txt",'w')
f.write(result)
f.close()

