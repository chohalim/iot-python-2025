# py01_gpt_clone.py
# GUI를 위한 모듈 # 절차적 형식 !!!

from tkinter import * # tkinter 모듈에 있는 대다수의 클래스, 함수, 변수들을 다 쓰겠다(용량 많아짐)
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import * # 5번을 위한

# 7. 폰트를 위한 모듈
from tkinter.font import *


# 6. 제미나이를 위한 모듈
import google.generativeai as genai

# 6. 제미나이 API용 구성
# configure(환경을 설정하다)-컴파일(번역) 하기 직전에 라이브러리에 존재여부를 확인하고 연결시킨다 
genai.configure(api_key='AIzaSyBPuAhm1CP6pMLsk9UioATjQVKTbbrq8dE')
model = genai.GenerativeModel('gemini-1.5-flash')

# 4. 전송버튼 이벤트, 제미나이 실행 포함
def responseMessage():
    # showinfo('실행', 'API를 실행합니다!') # .replace('\n','').strip() 줄바꿈을 두번하는 이유 ?????
    inputText = textMessage.get('1.0', END).replace('\n','').strip() # 자동줄바꿈, 띄움 없애기
    print(inputText)
    textMessage.delete('1.0', END) # 입력하고 전송한 후에 글이 지워지도록
    # showinfo('결과', inputText) # 다이얼로그, 모달(Modal)창 - 제어권을 갖는 창 <-> 모달리스트

    if inputText:
        try:
            textResult.insert(END,'유저: ', BOLD)
            textResult.insert(END, f'{inputText}\n\n', 'user') 

            ai_response = model.generate_content(inputText) # generate_content??
            response = ai_response.text

            textResult.insert(END, '챗봇: ', 'bold')
            textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 태그

            textResult.see(END) # 스크롤텍스트 마지막 위치로 스크롤 다운
        except Exception as e:
            textResult.insert(END, f'{response}\n\n', 'error')
        finally:
            textResult.see(END)

# 8. textMessage 위젯에서 엔터를 치면 전송버튼이 클릭 
def keypress(event):
    # print(repr(event.char)) # repr을 안쓰면 \r, \x80 표시 안됨
    # \r(캐리지 리턴), \n(뉴라인) # 혼용해서 사용 \r\n, \r, \n
    if event.char == '\r': 
        responseMessage()

#11. 종료시 이벤트처리 함수
def onClosing():
    if askyesno('종료확인', '종료하시겠습니까?'): # askokcancel
        root.destroy() # 완전 종료

# 1. 메인 윈도우 생성, 초기 설정
root = Tk()
root.title('제미나이 챗봇')
root.geometry('730x450')
# 12. 아이콘 변경
root.iconbitmap('./image/chatbot.ico') # 파이썬인스톨러로 설치할 땐 해당폴더에 복사하고 

# 7. 전체에서 사용할 폰트 지정 -> 나눔고딕 
myFont = Font(family='NanumGothic', size=10)
boldFont = Font(family='NanumGothic', size=10, weight=BOLD)

# 2. UI화면 구성 
inputFrame = Frame(root, width=730, height=30, bg='#EFEFEF') # root, width=730, height=30, bg='#EFEFEF' 없어도 같은 결과인디 ?
inputFrame.pack(side=BOTTOM, fill=BOTH)

# 3. inputFrame에 들어갈 Entry와 Button 구성
textMessage = Text(inputFrame, width=75, height=1, wrap=WORD, font=myFont) # wrap=WORD 글자수대로 자동 줄바꿈
# 8.  입력창에서 엔터를 치면 keypress 이벤트처리함수 발생
textMessage.bind('<Key>', keypress)

textMessage.pack(side=LEFT, padx=15)


bottonSend = Button(inputFrame, text='전송', bg='green', fg='white', font=myFont, command=responseMessage) ###### 폰트 커맨드 앞에?
bottonSend.pack(side=RIGHT, padx=20, pady=5) # padx=20 양옆으로, pady=5 아래위로

# 5. API호출 결과메세지가 출력 될 스크롤 기능 텍스트 위젯
textResult = ScrolledText(root, wrap=WORD, bg='#000000', fg='white', font=myFont) # '#0000000'='black' ###### root에 위치?
textResult.pack(fill=BOTH, expand=True) 

# 10. 스크롤텍스트에 나올 메시지 디자인
textResult.tag_configure('user', font=boldFont, foreground='yellow') # 글자 굵게, 노란색으로 # slant=ITALIC?????????
textResult.tag_configure('ai', font=boldFont, foreground='limegreen') 
textResult.tag_configure('error', font=boldFont, foreground='red') 

# 9. 실행 후 바로 입력창에 포커스가 가도록
textMessage.focus_set()

# 11. 종료버튼(x) 누르면 종료메세지 확인 후 종료
root.protocol('WM_DELETE_WINDOW', onClosing)

# 1. 종료시까지 계속 실행
root.mainloop()
