# py06_exception.py

# 예외처리
## 오류, Error, Fault,
## 1. Error(문법적 오류) - 코딩하다가 빨간색 밑줄 생기는 오류
##    오류표시가 안나고 코딩을 잘못한 오류 포함(!) mul(7, 6) -> 42예상, 결과13
## 2. Exception(실행중 발생 예외) - 문법오류 수정 후 실행하다가 비정상 종료되는 거
## 파이썬은 Error도 **Error고 Exception도 **Error
## 에디터 상에 오류표시가 나면 Error
## 실행 중에 발생하면 Exception
## try :
##      예외가 발생할 수 있는 로직
## except 예외클래스 as e:
##    예외처리 로직
##    Exception 클래스는 다른 모든 예외 클래스의 조상, Exception만 쓰면 됨됨
## [finally:] - 옵션
##     예외발생 유무와 상관없이 항상 처리해야 할 로직
## try문을 반복해서 사용하지 말 것 - 속도 느려짐짐

## 디버깅 - 천천히 어디에서 예외(오류)가 발생하는 지 확인하기 위해 사용
## F9 - 중단점(Break Point) 표시/해제 기능
## F5 - 디버깅 시작, 중단점까지 실행
## F10 - 한 줄 실행, 함수가 있어도 함수를 실행하고 넘어감
## F11 - 한 줄 실행, 함수가 있으면 함수 안으로 진입
## Shift + F5 - 디버깅 종료
## 변수 탭 - 현재 변수에 들어있는 값 표시
## 조사식 탭 - 내가 원하는 식을 실행, 결과 표시
## 예외는 오류로 안 나옴


numbers = list(range(1,11))
for i in numbers: ############ 포인문 쓰는 이유 ??? i로 간단히 나타내기 위해서 ?
    # print(i)
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
    elif op == '*':
        try: # 콜론은 안으로 들어간다.
            x, y = input('곱할 수 입력 > ').split()
            x = int(x)
            y = int(y)

            print(f'{x} * {y} = {mul(x, y)}')

        except Exception as e: # as e 없으면 무슨에러인지 확인이 안됨
            print(f'입력 실수 {e}')
            # print('입력 실수. 다시하세요.') # 최종적으로 사용자만 확인되는 에러메세지

    elif op == '/': 
        try:
            x, y = input('나눌 수 입력 > ').split()
            x = int(x)
            y = int(y)
            print(f'{x} / {y} = {div(x, y)}')
        except ValueError as e: ################ except Exception as e: 로 써도 같은 결과, 무슨 차이 ?
            print(f'입력 실수 {e}')
        except ZeroDivisionError as e:
            print(f'너 바보야? 0으로 왜 나눠?')
            print(f'{e}')

    else:
        print('정확한 입력 요망')
