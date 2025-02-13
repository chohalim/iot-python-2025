# 4.  입력한 수를 거꾸로 출력하는 프로그램을 구현하세요.
# 예 1 3 5 7 9 --> 9 7 5 3 1

# x = input('거꾸로 출력할 숫자를 입력하시오 >').split()
# x의 순서를 바꾸는 방법
# y = x
# print(y)
# 수를 리스트로 하고
# 리스트의 순서를 바꾸게해라

# for i in x:
    # print(i,end='')
# print()

# 5. SmartPhone 이라는 클래스를 만들고, 객체를 생성해서 phoneOwner, phoneNumber, company 등의 
# 멤버변수(속성)을 가지도록 만드세요.(본인이 다른 기능을 좀 더 추가하여도 무방합니다)

class SmartPhone:
    def __init__(self, phoneOwner, phoneNumber, company):
        self.phoneOwner = phoneOwner
        self.phoneNumber = phoneNumber
        self.company = company

    def __str__(self):
        retStr = (f'제 이름은 {self.phoneOwner}이고, 제 번호는 {self.phoneNumber}입니다.') 
        return retStr 
    
    # 번호가 뭐야 ?
    # 내 번호는 뭐야로 답하게
    def hunting(self):
        print(f'내 번호는 {self.phoneNumber}야.')

girl = SmartPhone('하림', '010-8854-8451', '아이폰')
print('너 번호가 뭐야?')
girl.hunting()
print('자기소개 해주세요.')
print(girl)



