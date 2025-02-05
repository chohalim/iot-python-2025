# py04_file_inout.py

# 파일 입출력
# 파일 오픈, 읽고, 쓰고, 닫음
# 파일 경로 : 파일이 컴퓨터 상에 들어있는 위치
# 경로 구분자 \ / 다 사용 가능
# mode : r(읽기), w(쓰기), a(추가), ...
# encoding : 한글만(euc-kr, cp949), 국제어(utf-8)

## 상대경로
# . : 현재 자기 위치
# .. : 현재 자신의 부모폴더 위치
f = open('./day03/test.txt', mode = 'w', encoding = 'utf-8') 

## 절대경로
# 드라이브부터 모든 경로를 다 작성하는 방법
# C:
# f = open('C:/source/iot-python-2025/day03/test2.txt', mode = 'w', encoding = 'utf-8')

# f = open('../test3.txt', mode = 'w', encoding = 'utf-8')

# f = open('C:\\source\\iot-python-2025\\day03\\test5.txt', mode = 'w', encoding = 'utf-8') 
# # \역슬래시는 특수기호
# 역슬래시를 문자열에 표현하고 싶으면 \\ 두번사용


f.write('파일 쓰기 시작!\n')
f.write('두번째 줄 작성합니다.\n')
# f.write('\n')

f.close()
print('파일쓰기 완료')

r = open('./day03/test.txt', mode = 'r', encoding = 'utf-8')

while True:
    line = r.readline() # 한줄씩 읽음
    if not line: # 한줄 읽은 값이 None이면
        break   # while문을 탈출하라

    # print(line, end='')
    print(line.replace('\n',''))

r.close()
