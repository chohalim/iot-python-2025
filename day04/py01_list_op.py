# py01_list_o.py

# 리스트 연산
# 리스트가 for, while 반복문에서 가장 많이 활용되는 구조
# iterable -> 반복할 수 있는 요소가 for, while문에 사용
listSimple = [1,2,3,4,5,6,7,8,9,10] # 반복

sum = 0
for i in listSimple:
    sum = sum + i # sum += i

print(f'합산결과 = {sum}')
# 리스트 연산
arr = [1,2,3,4,5]
arr2 = [2,4,6,8,10]

# print(arr)
# print(arr[4])
# print(arr[0] + arr[2])
# print(arr[-2])
# print(arr[2:3])

print(arr+arr2) # 중복수 그대로 나옴옴
print(arr*2)

## 리스트 길이
print(len(arr)) 

## 데이터 할당
arr[2] = 9 # 9가 들어가고 원래 숫자 없어짐
print(len(arr), arr)

## 리스트 요소 삭제
# arr[2] = None 불가함
del(arr[2]) # 3이 삭제됨
print(len(arr), arr)

## 리스트 요소 추가
arr.append(7) # 리스트의 마지막에 추가됨
print(len(arr), arr)

arr.insert(2, 100) # 2자리에 추가됨
print(len(arr), arr)

## 리스트 합칠 때
arr + arr2 ################################### 왜 None 나옴?
print(arr.extend(arr2))

## 리스트 정렬(쇼핑몰 낮은가격순, 높은가격순, 최신일자부터 ...)
arr = [6, 7, 1, 3, 9, 0, 2, 8,] # 마지막에 쉼표 무관
print(arr)
arr.sort() # 오름차순
print(arr)
arr.sort(reverse=True) # 오름차순 반대, 내림차순 정렬
print(arr)

## 요소의 위치파악
print(arr.index(6)) # 없는 데이터의 순서를 인덱스하면 오류발생
# find는 문자열만 가능

## 요소 꺼내기
print(arr.pop(1)) # 공백시 제일 마지막 값음 꺼냄
print(arr) # 8이 없어짐 ~

## 리스트컴프리핸션 # 대량의 리스트를 쉽게 생성하는 방법
arr = [i for i in range(1, 100 + 1)]
print(arr)

sum = 0
for i in arr:
    sum = sum + i #################### 뭔말 ?

print(f'{len(arr)}까지의 합산은, {sum}입니다.')

