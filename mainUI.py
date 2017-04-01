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
    predict_owner = vote_all_model_with_acc('model56mix',tobe_predict=wav_path)
    predict_result_varible.set(predict_owner)

    if owner == predict_owner:

        photo_label.config(image=right)
    else:
        photo_label.config(image=wrong)

    return 0


def singing_openfile():
    addres = tkFileDialog.askopenfilename(title='choose wav file ',
                                          filetypes=[('Audio', '*.wav *.WAV'), ('All Files', '*')])
    print addres
    singing_path_entry_varible.set(addres)
    owner = addres.split('-')[-1].split('.')[0]
    singing_true_result_variable.set(owner)
    return addres


def singing_submit():
    wav_path = singing_path_entry_varible.get()
    owner = singing_true_result_variable.get()
    predict_owner = vote_all_model_with_acc('model28singing',tobe_predict=wav_path)
    singing_predict_result_varible.set(predict_owner)

    if owner == predict_owner:

        singing_photo_label.config(image=right)
    else:
        singing_photo_label.config(image=wrong)

    return 0


def reading_openfile():
    addres = tkFileDialog.askopenfilename(title='choose wav file ',
                                          filetypes=[('Audio', '*.wav *.WAV'), ('All Files', '*')])
    print addres
    reading_path_entry_varible.set(addres)
    owner = addres.split('-')[-1].split('.')[0]
    reading_true_result_variable.set(owner)
    return addres


def reading_submit():
    wav_path = reading_path_entry_varible.get()
    owner = reading_true_result_variable.get()
    predict_owner = vote_all_model_with_acc('model28reading',tobe_predict=wav_path)
    reading_predict_result_varible.set(predict_owner)

    if owner == predict_owner:

        reading_photo_label.config(image=right)
    else:
        reading_photo_label.config(image=wrong)

    return 0


def readOnsing_openfile():
    addres = tkFileDialog.askopenfilename(title='choose wav file ',
                                          filetypes=[('Audio', '*.wav *.WAV'), ('All Files', '*')])
    print addres
    readOnsing_path_entry_varible.set(addres)
    owner = addres.split('-')[-1].split('.')[0]
    readOnsing_true_result_variable.set(owner)
    return addres


def readOnsing_submit():
    wav_path = readOnsing_path_entry_varible.get()
    owner = readOnsing_true_result_variable.get()
    predict_owner = vote_all_model_with_acc('model28readOnsing',tobe_predict=wav_path)
    readOnsing_predict_result_varible.set(predict_owner)

    if owner == predict_owner:

        readOnsing_photo_label.config(image=right)
    else:
        readOnsing_photo_label.config(image=wrong)

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


singing_title_libel = Label(win, text='singing voice recognition')
singing_intro_labe = Label(win, text='pls choose wav file:')
singing_path_entry_varible = StringVar()
singing_path_entry = Entry(win, state=DISABLED, textvariable=singing_path_entry_varible)
singing_choose_button = Button(win, text='choose', command=singing_openfile)
singing_submit_button = Button(win, text='submit', command=singing_submit)
singing_true_label = Label(win, text='answer:')
singing_true_result_variable = StringVar()
singing_true_result = Entry(win, state=DISABLED, textvariable=singing_true_result_variable)
singing_predict_label = Label(win, text='predict:')
singing_predict_result_varible = StringVar()
singing_predict_result = Entry(win, state=DISABLED, textvariable=singing_predict_result_varible)
singing_photo_label = Label()
singing_photo_label.config(image=default)


singing_title_libel.grid(row=4, column=0, columnspan=4)
singing_intro_labe.grid(row=5, column=0, sticky=W)
singing_path_entry.grid(row=5, column=1, sticky=W)
singing_choose_button.grid(row=5, column=2, sticky=W)
singing_submit_button.grid(row=5, column=3, sticky=W)
singing_true_label.grid(row=6, column=0, sticky=W)
singing_true_result.grid(row=6, column=1, sticky=W)
singing_predict_label.grid(row=7, column=0, sticky=W)
singing_predict_result.grid(row=7, column=1, sticky=W)
singing_photo_label.grid(row=6, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)




reading_title_libel = Label(win, text='reading voice recognition')
reading_intro_labe = Label(win, text='pls choose wav file:')
reading_path_entry_varible = StringVar()
reading_path_entry = Entry(win, state=DISABLED, textvariable=reading_path_entry_varible)
reading_choose_button = Button(win, text='choose', command=reading_openfile)
reading_submit_button = Button(win, text='submit', command=reading_submit)
reading_true_label = Label(win, text='answer:')
reading_true_result_variable = StringVar()
reading_true_result = Entry(win, state=DISABLED, textvariable=reading_true_result_variable)
reading_predict_label = Label(win, text='predict:')
reading_predict_result_varible = StringVar()
reading_predict_result = Entry(win, state=DISABLED, textvariable=reading_predict_result_varible)
reading_photo_label = Label()
reading_photo_label.config(image=default)


reading_title_libel.grid(row=8, column=0, columnspan=4)
reading_intro_labe.grid(row=9, column=0, sticky=W)
reading_path_entry.grid(row=9, column=1, sticky=W)
reading_choose_button.grid(row=9, column=2, sticky=W)
reading_submit_button.grid(row=9, column=3, sticky=W)
reading_true_label.grid(row=10, column=0, sticky=W)
reading_true_result.grid(row=10, column=1, sticky=W)
reading_predict_label.grid(row=11, column=0, sticky=W)
reading_predict_result.grid(row=11, column=1, sticky=W)
reading_photo_label.grid(row=10, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)


readOnsing_title_libel = Label(win, text='readOnsing voice recognition')
readOnsing_intro_labe = Label(win, text='pls choose wav file:')
readOnsing_path_entry_varible = StringVar()
readOnsing_path_entry = Entry(win, state=DISABLED, textvariable=readOnsing_path_entry_varible)
readOnsing_choose_button = Button(win, text='choose', command=readOnsing_openfile)
readOnsing_submit_button = Button(win, text='submit', command=readOnsing_submit)
readOnsing_true_label = Label(win, text='answer:')
readOnsing_true_result_variable = StringVar()
readOnsing_true_result = Entry(win, state=DISABLED, textvariable=readOnsing_true_result_variable)
readOnsing_predict_label = Label(win, text='predict:')
readOnsing_predict_result_varible = StringVar()
readOnsing_predict_result = Entry(win, state=DISABLED, textvariable=readOnsing_predict_result_varible)
readOnsing_photo_label = Label()
readOnsing_photo_label.config(image=default)


readOnsing_title_libel.grid(row=12, column=0, columnspan=4)
readOnsing_intro_labe.grid(row=13, column=0, sticky=W)
readOnsing_path_entry.grid(row=13, column=1, sticky=W)
readOnsing_choose_button.grid(row=13, column=2, sticky=W)
readOnsing_submit_button.grid(row=13, column=3, sticky=W)
readOnsing_true_label.grid(row=14, column=0, sticky=W)
readOnsing_true_result.grid(row=14, column=1, sticky=W)
readOnsing_predict_label.grid(row=15, column=0, sticky=W)
readOnsing_predict_result.grid(row=15, column=1, sticky=W)
readOnsing_photo_label.grid(row=14, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

mainloop()  # 进入主循环，程序运行
