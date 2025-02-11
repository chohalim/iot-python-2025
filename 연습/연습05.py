from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *

import google.generativeai as genai

# 6. 제미나이 API용 구성 
genai.configure(api_key='AIzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE') 
model = genai.GenerativeModel('gemini-1.5-flash')


def responseMessage(): # '1.0', END?????????????
    inputText = textMessage.get('1.0', END).replace('\n','').strip() 
    print(inputText)
    textMessage.delete('1.0', END) 
    if inputText:
        try:
            textResult.insert(END, '유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아규먼트

            ai_response = model.generate_content(inputText)
            response = ai_response.text
            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 태그

            textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운
        except Exception as e:
            textResult.insert(END, f'{response}\n\n', 'error')
        finally:
            textResult.see(END)


   

root = Tk() 
root.title('제미나이 챗봇')
root.geometry('730x450')

myFont = Font(family='NanumGothic', size=10)

textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myFont) # '#0000000'='black' ###### root에 위치?
textResult.pack(fill=BOTH, expand=True) # fg='white' fill=BOTH, expand=True ???

inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF') # 루트는 인자, 루트는 티케이를 따르고, 프레임은 티킨터X?
inputFrame.pack(side=BOTTOM, fill=BOTH) 

textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont)

textMessage.pack(side=LEFT, padx=40) # 검색창을 왼쪽으로 양옆 40 띄우고 

bottonSend = Button(inputFrame, text='전송', bg='green', fg='white', command=responseMessage) 
bottonSend.pack(side=RIGHT, padx=30, pady=5) # 전송버튼을 설정

root.mainloop()