from os import linesep


file= open('frankensteinChapter8.txt',"r")
frankText = ''

for line in file:
    frankText += line
print(len(frankText))

sentences= frankText.split(".")

# print(sentences[0])
# print(len(sentences))

words = frankText.split()
# print(words[0])
# print(len(words))

dash = '-'.join(words)

lines=[]
for line in file:
    lines.append(line.strip())

file.close()
fullText = ''.join(frankText) 
print(fullText)

f=open("NewFrankText",'w')
f.write(fullText)
f.close()
