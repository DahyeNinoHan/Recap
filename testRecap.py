import copy as copy 

a=[1,2,3]
b=copy(a)
print(b)

a='python'
b='life'
c,d=('PYTHON','LIFE')
print(c,d)

a=b='python'

a=3
b=5

a,b = b,a 