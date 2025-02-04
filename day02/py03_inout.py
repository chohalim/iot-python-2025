# py03_inout.py
# 화면입출력

print('출력입니다.')

# 기본입력
number = input('만나이를 입력하세요 >') # 입력방법
 # 입력되는 값, 출력되는 값 모두 문자열!
number = int(number) # str -> int
print(type(number))
print(number)


# 다중입력
x, y = input('합산할 두 수를 입력하세요 >').split() # 기본으로 공백을 잘라줘
x = int(x)
y = int(y)
print(x + y)