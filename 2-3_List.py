# ## String ##

# # 문자열 슬라이싱
# a='ddfdfsdfsdf'
# b=a[1:10:1]
# print(a)
# c=a[::-1]
# print(c)

# # f포매팅
# name='Nino'
# age=30
# print(f'My name is {name}. I am {age} years old')


# # 문자열 개수 세기
# a='hobby'
# print(a.find('h'))


# # 문자열 위치 찾기 -- 첫 번째 찾은 애의 인덱스 리턴
# print(a.find('b'))

# # 문자 삽입 join
# a=','.join('abcd')
# print(a)

# #대문자로 바꾸기
# print(a.upper())
# print(a.lower())

# # 공백 없애기
# a='   cute   '
# print(a.rstrip())
# print(a.lstrip())
# a='   cute   '
# print(a.strip())

# # 문자열 바꾸기
# a = "Life is too short"
# print(a.replace('Life','Leg'))

# #문자열을 쪼개서 리스트에 넣기
# print(a.split())

# a="a:b:c:d"
# print(a.split(':'))




# ## List ##
# a = [a, "hello", ['a','b','c']]
# print(a[1][0])
# print(a[0::2]) #리스트 슬라이싱


# print(a*3)

# a=[1,2,3,4]
# del a[1]
# print(a)
# print(a.index(3))

a = [1,2,3,4]
a.insert(0,4) #0번째 인덱스에 4를 추가하겠다
print(a)

#리스트 요소 끄집어 내기 
a = [1,2,3] 
b = a.pop() # 마지막꺼를 튀어 내보냄


print(a)
print(b)

a = [1,2,3] 
c = a.pop(1) #인덱스1 내보냄
print(c)

a = [1,2,3]
a+=[4]
print(a)