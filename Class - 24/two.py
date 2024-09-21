fp = None

try :
    fp = open('data.txt','r')
    
except :
    fp = open('one.txt','r')

data = fp.read()
print(data)

print('Hello ! Guys')