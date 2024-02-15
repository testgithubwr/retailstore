from tkinter import *
import random
from tkinter import messagebox

timeleft=60
def timer():
    global timeleft,i
    if timeleft>0:
        timeleft-=1
        timerlabel.config(text=timeleft)
        timerlabel.after(1000,timer)
    else:
        wordentry.config(state=DISABLED)
        result=correct_word-wrong_word
        instructionlabel.config(text=f'Correct words {correct_word}\n Wrong words {wrong_word}\n Final score {result}')
        if result<15:
            emojilabel.config(image=sadimage)
            emoji2label.config(image=sadimage)
        if result>15:
            emojilabel.config(image=happyimage)
            emoji2label.config(image=happyimage)
        if result>30:
            emojilabel.config(image=proimage)
            emoji2label.config(image=proimage)
        res=messagebox.askyesno('Confirm','Do you want to play again?')
        if res:
            i=0
            timeleft=60
            countlabel.config(text='0')
            timerlabel.config(text='60')
            wordentry.config(state=NORMAL)
            instructionlabel.config(text='Type and HIT ENTER')
            emojilabel.config(image='')
            emoji2label.config(image='')



correct_word=0
wrong_word=0
i=0
def lets_begin(event):
    if wordentry.get()!='':
        global i,correct_word,wrong_word
        i+=1
        countlabel.config(text=i)
        instructionlabel.config(text='')
        if timeleft==60:
            timer()

        if wordentry.get()==wordl['text']:
            correct_word+=1
        else:
            wrong_word+=1

        random.shuffle(word_list)
        wordl.config(text=word_list[0])
        wordentry.delete(0, END)

word_list=['Elephant','King','Bhopal','Kerala','singapore','australia','banana','grapes','ram','canada','eagle','zebra','table','Laptop','mouse',
           'photo','shirt','Charger','jug','light','frame','key','fish','God','tractor','mirror','sparrow','flower','bulb','hat',
           'nice','killer','hat','hand','eyes','parrot','bell']


sliderwords=''
count=0
def slider():
    global sliderwords,count
    text='Welcome to TYPING GAME'
    if count>=len(text):
        count=0
        sliderwords=''
    sliderwords=sliderwords+text[count]
    movelabel.config(text=sliderwords)
    count +=1
    movelabel.after(100,slider)


root=Tk()
root.title('Speed typing game')
root.iconbitmap('communication_laptop_typing_computer_keyboard_icon_251404.ico')
root.geometry('800x700+120+80')
root.resizable(False,False)
root.config(bg='light blue')
logoimage=PhotoImage(file='computer2.png')
logolabel=Label(root,image=logoimage,bg='light blue')
logolabel.place(x=270,y=110)

movelabel=Label(root,text='',bg='light blue',font=('arial',25,'bold italic'),width=35,fg='brown')
movelabel.place(x=0,y=10)
slider()
random.shuffle(word_list)
wordl=Label(root,text=word_list[0],font=('cooper black',38,'italic bold'),bg='light blue')
wordl.place(x=380,y=380,anchor=CENTER)

wordlabel= Label(root,text='Words',font=('cooper black',38,'bold'),bg='light blue')
wordlabel.place(x=40,y=140)

countlabel= Label(root,text='0',font=('black cooper',38,'bold'),bg='light blue')
countlabel.place(x=90,y=200)


timelabel= Label(root,text='Timer',font=('cooper black',38,'bold'),bg='light blue')
timelabel.place(x=600,y=140)

timerlabel= Label(root,text='60',font=('cooper black',38,'bold'),bg='light blue')
timerlabel.place(x=650,y=200)


wordentry= Entry(root,font=('arial',25,'bold'),bd=8,justify=CENTER)
wordentry.place(x=190,y=420)
wordentry.focus_set()
instructionlabel= Label(root,text='Type and HIT ENTER',font=('chiller',38,'bold'),bg='light blue',fg='red')
instructionlabel.place(x=220,y=500)

happyimage=PhotoImage(file='happy.png')
sadimage=PhotoImage(file='sad.png')
proimage=PhotoImage(file='pro.png')

emojilabel=Label(root,bg='light blue')
emojilabel.place(x=80,y=450)


happy2image=PhotoImage(file='happy.png')
emoji2label=Label(root,bg='light blue')
emoji2label.place(x=610,y=450)

root.bind('<Return>',lets_begin)





root.mainloop()
