# py01_gpt_clone.py
# 

from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수들을 다 쓰겠다(용량 많아짐)

# 1. 메인 윈도우 생성, 초기 설정
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')

# 2. UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='gray')
inputFrame.pack(side=BOTTOM)

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, hight=1, wrap=WORD) # wrap=WORD 글자수대로 자동 줄바꿈
textMessage.pack(side=LEFT)

bottonSend = Button(inputFrame, text='전송', bg='green', fg='white')
bottonSend.pack(side=RIGHT)



# 1. 종료시까지 계속 실행
root.mainloop()
