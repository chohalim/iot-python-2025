# py04_module.py

# 수학모듈 : 수학함수들이 모여있는 파이썬 모듈
import math

print(math.pi)

PI = 3.141592
# 2 ** 10 -> int
print(math.pow(2,10)) # float
print(math.sqrt(4))
print(math.log2(2))

import random

# 초간단 로또(중복됨)
numbers = [i for i in range(1, 45 + 1)]
result = []

for i in range(6): # 6번 반복
    result.append(random.choice(numbers))

print(result)

# 한꺼번에 여섯개를 추출하는 방법(중복됨)
numbers = weight = list(range(1, 45 + 1)) # weight : 가중치
random.shuffle(weight) # 셔플 : 섞는다

result = random.choices(numbers, weights=weight, k=6)
print(result)
