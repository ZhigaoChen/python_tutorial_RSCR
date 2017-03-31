from tkinter import *

win = Tk()
label1 = Label(win, text='hell',borderwidth=10)
label2 = Label(win, text='hell')
entry1 = Entry(win)
entry2 = Entry(win)
checkbutton = Checkbutton(win)
radiobutton = Radiobutton(win)
# image = Image(win)
button1 = Button(win,text='hello')
button2 = Button(win,text='hhhhhhhh')

label1.grid(sticky=E)
label2.grid(sticky=E)

entry1.grid(row=0, column=1,columnspan=2, rowspan=2,sticky=W + E + N + S,)
entry2.grid(row=1, column=1)
checkbutton.grid(row=2,column=0)
radiobutton.grid(row=1, column=2)
# image.grid(row=0, column=2, columnspan=2, rowspan=2,
#            sticky=W + E + N + S, padx=5, pady=5)
button1.grid(row=2, column=2)
button2.grid(row=2, column=3)
mainloop()
