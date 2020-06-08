import sys
import tkinter
import sqlite3
con = sqlite3.connect("ScheduleDB")
cur = con.cursor()
#cur.execute("CREATE TABLE userTable(SC_date TEXT, SC_name TEXT, SC_hour TEXT, SC_min TEXT, SC_detail TEXT)")

from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
from PyQt5.QtCore import QDate, Qt

class MyApp(QWidget):       #달력 출력 클래스

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        count=0
        global cal
        cal = QCalendarWidget(self)  #달력
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(function)  #

        self.makebrown()

        self.lbl = QLabel(self)
        date = cal.selectedDate()  #날짜
        self.lbl.setText(date.toString(Qt.DefaultLocaleLongDate))

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl)
        vbox.addWidget(cal)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def makebrown(self):

        daydate = []
        cur.execute("SELECT *FROM userTable")
        row = cur.fetchall()
        daydate = [0 for i in range(len(row))]
        i = 0
        while i < len(row):
            daydate[i] = str(row[i][0])
            i = i + 1
        color = ['#bf5b17']
        fm = QTextCharFormat()
        fm.setBackground(QColor(color[0]))

        for d_day in daydate:
            d_day2 = QDate.fromString(d_day, "yyyy년MM월dd일")
            cal.setDateTextFormat(d_day2, fm)

def showDB(date):
    hour = ['', '', '', '', '']  #DB에서 시간 받아옴
    min = ['', '', '', '', '']  #DB에서 분 받아옴
    detail = ['', '', '', '', '']  #DB에서 내용 받아옴
    day = ['', '', '', '', '']  #DB에서 날짜 받아옴
    name = ['', '', '', '', '']  #DB에서 이름 받아옴
    re = ["","","","",""]  #DB에서 받은 정보 모음
    while(True):
        i=0
        cur.execute("SELECT * FROM userTable WHERE userTable.SC_date =='%s'" % date.toString('yyyy년MM월dd일'))
        row=cur.fetchall()
        while i < len(row):
            day[i]=str(row[i][0])
            name[i]=str(row[i][1])
            hour[i]=str(row[i][2])
            min[i]=str(row[i][3])
            detail[i]=str(row[i][4])
            re[i]=(day[i],name[i],hour[i],min[i],detail[i])
            i=i+1
        break;
    return re

def function(date):

        def StartSC(event):
            Schedule(date)

        def close(event):
            window.destroy()

        def printed(event):
            print(help)

        def deleteSC0(event):  #선택된 데이터 삭제
            de_detail=text[0]
            cur.execute("DELETE FROM usertable WHERE SC_detail = ?", (de_detail[4],))
            con.commit()
            a = MyApp()
            a.initUI().repaint()

        def deleteSC1(event):
            de_detail=text[1]
            cur.execute("DELETE FROM usertable WHERE SC_detail = ?", (de_detail[4],))
            con.commit()
            a = MyApp()
            a.initUI().repaint()

        def deleteSC2(event):
            de_detail=text[2]
            cur.execute("DELETE FROM usertable WHERE SC_detail = ?", (de_detail[4],))
            con.commit()
            a = MyApp()
            a.initUI().repaint()

        def deleteSC3(event):
            de_detail = text[3]
            cur.execute("DELETE FROM usertable WHERE SC_detail = ?", (de_detail[4],))
            con.commit()
            a = MyApp()
            a.initUI().repaint()

        def deleteSC4(event):
            de_detail=text[4]
            cur.execute("DELETE FROM usertable WHERE SC_detail = ?", (de_detail[4],))
            con.commit()
            a = MyApp()
            a.initUI().repaint()

        def updateSC0(event): #선택된 데이터 수정
            de_detail=text[0]
            Modify(date,de_detail)

        def updateSC1(event):
            de_detail=text[1]
            Modify(date,de_detail)

        def updateSC2(event):
            de_detail=text[2]
            Modify(date,de_detail)

        def updateSC3(event):
            de_detail=text[3]
            Modify(date,de_detail)

        def updateSC4(event):
            de_detail=text[4]
            Modify(date,de_detail)

        global text  # DB에서 받아온 데이터 저장
        text = showDB(date)

        window = Tk()
        window.title("일정 보기")
        window.geometry("350x200+100+100")
        window.resizable(False, False)

        #일정이 있으면 출력
        label=Label(window, text= '이름           ' + '시간           ' + '내용'+'                            '+'<최대 5개>')
        label.place(x=0,y=0,)
        line= Label(window,text='-------------------------------------------------------------------')
        line.place(x=0,y=17)
        if text[0] != '':
            label_0 = Label(window, text=text[0][1] + '          '+ text[0][2]+': '+text[0][3]+'         '+text[0][4])
            label_0.place(x=0, y=40+30*0)
            button0_1= Button(window,width=3, text="수정")
            button0_2= Button(window,width=3,text="삭제")
            button0_1.bind("<Button-1>", updateSC0)
            button0_2.bind("<Button-1>",deleteSC0)
            button0_1.place(x=280, y=40 + 30 * 0)
            button0_2.place(x=315, y=40 + 30 * 0)
        if text[1] != '':
            label_1 = Label(window, width=20, text=text[1][1] + '          '+ text[1][2] + '시 ' + text[1][3] + '분' +'         ' + text[1][4])
            label_1.place(x=0, y=40 + 30 * 1)
            button1_1 = Button(window, width=5, text="수정")
            button1_2 = Button(window, width=5, text="삭제")
            button1_1.place(x=280, y=40 + 30 * 1)
            button1_2.place(x=315, y=20 + 30 * 1)
            button1_1.bind("<Button-1>", updateSC1)
            button1_2.bind("<Button-1>", deleteSC1)
        if text[2] != '':
            labe_2 = Label(window, width=20, text=text[2][1] +'          '+ text[2][2] + '시 ' + text[2][3] + '분' +'         ' + text[2][4])
            labe_2.place(x=0, y=40 + 30 * 2)
            button2_1 = Button(window, width=5, text="수정")
            button2_2 = Button(window, width=5, text="삭제")
            button2_1.place(x=280, y=40 + 30 * 2)
            button2_2.place(x=315, y=40 + 30 * 2)
            button2_1.bind("<Button-1>", updateSC2)
            button2_2.bind("<Button-1>", deleteSC2)
        if text[3] != '':
            label_3 = Label(window, width=20, text=text[3][1] +'          '+ text[3][2] + '시 ' + text[3][3] + '분' +'         '+ text[3][4])
            label_3.place(x=0, y=40 + 30 * 3)
            button3_1 = Button(window, width=5, text="수정")
            button3_2 = Button(window, width=5, text="삭제")
            button3_1.place(x=280, y=40 + 30 * 3)
            button3_2.place(x=315, y=40 + 30 * 3)
            button3_1.bind("<Button-1>", updateSC3)
            button3_2.bind("<Button-1>", deleteSC3)
        if text[4] != '':
            label_4 = Label(window, width=20, text=text[4][1]+'          '+text[4][2] + '시 ' + text[4][3] + '분' + '     ' + text[4][4])
            label_4.place(x=0, y=40 + 30 * 3)
            button4_1 = Button(window, width=5, text="수정")
            button4_2 = Button(window, width=5, text="삭제")
            button4_1.place(x=280, y=40 + 30 * 3)
            button4_2.place(x=315, y=40 + 30 * 3)
            button4_1.bind("<Button-1>", updateSC4)
            button4_2.bind("<Button-1>", deleteSC4)


        button1 = Button(window, width = 20,text="저장")  #저장 버튼
        button1.place(x=10, y=170)
        button1.bind("<Button-1>",StartSC)  #, self.setWindowTitle('QCalendarWidget')
        button2 = Button(window, width = 20, text="취소")  #취소 버튼
        button2.place(x=190, y=170)
        button2.bind("<Button-1>", close)
        window.mainloop()

def Modify(date,list):
        win = Tk()
        win.title("일정 수정")
        win.geometry("200x250+300+300")
        win.resizable(False, False)
        label = Label(win, font=(30), text=date.toString(Qt.DefaultLocaleLongDate))
        label.place(x=20, y=10)

        def updateDB():  # DB에 일정 추가
            DB_date = str(date.toString('yyyy년MM월dd일'))  # DB에 넣을 날짜 저장
            DB_name = str(input1.get())  # DB에 넣을 이름 저장
            DB_hour = str(c_hour.get())  # DB에 넣을 시간 저장
            DB_min = str(c_mins.get())  # DB에 넣을 시간 저장
            DB_detail = str(input2.get())  # DB에 넣을 내용 저장
            cur.execute("UPDATE usertable SET SC_date = ?, SC_name= ?, SC_hour = ?, SC_min = ?, SC_detail = ?", (DB_date, DB_name, DB_hour, DB_min, DB_detail))
            con.commit()
            win.destroy()
            a=MyApp()
            a.initUI().repaint()

        def close(event):
            win.destroy()

        label1 = Label(win, text='일정')
        label1.place(x=00, y=50)
        input1 = Entry(win)
        input1.insert(0,list[1])
        input1.place(x=30, y=50)

        label1 = Label(win, text='시간')
        label1.place(x=00, y=80)

        hours = [i for i in range(00, 24)]
        mins = [j for j in range(0, 60)]

        c_hour = ttk.Combobox(win, width=2, height=10, value=hours)
        c_hour.place(x=40, y=80)
        c_hour.set(list[2])
        label3 = Label(win, text='시')
        label3.place(x=80, y=80)
        c_mins = ttk.Combobox(win, width=2, height=15, value=mins)
        c_mins.place(x=100, y=80)
        c_mins.set(list[3])
        label4 = Label(win, text='분')
        label4.place(x=140, y=80)

        label2 = Label(win, text='내용')
        label2.place(x=00, y=110)
        input2 = Entry(win)
        input2.insert(0,list[4])
        input2.place(x=30, y=110, height=80)

        button = Button(win, text="저장", command=updateDB)
        button.place(x=50, y=220)
        button1 = Button(win, text="취소")
        button1.place(x=110, y=220)
        button1.bind("<Button-1>", close)
        win.mainloop()

def Schedule(date):  #캘린더에 일정 추가
        win = Tk()
        win.title("일정 관리")
        win.geometry("200x250+300+300")
        win.resizable(False, False)
        label=Label(win,font=(30),text=date.toString(Qt.DefaultLocaleLongDate))
        label.place(x=20,y=10)

        def goDB():     #DB에 일정 추가
            DB_date=str(date.toString('yyyy년MM월dd일'))  #DB에 넣을 날짜 저장
            DB_name = str(input1.get())    #DB에 넣을 이름 저장
            DB_hour = str(c_hour.get())   #DB에 넣을 시간 저장
            DB_min = str(c_mins.get())    #DB에 넣을 시간 저장
            DB_detail = str(input2.get())   #DB에 넣을 내용 저장
            cur.execute("INSERT INTO userTable VALUES('"+DB_date+"', '"+DB_name+"', '"+DB_hour+"', '"+DB_min+"', '"+DB_detail+"')")
            con.commit()
            win.destroy()
            a = MyApp()
            a.initUI().repaint()

        def close(event):
            win.destroy()

        label1=Label(win,text='일정')
        label1.place(x=00,y=50)
        input1=Entry(win)
        input1.place(x=30,y=50)

        label1 = Label(win, text='시간')
        label1.place(x=00, y=80)

        hours=[i for i in range(00,24)]
        mins=[j for j in range(0,60)]

        c_hour=ttk.Combobox(win,width=4,height=10,value=hours)
        c_hour.place(x=32,y=80)
        c_hour.set("시")
        label3= Label(win,text='시')
        label3.place(x=85, y=80)
        c_mins=ttk.Combobox(win,width=4,height=15,value=mins)
        c_mins.place(x=105,y=80)
        c_mins.set("분")
        label4 = Label(win, text='분')
        label4.place(x=157, y=80)

        label2 = Label(win, text='내용')
        label2.place(x=00, y=110)
        input2 = Entry(win)
        input2.place(x=30, y=110,height=80)

        button = Button(win, width = 10, text="저장", command=goDB )
        button.place(x=13,y=220)
        button1 = Button(win, width = 10, text="취소")
        button1.place(x=98, y=220)
        button1.bind("<Button-1>", close)
        win.mainloop()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
    con.close()