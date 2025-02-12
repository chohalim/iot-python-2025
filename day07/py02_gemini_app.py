# py02_gemini_app.py
# TKinter 클래스화 # 객체지향 형식 !!!! (class)

from tkinter import * 
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE') 
model = genai.GenerativeModel('gemini-1.5-flash')

class window(Tk): # 원래는 window: #window(Tk): 는 Tk를 상속받는다
    def __init__(self):
        super().__init__() # 부모객체도 같이 초기화 # 오버라이딩, 부모 클래스 재정의???????
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        # 클래스 작업할 땐 self 유심히
        self.iconbitmap('./chatbot.ico') 
        self.protocol('AIzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE', self.onClosing)

        # self.initWindow()
       

        # def initWindow(self): # 이거 안해도 됨, 구분하기 편하라고
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD)

        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF') # '#EFEFEF' 연한회색
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=75, height=1, wrap=WORD, 
                                font=self.myFont)
        self.textMessage.bind('<Key>', self.keypress) ## ?????
        self.textMessage.pack(side=LEFT, padx=15)

        self.bottonSend = Button(self.inputFrame, text='전송', bg='green', fg='white',
                    font=self.myFont,
                    command=self.responseMessage)
        self.bottonSend.pack(side=RIGHT, padx=20, pady=5) 

        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont) # '#0000000'='black' ###### root에 위치?
        self.textResult.pack(fill=BOTH, expand=True) 

        # self.textResult.tag_configure('user', font=boldFont, foreground='yellow') # 글자 굵게, 노란색으로 # slant=ITALIC?????????
        # self.textResult.tag_configure('ai', font=boldFont, foreground='limegreen') 
        # self.textResult.tag_configure('error', font=boldFont, foreground='red') 


    # 나머지 부분 복사

    def responseMessage(self):
        #   showinfo('동작',f'이제 API를 호출하면 됩니다!\n{self.textMessage.get("1.0", END)}')
        self.inputText = self.textMessage.get('1.0', END).replace('\n','').strip() # 자동줄바꿈, 띄움 없애기
        print(self.inputText)
        self.textMessage.delete('1.0', END)

        if self.inputText:
            try:
                ai_response = model.generate_content(self.inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n\n', 'ai')
            except Exception as e:
                self.textResult.insert(END, f'{response}\n\n', 'error')
            finally:
                self.textResult.see(END)

              
    def keypress(self, event):
        if event.char == '\r': ######## 티킨터는 \r 사용?????
            self.responseMessage()

    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?'): # askokcancel
            self.destroy() # 완전 종료



if __name__ == '__main__':
   print('Tkinter 클래스 시작!')
   app = window() # Tkinter 클래스 객체 생성
   app.mainloop()

    
