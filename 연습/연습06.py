from tkinter import * # import 불러오다
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from tkinter.font import *

import google.generativeai as genai # generativeai -> ai를 생성한다


genai.configure(api_key='IzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE') # cofigure 환경을 설정하다
model = genai.GenerativeModel('gemini-1.5-flash')

def responseMessage():
    inputText = textMessage.get('1.0', END).replace('\n','').strip() #####'1.0', END?????? # .strip() 
    print(inputText)
    textMessage.delete('1.0', END)

    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n','user')

            ai_response = model.generate_content(inputText) # generate_content??
            response = ai_response.text

            textResult.insert(END, '챗봇: ', BOLD)
            textResult.insert(END, f'{response}\n\n', 'ai')

            textResult.see(END)

        except Exception as e:
            textResult.insert(END, f'{response}\n\n', 'error')
        finally:
            textResult.see(END)


def keypress(event):
    if event.char == '\r': 
        responseMessage()

root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450') # geometry 기하학 구조

myFont = Font(family='NanumGothic', size=10) # 폰트는 화면에서 할거니까 화면을 구성하고 ~
boldFont = Font(family='NanumGothic', size=10, weight=BOLD)

inputFrame = Frame(root, width=730, height=30, bg='black') # root 넣는 이유 ???
inputFrame.pack(side=BOTTOM, fill=BOTH)

textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)
textMessage.bind('<Key>', keypress)
textMessage.pack(side=LEFT, padx=15)

bottonSend = Button(inputFrame, text='전송', bg='green',fg='white',font=myFont, command=responseMessage)
bottonSend.pack(side=RIGHT, padx=20, pady=5)

textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myFont) # '#0000000'='black' ###### root에 위치?
textResult.pack(fill=BOTH, expand=True)

textResult.tag_configure('user', font=boldFont, foreground='yellow') # 글자 굵게, 노란색으로 # slant=ITALIC?????????
textResult.tag_configure('ai', font=boldFont, foreground='limegreen') 
textResult.tag_configure('error', font=boldFont, foreground='red') 

textMessage.focus_set()


root.mainloop() # mainloop 꺼지지 않고 창이 계속 켜져있게 하는 것