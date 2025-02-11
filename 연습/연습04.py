from tkinter import * # tkinter 모듈에 있는 대다수의 클래스, 함수, 변수들을 다 쓰겠다(용량 많아짐)
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음

from tkinter.font import *


def responseMessage():
    inputText = textMessage.get('1.0', END).replace('\n','').strip() 
    print(inputText)
    textMessage.delete('1.0', END)

root = Tk() # Tk는 티킨터 ?
root.title('제미나이 챗봇')
root.geometry('730x450')

myFont = Font(family='NanumGothic', size=10)

# 2. UI화면 구성
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF') # , width=730, height=30, bg='#EFEFEF' 없어도 똑같은데 ??
inputFrame.pack(side=BOTTOM, fill=BOTH) # side=BOTTOM, fill=BOTH 무슨 뜻 ??

textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)

textMessage.pack(side=LEFT, padx=15)

bottonSend = Button(inputFrame, text='전송', bg='green', fg='white', command=responseMessage) 
bottonSend.pack(side=RIGHT, padx=20, pady=5)

root.mainloop()

