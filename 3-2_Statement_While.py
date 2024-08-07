i=0

while i<10:
    print(f'나무찍기 {i}번')
    i+=1
 

prompt = '''
1. Add
2. Del
3. List
4. Quit
'''

number=0
while number !=4:
    print(prompt)

    number=int(input())


coffee = 10
while True: 
    money = int(input('돈을 넣어 주세요. '))
    if coffee == 0:
        print('커피가 다 떨어졌습니다, 판매를 중지합니다.')
        break
    elif money == 300:
        print("돈을 받았으니 커피를 주겠어요. ")
        coffee-=1
    elif money >300:
        print("거스름돈 %d를 주고 커피를 줍니다." %(money-300))
        coffee-=1
    else:
        print('돈이 부족하잖니.')

