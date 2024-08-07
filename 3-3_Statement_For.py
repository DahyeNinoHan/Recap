l1=['one','two','three']

for i in l1:
    print(i)

a=[(1,2),(3,4),(5,6)]
for (first,last) in a:
    print(first+last)

marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark>=60:
        pass
    else:
        print("%d학생 FAIL" %number)
        break

add=0
for i in range(1,11):
    add+=1
    print(add)

for i in range(2,10):
    for j in range(2,10):
        print(f'{i} 곱하기 {j}는 {i*j}',end='')



a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

a=[1,2,3,4]
result = [num*3 for num in a]
print(result)

a=[1,2,3,4]
result = [num*3 for num in a if num%2==0]
print(result)

result = [x*y for x in range(2,10) for y in range(2,10)]
print(result)

