from tkinter.simpledialog import *

win = tkinter.Tk()
win.title("M_delete")
output = tkinter.Tk()
output.title('M_delete_output')
#设置大写和位置
win.geometry("400x400+200+50")
output.geometry("400x400+200+50")

lb = Text(win)
op = Text(output)
lb.pack()
op.pack()
lb.insert('1.0','请输入文字：\n')
op.insert('1.0','更新后内容：\n \n')
def getTextInput():
    result=lb.get("2.0","end")    #获取文本输入框的内容
    n_data = result.replace('\n','')
    print('\n')
    op.insert('3.0',n_data)  

btnRead=Button(win, height=1, width=10, text="Read", command=getTextInput)   #command绑定获取文本框内容的方法
btnRead.pack()
win.mainloop()
