a = {1:'a'}
a[2] = 'b'
a['Ganada'] = 'b' 
print(a)

del a[2]
print(a)

grade = {'pey': 100,
         'Kay': 99}
print(grade['pey'])

print(grade)

# 딕셔너리 Key로는 immutable 자료형을 사용해야 함

a = {'name':'pey',
     'phone':'010-4332-9843',
     'birth':'1118'}
print(a.keys())

for k in a.keys():
    for i in a.values():
        print(f'{k} and {i}')

print(a.items())
#print(a.clear())

print(a.get('pHone','nono'))
print(a['phone'])

print('name' in a)

a = {0:1,1:2,2:3}
print(a)
print(type(a))