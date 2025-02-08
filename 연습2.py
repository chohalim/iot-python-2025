listSimple = [1,2,3,4,5,6,7,8,9,10] # 반복

print(f'합산결과는 {sum(listSimple)}이다.')

# for i in listSimple: # for 변수 in 반복대상
    # print(f'합산결과 = {i}')

sum = 0 ####### list의 값을 다 더하는 거 ~
for i in listSimple:
    sum = sum + i # sum += i


print(f'합산결과 = {sum}')




class Car:
    # __new__(사용빈도 낮음), __init__(많이 사용)
    ## Car() 호출하면 아래의 메서드가 실행
    ## company, name, plateNumber 모를 때는 None
    def __init__(self, company=None, name=None, plateNumber=None):
        self.__company = company # 멤버변수 이름 앞 __ : 외부접근 불가
        self.__name = name
        self.__plateNumber = plateNumber
        print ('Car 클래스를 새로 생성!')

# 클래스 자체가 출력되는데, __str__ 문자열로 출력되도록 바꿔줌
    def __str__(self): ################# __str__은 class에서만 사용 ?
        return f'제 차는 {self.__name}이고, 차번호는 {self.__plateNumber}입니다.'
    
    # 외부에서 잘못 된 차번호를 넣으면 안들어감
    def setPlateNumber(self, newPlateNumber):
        if type(newPlateNumber) is str: # 문자열만 들어갈 수 있도록
            self.__plateNumber = newPlateNumber

    def setName(self, newName = '글쎄요'): # 이름을 모를때
        self.__name = newName


myCar = Car('현대', '아이오닉', '54라9537') # ()넣으면 None 출력됨
# myCar = Car(name='아이오닉', plateNumber='54라9537', company='현대')
myCar.setName('하림') # 빈칸일 경우 글쎄요가 출력됨
print(myCar)

myCar.__plateNumber = 2018 # 2018 숫자열 print되지 않음
print(myCar) ########################## Car 클래스 새로 생성! 반복되지 않는 이유 ?

myCar.setPlateNumber('2025') # 2025가 문자열로 들어가서 가능
print(myCar) 