import sys

if (len(sys.argv)<5):
    print("Usage: python3 lab06args.py <int 1> <int 2> <int 3> <int 4> <int 5>")
    exit()

print('Item 0 in sys.argv:', sys.argv[0])
print('Item 1 in sys.argv:', sys.argv[1])
print('Item 2 in sys.argv:', sys.argv[2])
print('Item 3 in sys.argv:', sys.argv[3])
print('Item 4 in sys.argv:', sys.argv[4])
print('Item 5 in sys.argv:', sys.argv[5])
#print((int(sys.argv[2]))*int(sys.argv[5]))