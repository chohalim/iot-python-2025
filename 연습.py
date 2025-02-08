def say_hi():
    print('안녕~')

say_hi()

def say_hello(name):
    print(f'{name}야, 안녕!')

say_hello('하림')

# def get_age(birthYear): # 함수(약자):
    # age = 2025 - birthYear  # 조건
    # print(f'{age}') # 출력
    # return age # return 결과를 가지고 호출한 위치로

# get_age(12) # 함수(수(약자))

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def real_name(self):
        print(f'내 이름은 {self.name}')

    def bone_year(self):
        real = 2025- self.age
        return real
        # print(f'출생년도는 {real}')

    def real_age(self,age):
        print(f'{self.name}의 원래 나이는?')
        print(f'우린 {self.age}로 알고 있었어')
        self.age = age
        print(f'그녀는 사실 {self.age}살 이야')
    

girl = person('하림',27)
girl.real_name()
girl.bone_year()
girl.real_age(30)
print(f'{girl.name}의 나이는 {girl.age}')
print(f'출생년도는 {girl.bone_year()}야')
print(f'{girl.name}의 출생년도는 {girl.bone_year()}')

class Person:

    def __init__(self, name, age, weihgt, gender):
        self.name = name
        self.age = age
        self.weight = weihgt
        self.gender = gender

    def __str__(self):
        retStr = f'{self.name}\n{self.age}\n{self.weight}\n{self.gender}'       
        return retStr   
    
    def setWeight(self, weight):
        print(f'{self.name}의 몸무게가 변경됩니다.')
        print(f'현재 {self.weight}kg')
        self.weight = weight
        print(f'변경 후 {self.weight}kg')

man = Person('명건', 50, 70.5, 'man')
man.setWeight(80.1)
print(man)

