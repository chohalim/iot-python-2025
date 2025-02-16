from tkinter import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import * 

from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE')
model = genai.GenerativeModel('gemini-1.5-flash')



def responseM():
    inputT = textMessage.get('1.0',END).replace('\n','').strip()
    print(inputT)
    textMessage.delete('1.0',END)
    
    if inputT:
        try:
            textR.insert(END, '유저: ', BOLD)
            textR.insert(END, f'{inputT}\n\n','user')

            ai_r = model.generate_content(inputT)
            response = ai_r.text

            textR.insert(END,'챗봇: ', 'bold')
            textR.insert(END,f'{response}\n\n', 'ai')

            textR.see(END)
        except Exception:
            textR.see(END)
        finally:
            textR.see(END)

def keypress(event):
    if event.char == '\r':
        responseM()

            

root = Tk()
root.title('하림 연습')
root.geometry('730x450')

myfont = Font(family='NanumGothic', size=10)
boldfont = Font(family='NanumGothic', size=10, weight=BOLD)

inputFrame = Frame(root, width=730, height=30, bg='black')
inputFrame.pack(side=BOTTOM, fill=BOTH) # fill=BOTH 는 화면창이 넓어져도 채워지는 것

textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myfont)
textMessage.bind('<Key>', keypress) 
textMessage.pack(side=LEFT, padx=15)

buttonS = Button(inputFrame, text='전송', bg='pink',fg='white',font=myfont, command=responseM)
buttonS.pack(side=RIGHT, padx=20, pady=5)


textR = ScrolledText(root, wrap=WORD, bg='white', fg='#000000', font=myfont)
textR.pack(fill=BOTH, expand=True)

textR.tag_configure('user', font=boldfont, foreground='yellow') # 글자 굵게, 노란색으로 # slant=ITALIC?????????
textR.tag_configure('ai', font=boldfont, foreground='limegreen') 

textMessage.focus_set()

root.mainloop()