# coding=utf-8
import tkFileDialog
from Tkinter import *  # 引入Tkinter工具包

from voteAllSkearn import vote_all_model_with_acc


def openfile():
    addres = tkFileDialog.askopenfilename(title='choose wav file ',
                                          filetypes=[('Audio', '*.wav *.WAV'), ('All Files', '*')])
    print addres
    path_entry_varible.set(addres)
    owner = addres.split('-')[-1].split('.')[0]
    true_result_variable.set(owner)
    return addres


def submit():
    wav_path = path_entry_varible.get()
    owner = true_result_variable.get()
    predict_owner = vote_all_model_with_acc(tobe_predict=wav_path)
    predict_result_varible.set(predict_owner)

    if owner == predict_owner:

        photo_label.config(image=right)
    else:
        photo_label.config(image=wrong)

    return 0


win = Tk()  # 定义一个窗体
win.title('RSCR')  # 定义窗体标题
# win.config(bg='w')
# win.geometry('600x100')  # 定义窗体的大小，是400X200像素
title_libel = Label(win, text='RSCR:(R)reading and (S)singing voice recognition and (C)cross (R)recognition')
intro_labe = Label(win, text='pls choose wav file:')
path_entry_varible = StringVar()
path_entry = Entry(win, state=DISABLED, textvariable=path_entry_varible)
choose_button = Button(win, text='choose', command=openfile)
submit_button = Button(win, text='submit', command=submit)
true_label = Label(win, text='answer:')
true_result_variable = StringVar()
true_result = Entry(win, state=DISABLED, textvariable=true_result_variable)
predict_label = Label(win, text='predict:')
predict_result_varible = StringVar()
predict_result = Entry(win, state=DISABLED, textvariable=predict_result_varible)
default = PhotoImage(file='default.gif')
right = PhotoImage(file='right.gif')
wrong = PhotoImage(file='wrong.gif')
photo_label = Label()
photo_label.config(image=default)

title_libel.grid(row=0, column=0, columnspan=4)
intro_labe.grid(row=1, column=0, sticky=W)
path_entry.grid(row=1, column=1, sticky=W)
choose_button.grid(row=1, column=2, sticky=W)
submit_button.grid(row=1, column=3, sticky=W)
true_label.grid(row=2, column=0, sticky=W)
true_result.grid(row=2, column=1, sticky=W)
predict_label.grid(row=3, column=0, sticky=W)
predict_result.grid(row=3, column=1, sticky=W)
photo_label.grid(row=2, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

mainloop()  # 进入主循环，程序运行
