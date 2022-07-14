from tkinter import *
#윈도우 설정
root = Tk()
root.title("Calculator")
root.geometry("350x480")

#프레임 설정
up_frame = Frame(root, width=400, height=70)
up_frame.pack(pady=40)
 
dn_frame = Frame(root, width=400, height=100)
dn_frame.pack(padx=10, pady=10)
 #계산 받는 곳 설정
entry = Entry(up_frame, width=20, font=("Courier",18), borderwidth=4)
entry.pack()
entry.insert(0,"")

current=' ' #변수 초기 값

def operate(op): #기호 함수
    global current #변수 지역->전역변수로 맞추기
    current = entry.get() #실시간 변수 입력
    entry.delete(0,END)

    if op=='C':
        entry.delete(0,END)
        current=entry.get() #실시간 변수 입력
    elif op=='^':
        current+='**'
    else:
        entry.insert(0, str(current)+op) #entry 칸에 내가 쓴 수식 써주기

def btn_click(num) : #숫자 함수
    global current
    current = str(entry.get()) #실시간 변수 입력
    entry.delete(0,END)
    entry.insert(0, str(current)+num) #entry 칸에 내가 쓴 수식 써주기
    current = str(entry.get()) #실시간 변수 입력
def answer(an='='): #답 함수
    global current
    a=entry.get()
    entry.delete(0,END)
        
    print(a) #내가 쓴 수식 idle에 써놔주기
    entry.insert(0,str(eval(a))) #eval 함수를 통하여 문자열을 수식 그대로 계산해주기
    current=str(eval(a)) #실시간 변수 입력




def del_(d='del'):
    global current
    b=list(current)
    b.pop()
    #리스트 함수를 통하여 하나씩 지우기
    current=''.join(b) #리스트 합치기
    entry.delete(0,END)
    entry.insert(0,str(current))
#버튼 배치
btn = Button(dn_frame,text='7',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('7'))#람다 함수를 통하여 버튼 클릭시 위에 있는 함수 사용
btn.grid(column=0, row=0, padx=5, pady=5)
btn = Button(dn_frame,text='8',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('8'))
btn.grid(column=1, row=0, padx=5, pady=5)
btn = Button(dn_frame,text='9',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('9'))
btn.grid(column=2, row=0, padx=5, pady=5)
btn = Button(dn_frame,text='+',padx=15,pady=10,font=("Courier",15),command=lambda: operate('+'))
btn.grid(column=3, row=0, padx=5, pady=5)
btn = Button(dn_frame,text='^',padx=15,pady=10,font=("Courier",15),command=lambda: operate('**'))
btn.grid(column=0, row=4, padx=5, pady=5)

btn = Button(dn_frame,text='4',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('4'))
btn.grid(column=0, row=1, padx=5, pady=5)
btn = Button(dn_frame,text='5',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('5'))
btn.grid(column=1, row=1, padx=5, pady=5)
btn = Button(dn_frame,text='6',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('6'))
btn.grid(column=2, row=1, padx=5, pady=5)
btn = Button(dn_frame,text='00',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('00'))
btn.grid(column=1, row=4, padx=5, pady=5)
btn = Button(dn_frame,text='-',padx=15,pady=10,font=("Courier",15),command=lambda: operate('-'))
btn.grid(column=3, row=1, padx=5, pady=5)

btn = Button(dn_frame,text='1',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('1'))
btn.grid(column=0, row=2, padx=5, pady=5)
btn = Button(dn_frame,text='2',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('2'))
btn.grid(column=1, row=2, padx=5, pady=5)
btn = Button(dn_frame,text='3',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('3'))
btn.grid(column=2, row=2, padx=5, pady=5)
btn = Button(dn_frame,text='*',padx=15,pady=10,font=("Courier",15),command=lambda: operate('*'))
btn.grid(column=3, row=2, padx=5, pady=5)

btn = Button(dn_frame,text='.',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('.'))
btn.grid(column=0, row=3, padx=5, pady=5)
btn = Button(dn_frame,text='0',padx=15,pady=10,font=("Courier",15),command=lambda: btn_click('0'))
btn.grid(column=1, row=3, padx=5, pady=5)
btn = Button(dn_frame,text='C',padx=15,pady=10,font=("Courier",15),command=lambda: operate('C'))
btn.grid(column=2, row=3, padx=5, pady=5)
btn = Button(dn_frame,text='÷',padx=15,pady=10,font=("Courier",15),command=lambda: operate('/'))
btn.grid(column=3, row=3, padx=5, pady=5)
btn = Button(dn_frame,text='=',padx=15,pady=10,font=("Courier",15),command=lambda: answer('='))
btn.grid(column=3, row=4, padx=5, pady=5)
btn = Button(dn_frame,text='del',padx=15,pady=10,font=("Courier",15),command=lambda: del_('del'))
btn.grid(column=2, row=4, padx=5, pady=5)

root.mainloop()