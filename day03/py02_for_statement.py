# py02_for_statement.py

# for문 : 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#   구문안으로 ...

# 아래와 같이 *이 늘어나는 프로그램을 작성하시오
'''
*
**
***
****
'''

# range() 범위를 생성해주는 클래스
# 마지막수 : max -1
# range(8) == range(0, 8) -> 0~7을 의미
# range(init, max, addtion)
# print(range(8))

# for i in range(0, 8, 2): # 조건이 참인 동안 반복 # 짝수만 나오게
#     print(i)

# num = int(input('최대별수 : '))

# for i in range(1, num + 1): # 마지막 수에 +1 해야 입력값만큼 '*' 출력됨
#     print('*' * i)

# 구구단
# 2*9 ~ 9*9
# 1. 한줄에 각 단씩 나오도록
# 2. x*y 값이 항상 두 자릿수로 표현 되도록 :2d 로
# 3. 단 시작을 표시해주세요.
for x in range(2, 9 + 1):
    # if x == 8: break # if문 뒤에 조건 1가지는 한 줄에 같이 쓸 수 있음
    if x == 8: continue # 8은 지나가고 그대로 진행

    print(f'{x}단 시작')
    for y in range(1, 9 + 1):
        # if y == 8: break
        if y == 7: continue # 7은 지나가고 그대로 진행행
        print(f'{x} x {y} = {x * y:2d}', end = '   ')

    print() # 그냥 한 줄 내리기

print('구구단 종료\n\n') # \n은 한줄 띄우기

## 반복을 빠져나올 때 : break
## 반복문에서 특정 조건을 지나칠 때 : continue

