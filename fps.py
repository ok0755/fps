#coding=utf-8
from Tkinter import *
import ttk
import tkMessageBox
import shelve
import string
import win32api
from win32api import GetSystemMetrics
def cmd_exe(event=None):
    try:
        if players.current()==0:
            open_file=lis['fps'][string.upper(text_value.get())]                  ## 精确匹配输入字符串，将接收的小写字母强制转换成大写，匹配出FPS文件路径
        elif players.current()==1:
            open_file=lis['cad'][string.upper(text_value.get())]                  ## 查找CAD或零件图
        win32api.ShellExecute(0,'open',open_file,'','',1)                         ## 调用默认浏览器打开图纸
    except:
        tkMessageBox.showinfo('警告','{} 无该编号图纸'.format(text_value.get()))  ## 错误提示
width = GetSystemMetrics(0)/2                                                     ## 程序居中屏幕显示
height = GetSystemMetrics(1)/2
root = Tk()
root.geometry('418x57+{}+{}'.format(width-209,height-57))
root.resizable(0,0)
root.title(u'图纸查询')
name = StringVar()
text_value= StringVar()
players = ttk.Combobox(root, textvariable=name,width=14,font=("Microsoft YaHei", 14))
players.grid(sticky=W,row=0,column=0)
players["values"] = (u"FPS图",u"零件图 or CAD图")  ## 因大多数fps与cad文件名相同，路径不同，故分开识别
players["state"] = "readonly"
players.current(0)

e=Entry(root,textvariable=text_value,width=21,font=("Microsoft YaHei", 14))       ## 输入框，接收图纸编号
e.grid(sticky=W,row=0,column=1)
e.bind('<Return>',cmd_exe)
Label(root,text='(C)周斌 保留所有权利',fg='#D7236B',relief='groove',bd=2,padx=1,pady=2,font=("Microsoft YaHei", 10), width=52).grid(sticky=W,row=1,column=0,columnspan=2)
lis=shelve.open(r'I:\Public\fps.db',flag='r')
Entry.focus_set(e)                                                                 ## 光标定位于输入框
root.mainloop()