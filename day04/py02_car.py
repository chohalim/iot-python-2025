# py02_car .py

# 객체지향 다시
class Car:
    # __new__(사용빈도 낮음), __init__(많이 사용)
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를 때는 None # None 생략가능
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company # 멤버변수 이름 앞 __ : 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print('Car 클래스를 새로 생성!')

# 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self):
        return f'제 차는 {self.__name}이고, 차번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘못 된 차번호를 넣으면 안들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str: # 문자열만 들어갈 수 있도록
            self.__plateNumber = newPlateNumber
    
    # yourCar
    def setName(self, newName = '글쎄요'): # 이름을 모를때
        self.__name = newName

    def getname(self):
        return self.__name

# myCar = Car('현대', '아이오닉', '54라9537')
# 파라미터명 = 값 으로 매개변수 순서를 변경가능
myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대')
myCar.setName('아이오닉') # 빈칸일 경우 글쎄요가 출력됨
print(myCar)


# myCar.__plateNumber = 2018 # 2018 숫자열 print되지 않음
# print(myCar)

# myCar.setPlateNumber('2025') # 2025가 문자열로 들어가서 가능
# print(myCar) 

# yourCar
yourCar = Car()
print(yourCar)
yourCar.setPlateNumber('11나2222')
print(yourCar)
yourCar.setName()
print(yourCar)

