from pygame import mixer
from tkinter import *
from tkinter.ttk import Progressbar


mixer.init()

mixer.music.load('kbc.mp3')
mixer.music.play(-1)


def select(event):
    progessbarA.place_forget()
    progessbarB.place_forget()
    progessbarC.place_forget()
    progessbarD.place_forget()

    progessbarlabelA.place_forget()
    progessbarlabelB.place_forget()
    progessbarlabelC.place_forget()
    progessbarlabelD.place_forget()



    b = event.widget
    value=b['text']
    print(value)

    for i in range(15):
        if value == correct_answer [i]:
            if value==correct_answer[14]:
                def close():
                    root2.destroy()
                    root.destroy()

                def playagain():
                    root2.destroy()
                    questionarea.delete(1.0, END)
                    questionarea.insert(END, questions[0])
                    optionAbutton.config(text=first_option[0])
                    optionBbutton.config(text=second_option[0])
                    optionCbutton.config(text=third_option[0])
                    optionDbutton.config(text=fourth_option[0])
                    amountlabel.config(image=amount_image[0])
                mixer.music.stop()
                mixer.music.load('Kbcwon.mp3')
                mixer.music.play()


                root2 = Toplevel()
                root2.config(bg='black')
                root2.geometry('550x480+100+20')
                root2.title('Congratulations! U won 1 millions dollars')
                imagelabel = Label(root2, image=logoimage, bd=0, bg='black')
                imagelabel.pack(padx=40)

                winlabel = Label(root2, text="YOU WIN", font=('cooper black', 40, 'bold'), bg='black', fg='white')
                winlabel.pack(padx=30)

                playagainbutton = Button(root2, text="Play Again", font=('arial', 20, 'bold'), bg='black', fg='white',
                                        activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                        command=playagain)
                playagainbutton.pack()

                closebutton = Button(root2, text="Close", font=('arial', 20, 'bold'), bg='black', fg='white',
                                     activebackground='black', activeforeground='white', bd=0, cursor='hand2',
                                     command=close)
                closebutton.pack()

                happyimage = PhotoImage(file='happy.png')
                happylabel = Label(root2, image=happyimage, bg='black')
                happylabel.place(x=40, y=350)

                happyimage2 = PhotoImage(file='happy.png')
                happylabel = Label(root2, image=happyimage2, bg='black')
                happylabel.place(x=450, y=350)

                root2.mainloop()
                break

            questionarea.delete(1.0,END)
            questionarea.insert(END,questions[i+1])

            optionAbutton.config(text=first_option[i+1])
            optionBbutton.config(text=second_option[i+1])
            optionCbutton.config(text=third_option[i+1])
            optionDbutton.config(text=fourth_option[i+1])
            amountlabel.config(image=amount_image[i+1])

        if value not in correct_answer:
            def close():
                root1.destroy()
                root.destroy()

            def tryagain():
                root1.destroy()
                questionarea.delete(1.0,END)
                questionarea.insert(END,questions[0])
                optionAbutton.config(text=first_option[0])
                optionBbutton.config(text=second_option[0])
                optionCbutton.config(text=third_option[0])
                optionDbutton.config(text=fourth_option[0])

                amountlabel.config(image=amount_image[i])

            root1=Toplevel()
            root1.config(bg='black')
            root1.geometry('550x480+100+20')
            root1.title('U won 0 dollars')
            imagelabel=Label(root1,image=logoimage,bd=0,bg='black')
            imagelabel.pack(padx=40)

            loselabel=Label(root1,text="YOU LOSE",font=('cooper black',40,'bold'),bg='black',fg='white')
            loselabel.pack(padx=30)

            tryagainbutton=Button(root1,text="Try Again",font=('arial',20,'bold'),bg='black',fg='white',activebackground='black',activeforeground='white',bd=0,cursor='hand2',command=tryagain)
            tryagainbutton.pack()

            closebutton = Button(root1, text="Close", font=('arial', 20, 'bold'), bg='black', fg='white',
                                    activebackground='black', activeforeground='white', bd=0, cursor='hand2',command=close)
            closebutton.pack()

            sadimage=PhotoImage(file='sad.png')
            sadlabel=Label(root1,image=sadimage,bg='black')
            sadlabel.place(x=40,y=350)

            sadimage2 = PhotoImage(file='sad.png')
            sadlabel = Label(root1, image=sadimage2, bg='black')
            sadlabel.place(x=450, y=350)

            root1.mainloop()
            break

def lifeline50():
    lifeline50image.config(image=image50x,state=DISABLED)
    if questionarea.get(1.0,'end-1c')==questions[0]:
        optionBbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[1]:
        optionAbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[2]:
        optionAbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0,'end-1c')==questions[3]:
        optionCbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[4]:
        optionBbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[5]:
        optionBbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[6]:
        optionAbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[7]:
        optionAbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[8]:
        optionAbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[9]:
        optionBbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[10]:
        optionAbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[11]:
        optionCbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[12]:
        optionBbutton.config(text='')
        optionDbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[13]:
        optionBbutton.config(text='')
        optionCbutton.config(text='')

    if questionarea.get(1.0, 'end-1c') == questions[14]:
        optionAbutton.config(text='')
        optionBbutton.config(text='')

def audiancepolelifeline():
        audianceimage.config(image=imageaudicancex, state=DISABLED)
        progessbarA.place(x=600,y=200)
        progessbarB.place(x=630,y=200)
        progessbarC.place(x=660,y=200)
        progessbarD.place(x=690,y=200)

        progessbarlabelA.place(x=600,y=320)
        progessbarlabelB.place(x=630,y=320)
        progessbarlabelC.place(x=660,y=320)
        progessbarlabelD.place(x=690,y=320)

        if questionarea.get(1.0,'end-1c')==questions[0]:
            progessbarA.config(value=80)
            progessbarB.config(value=50)
            progessbarC.config(value=40)
            progessbarD.config(value=60)


        if questionarea.get(1.0,'end-1c')==questions[1]:
            progessbarA.config(value=10)
            progessbarB.config(value=40)
            progessbarC.config(value=80)
            progessbarD.config(value=20)

        if questionarea.get(1.0,'end-1c')==questions[2]:
            progessbarA.config(value=60)
            progessbarB.config(value=50)
            progessbarC.config(value=30)
            progessbarD.config(value=90)

        if questionarea.get(1.0,'end-1c')==questions[3]:
            progessbarA.config(value=00)
            progessbarB.config(value=80)
            progessbarC.config(value=40)
            progessbarD.config(value=50)

        if questionarea.get(1.0,'end-1c')==questions[4]:
            progessbarA.config(value=90)
            progessbarB.config(value=50)
            progessbarC.config(value=10)
            progessbarD.config(value=60)

        if questionarea.get(1.0,'end-1c')==questions[5]:
            progessbarA.config(value=80)
            progessbarB.config(value=50)
            progessbarC.config(value=10)
            progessbarD.config(value=90)

        if questionarea.get(1.0,'end-1c')==questions[6]:
            progessbarA.config(value=80)
            progessbarB.config(value=10)
            progessbarC.config(value=40)
            progessbarD.config(value=100)

        if questionarea.get(1.0,'end-1c')==questions[7]:
            progessbarA.config(value=40)
            progessbarB.config(value=50)
            progessbarC.config(value=80)
            progessbarD.config(value=60)

        if questionarea.get(1.0,'end-1c')==questions[8]:
            progessbarA.config(value=10)
            progessbarB.config(value=80)
            progessbarC.config(value=40)
            progessbarD.config(value=12)

        if questionarea.get(1.0,'end-1c')==questions[9]:
            progessbarA.config(value=80)
            progessbarB.config(value=50)
            progessbarC.config(value=40)
            progessbarD.config(value=55)

        if questionarea.get(1.0,'end-1c')==questions[10]:
            progessbarA.config(value=42)
            progessbarB.config(value=50)
            progessbarC.config(value=40)
            progessbarD.config(value=97)

        if questionarea.get(1.0,'end-1c')==questions[11]:
            progessbarA.config(value=10)
            progessbarB.config(value=80)
            progessbarC.config(value=33)
            progessbarD.config(value=11)

        if questionarea.get(1.0,'end-1c')==questions[12]:
            progessbarA.config(value=72)
            progessbarB.config(value=55)
            progessbarC.config(value=80)
            progessbarD.config(value=60)

        if questionarea.get(1.0,'end-1c')==questions[13]:
            progessbarA.config(value=84)
            progessbarB.config(value=50)
            progessbarC.config(value=21)
            progessbarD.config(value=60)

        if questionarea.get(1.0,'end-1c')==questions[14]:
            progessbarA.config(value=41)
            progessbarB.config(value=66)
            progessbarC.config(value=40)
            progessbarD.config(value=82)



correct_answer= ["CHEETAH","RAJASTHAN","26 JANUARY","VICE-PRESIDENT","PRESIDENT","SAHARA",
                 "EURO","EVEREST","UNIFORM RESOURCE LOCATOR","1024KB","ANDRA PRADESH","YURI GAGAIN","UTTAR PRADESH","NH44","BANGLORE"]



questions=["Fastest animal on the earth?",
           "Which is the Largest state in India?",
           "When we celebrate our Indian Republic day",
           "Who is the 2nd citizen of India",
           "Who is the 1st citizen of India",
           "Largest desert in the world",
           "What currency do they use in FRANCE",
           "What is the highest mountain in the Himalaya",
           "Full form of URL is",
           "1 Mega byte ",
           "Satish Dhawan space center in which state",
           "First human to travel in space",
           "Which state is known as the sugar bowl of India",
           "Which is the longest National Highway in India",
           "Which city is known as Electronic city"
           ]

first_option=["CHEETAH","PUNJAB","3 MARCH","PRIME MINISTER","PRESIDENT","SIBERIA","COINS","URAL","UNIFORM ROSE LION","1024KB",
              "MAHARASTRA","RAKESH","ASSAM","NH44","TAMIL NADU"]

second_option=["PIG","GOA","21 DECEMBER","VICE-PRESIDENT","PRIME MINISTER","THAR","RUPEE","NANGA PARVAT","UNIFORM RESOURCE LOCATOR","1200KB",
               "KERALA","YURI GAGAIN","PUNJAB","NH26","ODISHA"]


third_option=["DEER","RAJASTHAN","30 JANUARY","GOVERNOR","CHIEF MINISTER","GOBI","YEN","EVEREST","UNIFORM RING LOCATION","1000KB",
              "MADHYA PRADESH","SACHIN TENDULKAR","UTTAR PRADESH","NH10","PUNE"]



fourth_option=["HORSE","BIHAR","26 JANUARY","DEFENCE MINISTER","GOVERNOR","SAHARA","EURO","K2","UNIFORM RISE LINK","999KB",
               "ANDRA PRADESH","MS DHONI","DELHI","NH33","BANGLORE"]




root=Tk()
root.geometry('1270x750+0+0')
root.title("KOHN BANEGA CARORPATI")
root.config(bg='black',bd=0)

leftframe= Frame(root,padx=30,pady=10,bg='black')
leftframe.grid(row=0,column=0)


topframe= Frame(leftframe,bg='black')
topframe.grid()


centerframe= Frame(leftframe,bg='black',bd=0)
centerframe.grid(row=1,column=0)


bottomframe= Frame(leftframe,pady=50,bg='black')
bottomframe.grid(row=2,column=0)

rightframe= Frame(root,padx=180,pady=50,bg='black')
rightframe.grid(row=0,column=1)


image50 =PhotoImage(file='50-50.png')
image50x=PhotoImage(file='50-50-X.png')
lifeline50image= Button(topframe,image=image50,bg='black',bd=0,activebackground='black',width=180,height=80,command=lifeline50)
lifeline50image.grid(row=0,column=0)

imageaudicance =PhotoImage(file='audiencePole.png')
imageaudicancex= PhotoImage(file='audiencePoleX.png')
audianceimage= Button(topframe,image=imageaudicance,bg='black',bd=0,activebackground='black',width=180,height=80,command=audiancepolelifeline)
audianceimage.grid(row=0,column=2,)




logoimage =PhotoImage(file='KAUN_BANEGA_CROREPATI_SEASON_11.png')
logolabel= Label(centerframe,image=logoimage,bg='black')
logolabel.grid(row=2,column=2)


amountimage16= PhotoImage(file='Picture15.png')
amountlabel= Label(rightframe,image=amountimage16,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage15= PhotoImage(file='Picture14.png')
amountlabel= Label(rightframe,image=amountimage15,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage14= PhotoImage(file='Picture13.png')
amountlabel= Label(rightframe,image=amountimage14,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage13= PhotoImage(file='Picture12.png')
amountlabel= Label(rightframe,image=amountimage13,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage12= PhotoImage(file='Picture11.png')
amountlabel= Label(rightframe,image=amountimage12,bg='black',pady=0)
amountlabel.grid(row=0,column=0)


amountimage11= PhotoImage(file='Picture10.png')
amountlabel= Label(rightframe,image=amountimage11,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage10= PhotoImage(file='Picture9.png')
amountlabel= Label(rightframe,image=amountimage10,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage9= PhotoImage(file='Picture8.png')
amountlabel= Label(rightframe,image=amountimage9,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage8= PhotoImage(file='Picture7.png')
amountlabel= Label(rightframe,image=amountimage8,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage7= PhotoImage(file='Picture6.png')
amountlabel= Label(rightframe,image=amountimage7,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage6= PhotoImage(file='Picture5.png')
amountlabel= Label(rightframe,image=amountimage6,bg='black',pady=0)
amountlabel.grid(row=0,column=0)


amountimage5= PhotoImage(file='Picture4.png')
amountlabel= Label(rightframe,image=amountimage5,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage4= PhotoImage(file='Picture3.png')
amountlabel= Label(rightframe,image=amountimage4,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage3= PhotoImage(file='Picture2.png')
amountlabel= Label(rightframe,image=amountimage3,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage2= PhotoImage(file='Picture1.png')
amountlabel= Label(rightframe,image=amountimage2,bg='black',pady=0)
amountlabel.grid(row=0,column=0)

amountimage1= PhotoImage(file='amount.png')
amountlabel= Label(rightframe,image=amountimage1,bg='black',pady=0)
amountlabel.grid(row=0,column=0)


amount_image=[amountimage1,amountimage2,amountimage3,amountimage4,amountimage5,amountimage6,amountimage7,amountimage8,amountimage9,amountimage10,amountimage11,amountimage12,amountimage13,amountimage14,amountimage15,amountimage16]


layoutimage= PhotoImage(file='lay.png')
laytimage=Label(bottomframe,image=layoutimage,bg='black',pady=50)
laytimage.grid(row=0,column=0)


questionarea= Text(bottomframe,font=("Times new roman",16,'bold'),width=35,height=2,bg='black',fg='white',bd=0)
questionarea.place(x=55,y=15)


labelA= Label(bottomframe,text='A:',font=('Times new roman',15,'bold'),bg='black',fg='white')
labelA.place(x=50,y=110)

questionarea.insert(END,questions[0])

optionAbutton= Button(bottomframe,text=first_option[0],font=('Times new roman',15,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionAbutton.place(x=73,y=107)


labelB= Label(bottomframe,text='B:',font=('Times new roman',15,'bold'),bg='black',fg='white')
labelB.place(x=320,y=110)
optionBbutton= Button(bottomframe,text=second_option[0],font=('Times new roman',15,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionBbutton.place(x=345,y=107)


labelC= Label(bottomframe,text='C:',font=('Times new roman',15,'bold'),bg='black',fg='white')
labelC.place(x=50,y=190)
optionCbutton= Button(bottomframe,text=third_option[0],font=('Times new roman',15,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionCbutton.place(x=75,y=187)


labelD= Label(bottomframe,text='D:',font=('Times new roman',15,'bold'),bg='black',fg='white')
labelD.place(x=320,y=190)
optionDbutton= Button(bottomframe,text=fourth_option[0],font=('Times new roman',15,'bold'),bg='black',fg='white',bd=0,activebackground='black',activeforeground='white',cursor='hand2')
optionDbutton.place(x=345,y=185)


progessbarA=Progressbar(root,orient=VERTICAL, length=120)
progessbarB=Progressbar(root,orient=VERTICAL, length=120)
progessbarC=Progressbar(root,orient=VERTICAL, length=120)
progessbarD=Progressbar(root,orient=VERTICAL, length=120)


progessbarlabelA= Label(root,text='A',font=('arial',20,'bold'),bg='black',fg='white')
progessbarlabelB= Label(root,text='B',font=('arial',20,'bold'),bg='black',fg='white')
progessbarlabelC= Label(root,text='C',font=('arial',20,'bold'),bg='black',fg='white')
progessbarlabelD= Label(root,text='D',font=('arial',20,'bold'),bg='black',fg='white')



optionAbutton.bind('<Button-1>',select )
optionBbutton.bind('<Button-1>',select )
optionCbutton.bind('<Button-1>',select )
optionDbutton.bind('<Button-1>',select )


root.mainloop()



