import graphics as gr 
file= open('colossalFontAlphabet.txt',"r")
file2 = open('colossalFontSymbols.txt',"r")
string=''
values=''
letterDict={}

#trying to put the keys into a list
for line in file:
    string += line
res = list(string)

#puts the collosal texts into the value of the dictionary named res2
res2={}
for key in res:
    value = file2.readline()
    for j in range(10):
        value += file2.readline()
    res2[key]=value
    
def vertical():
    #extention: printing it vertically
    str=''
    for k in userList:
        v=res2[k].split('\n')
        for i in range(11):
            str += v[i]+'\n'
    print(str,"done")

def horizontal():
    str=''
    for i in range(11):
        for k in userList:
            v=res2[k].split('\n')
            str += v[i]
        str += ('\n')
    print(str,"done")


if __name__ == '__main__':
    user=input("What do you want to type?")
    choice=input('do you want to do it vertically or horizontally. Type h or v') #extention 1 - prints the letters vertically
    userList=list(user)
    if choice=='h':
        horizontal()
    elif choice=='v':
        vertical()
    else:
        print('error, please retry')
        exit()

