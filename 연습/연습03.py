numbers = list(range(1,11))
for i in numbers:
    # print(i) ############# 포인문 사용하는 이유? print(numbers) 랑 같지 않나?
    pass

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

# q를 만나기 전까지 끝나지 않음
print('계산 시작')
while True:
    op = input('계산할 연산을 입력(*, /, q)')
    if op == 'q': # 종료조건
        break
    elif op == '*': # 곱하기
        x, y = input('곱할 수 입력 > ').split()
        x = int(x)
        y = int(y)
        print(f'{x} * {y} = {mul(x, y)}')
    elif op == '/': # 나누기
        x, y = input('나눌 수 입력 > ').split()
        x = int(x)
        y = int(y)
        print(f'{x} / {y} = {div(x, y)}')
    else:
        print('정확한 입력 요망')