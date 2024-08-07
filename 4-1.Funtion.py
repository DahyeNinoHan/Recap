def add(a,b):
    return a+b

def say():
    return "hi"

print(say())

def multiply(a,b):
    print("%d * %d = %d" %(a,b,a*b))
    

a=multiply(1,2)
print(a)


def sub(a,b):
    return a-b

sub(a=9,b=3)

def add_many(*args):
    result = 0
    for i in args:
        result +=i
    return result

print(add_many(1,2,3,4,5))

def cal(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result+=i
    elif choice == 'mul':
        result =1
        for i in args:
            result*=i
    return result 
print(cal("mul",1,2,3,4))

def print_kwargs(**kwargs):
    print(kwargs)
    print(kwargs['a'])

print_kwargs(a=1,b=2)

def add_and_mul(a,b):
    return a+b


def say_nick(nick):
    if nick=='moron':
        return
    print(f'My nickname is {nick}.')

say_nick('Beauty')
say_nick('moron')
say_nick('Hansome')


a=1
def vartest():
    global a 
    a=a+1
vartest()
print(a)

# mutable: int, double, String, tuple
# immutable: list, dictionary, set

#immutable
a=1
def vartest(a):
    a=a+1
vartest(a)
print(a)

#mutable
b=[1,2,3]
def vartest2(b):
    b=b.append(4)
vartest2(b)
print(b)

a=[1,2,3,4,5]
result = a.append(5)
print(result) # None

result=a.pop()
print(result) # 5

result = a.insert(0,10)
print(result)
print(a)
