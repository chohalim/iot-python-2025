# py04_module.py

# 수학모듈 : 수학함수들이 모여있는 파이썬 모듈
import math

print(math.pi)

PI = 3.141592
# 2 ** 10 -> int # float
print(math.pow(2,10)) # 제곱근
print(math.sqrt(4)) # 루트
print(math.log2(2))

import random

# 초간단 로또(중복됨)
numbers = [i for i in range(1, 45 + 1)]
result = []

for i in range(6): # 6번 반복 # == for i in range(1,7):
    result.append(random.choice(numbers))

print(result)

# 2번째 방법
random.shuffle(numbers) # 셔플 : 섞는다

result = random.choices(numbers, k=6)
print(result)
