# coding=utf-8
import tkFileDialog
from Tkinter import *  # 引入Tkinter工具包

from voteAllSkearn import vote_all_model_with_acc


def openfile():
    addres = tkFileDialog.askopenfilename(title='choose wav file ',
                                          filetypes=[('Audio', '*.wav *.WAV'), ('All Files', '*')])
    print addres
    path_entry_varible.set(addres)
    return addres


def submit():
    wav_path = path_entry_varible.get()
    owner = wav_path.split('-')[-1].split('.')[0]
    true_result_variable.set(owner)
    predict_owner = vote_all_model_with_acc(tobe_predict=wav_path)
    predict_result_varible.set(predict_owner)

    return 0


win = Tk()  # 定义一个窗体
win.title('RSCR')  # 定义窗体标题
win.geometry('600x100')  # 定义窗体的大小，是400X200像素
topFrame = Frame(win)
title_libel = Label(topFrame, text='RSCR:(R)reading and (S)singing voice recognition and (C)cross (R)recognition')
title_libel.pack()
topFrame.pack()
secondFrame = Frame(win)
left = Frame(secondFrame)
intro_labe = Label(left, text='pls choose wav file:')
intro_labe.pack(side=LEFT)
left.pack(side=LEFT)
leftSecond = Frame(secondFrame)
path_entry_varible = StringVar()
path_entry = Entry(leftSecond, state=DISABLED, textvariable=path_entry_varible)
path_entry.pack(side=LEFT)
leftSecond.pack(side=LEFT)
right = Frame(secondFrame)
choose_button = Button(right, text='choose', command=openfile)
choose_button.pack(side=LEFT)
right.pack(side=LEFT)
rightSecond = Frame(secondFrame)
submit_button = Button(rightSecond, text='submit', command=submit)
submit_button.pack(side=LEFT)
rightSecond.pack(side=LEFT)
secondFrame.pack()
thirdFrame = Frame(win)
leftThird = Frame(thirdFrame)
true_label = Label(leftThird, text='answer:')
true_label.pack(side=LEFT)
leftThird.pack(side=LEFT)
rightThird = Frame(thirdFrame)
true_result_variable = StringVar()
true_result = Entry(rightThird, state=DISABLED, textvariable=true_result_variable)
true_result.pack(side=LEFT)
rightThird.pack(side=LEFT)
thirdFrame.pack()
finalFrame = Frame(win)
leftFinal = Frame(finalFrame)
predict_label = Label(leftFinal, text='predict:')
predict_label.pack(side=LEFT)
leftFinal.pack(side=LEFT)
rightFinal = Frame(finalFrame)
predict_result_varible = StringVar()
predict_result = Entry(rightFinal, state=DISABLED, textvariable=predict_result_varible)
predict_result.pack(side=LEFT)
rightFinal.pack(side=LEFT)
finalFrame.pack()
mainloop()  # 进入主循环，程序运行
