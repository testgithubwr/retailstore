import tempfile
from tkinter import *
from tkinter import messagebox
import random,os,tempfile


def send_email():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.title("Send gmail")
        root1.config(bg='gray20')
        root1.resizable(0,0)

        senderframe= Label(root1,text='SENDER',font=('arial',16,'bold'))
        senderframe.grid(row=0,column=0)


        gmailIDlabel= Label(senderframe,text="Sender's Email",font=('arial',14,'bold'))
        gmailIDlabel.grid(row=0,column=0)


        root1.mainloop()


def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')


# def search_bill():
#     for i in os.listdir('bills/'):
#         if i.split('.')[0]==BillEntry.get():
#             fa = open(f'bills/{i}','r')
#             textarea.delete(1.0,END)
#             for data in fa:
#                 textarea.insert(END,data)
#             fa.close()
#             break
#
#     else:
#         messagebox.showerror('Error')
#


def save_bill():
    global billnumber
    result= messagebox.askyesno('Confirm, do you want to save the bill?')
    if result:
        bill_content= textarea.get(1.0,END)
        file= open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'bill number {billnumber} is saved successfully')
        billnumber = random.randint(500, 1000)

billnumber = random.randint(500,1000)
#funtion
def total():
    global soaprice,face,wash,hair,gel,lotion
    soaprice= int(bathsoapentry.get())*20
    face= int(facecreamentry.get())*50
    wash = int(facewashentry.get())*80
    hair = int(hairsprayentry.get())*100
    gel= int(hairgelentry.get())*60
    lotion= int(bodylotionentry.get())*90

    totalcosmaticprice= soaprice+face+wash+hair+gel+lotion
    cosmeticpriceentry.delete(0,END)
    cosmeticpriceentry.insert(0,f'{totalcosmaticprice} Rs')

    totalctax = totalcosmaticprice * 0.12
    cosmetictaxlabel.delete(0,END)
    cosmetictaxlabel.insert(0, str(totalctax)+'Rs')

    #grocery price
    global Rice,oil,Daal,Sugar,Tea,wheat
    Rice= int(Riceentry.get())*60
    oil= int(oilentry.get())*110
    Daal= int(Daalentry.get())*70
    Sugar= int(Sugarentry.get())*50
    Tea= int(Teaentry.get())*80
    wheat= int(Wheatentry.get())*30

    Totalgroceryprice= Rice+oil+Daal+Sugar+Tea+wheat
    groserypricelabel.delete(0,END)
    groserypricelabel.insert(0,f'{Totalgroceryprice} Rs')

    totalgtax= Totalgroceryprice*0.15
    groserytaxlabel.delete(0,END)
    groserytaxlabel.insert(0,str(totalgtax)+'Rs')

#Drinks price
    global  Maaza,pepsi,sprite,Dew,Frooti,Coca
    Maaza=int(Maaentry.get())*45
    pepsi= int(pepentry.get())*40
    sprite= int(spentry.get())*45
    Dew= int(Dewentry.get())*45
    Frooti= int(frentry.get())*45
    Coca= int(ccentry.get())*40

    Totaldrinksprice= Maaza+pepsi+sprite+Dew+Frooti+Coca
    drinkspricelabel.delete(0,END)
    drinkspricelabel.insert(0,f'{Totaldrinksprice} Rs')

    totaldtax= Totaldrinksprice*0.15
    colddrinktaxlabel.delete(0,END)
    colddrinktaxlabel.insert(0,str(totaldtax)+'Rs')


    global totalbill
    totalbill=totalcosmaticprice+Totaldrinksprice+Totalgroceryprice+totalctax+totalgtax+totaldtax

#Tax function
def print_area():
        if NameEntry.get() == '' or phoneEntry.get() == '':
             messagebox.showerror('Error','Customers Details Are Required')

        elif cosmeticpriceentry.get()== '0 Rs' or groserypricelabel.get() == '0 Rs' or drinkspricelabel.get() == '0 Rs':
            messagebox.showerror('Error','No product are selected')
        elif cosmeticpriceentry.get() == '0 Rs' or groserypricelabel.get() == '0 Rs' or drinkspricelabel.get() == '0 Rs':
            messagebox.showerror('Error', 'No product are purchased')
        else:
            textarea.delete(1.0,END)

            textarea.insert(END,'\t\t**Welcome Customers**')
            textarea.insert(END,f'\nBill number:{billnumber}\n')
            textarea.insert(END,f'\nCustomer Name:{NameEntry.get()}\n')
            textarea.insert(END,f'\nCustomer phone number:{phoneEntry.get()}\n')
            textarea.insert(END,'\n=============================================')
            textarea.insert(END,'\nproduct\t\tQuantity\t\t\tprice')
            textarea.insert(END, '\n=============================================')
            if bathsoapentry.get() != '0':
                textarea.insert(END,f'\nBath soap\t\t\t{bathsoapentry.get()}\t\t{soaprice} Rs')
            if hairsprayentry.get() != '0':
                textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayentry.get()}\t\t{hair} Rs')
            if facecreamentry.get() != '0':
                textarea.insert(END,f'\nFace Cream\t\t\t{facecreamentry.get()}\t\t{face} Rs')
            if facewashentry.get() != '0':
                textarea.insert(END,f'\nFace Wash\t\t\t{facewashentry.get()}\t\t{wash} Rs')
            if hairgelentry.get() != '0':
                textarea.insert(END,f'\nHair Gel\t\t\t{hairgelentry.get()}\t\t{hair} Rs')
            if bodylotionentry.get() != '0':
                textarea.insert(END,f'\nBody lotion\t\t\t{bodylotionentry.get()}\t\t{lotion} Rs')
            if Riceentry.get() != '0':
                textarea.insert(END,f'\nRice\t\t\t{Riceentry.get()}\t\t{Rice} Rs')
            if Daalentry.get() != '0':
                textarea.insert(END,f'\nDaal\t\t\t{Daalentry.get()}\t\t{Daal} Rs')
            if Teaentry.get() != '0':
                textarea.insert(END,f'\nTea\t\t\t{Teaentry.get()}\t\t{Tea} Rs')
            if Sugarentry.get() != '0':
                textarea.insert(END,f'\nSugar\t\t\t{Sugarentry.get()}\t\t{Sugar} Rs')
            if oilentry.get() != '0':
                textarea.insert(END,f'\nOil\t\t\t{oilentry.get()}\t\t{oil} Rs')
            if Wheatentry.get() != '0':
                textarea.insert(END,f'\nwheat\t\t\t{Wheatentry.get()}\t\t{wheat} Rs')

        #cold drinks
            if Maaentry.get() != '0':
                textarea.insert(END, f'\nMaaza\t\t\t{Maaentry.get()}\t\t{Maaza} Rs')
            if pepentry.get() != '0':
                textarea.insert(END, f'\nPepsi\t\t\t{pepentry.get()}\t\t{pepsi} Rs')
            if spentry.get() != '0':
                textarea.insert(END, f'\nSprite\t\t\t{spentry.get()}\t\t{sprite} Rs')
            if Dewentry.get() != '0':
                textarea.insert(END, f'\nMaaza\t\t\t{Dewentry.get()}\t\t{Dew} Rs')
            if frentry.get() != '0':
                textarea.insert(END, f'\nFrooti\t\t\t{frentry.get()}\t\t{Frooti} Rs')
            if ccentry.get() != '0':
                textarea.insert(END, f'\nCoca cola\t\t\t{ccentry.get()}\t\t{Coca} Rs')
            textarea.insert(END, '\n---------------------------------------------')

            if cosmetictaxlabel != '0.0':
                textarea.insert(END,f'\n Cosmetic Tax\t\t\t\t{cosmetictaxlabel.get()}')
            if groserytaxlabel != '0.0':
                textarea.insert(END,f'\n Grosery Tax\t\t\t\t{groserytaxlabel.get()}')
            if colddrinktaxlabel != '0.0':
                textarea.insert(END,f'\n Cold drinks Tax\t\t\t\t{colddrinktaxlabel.get()}')
            textarea.insert(END, '\n---------------------------------------------')

            textarea.insert(END,f'\nTotal Bill\t\t\t\t{totalbill}')

            save_bill()





#GUI part
root=Tk()
root.title("Retail billing system")
root.geometry("1270x685")

headingLabel = Label(root,text="Retail Billing System",font=("Times new roman",40,"bold"),bg="Gray20",fg="gold",bd=12,relief="groove")
headingLabel.pack(fill='x')

customer_detail_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),fg='gold',relief='groove',bd=12,bg='gray20')
customer_detail_frame.pack(fill='x',pady=5)

namelabel=Label(customer_detail_frame,text='Name',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
namelabel.grid(row=0,column=0,padx=20,pady=2)

NameEntry= Entry(customer_detail_frame,font=('arial',15),bd=7,width=17)
NameEntry.grid(row=0,column=1,padx=8)

phonelabel=Label(customer_detail_frame,text='phone Number',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
phonelabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry= Entry(customer_detail_frame,font=('arial',15),bd=7,width=17)
phoneEntry.grid(row=0,column=3,padx=8)

billnolabel=Label(customer_detail_frame,text='Bill number',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
billnolabel.grid(row=0,column=4,padx=20,pady=2)

BillEntry= Entry(customer_detail_frame,font=('arial',15),bd=7,width=17)
BillEntry.grid(row=0,column=5,padx=8)

searchbutton=Label(customer_detail_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=15)
searchbutton.grid(row=0,column=6,padx=15,pady=8)

productframe = Frame(root)
productframe.pack(pady=8)

cosmeticframe = LabelFrame(productframe,text="Cosmetics",font=('times new roman',15,'bold'),fg='gold',relief='groove',bd=12,bg='gray20')
cosmeticframe.grid(row=0,column=0)

bathsoaplabel = Label(cosmeticframe,text='Bath Soap',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
bathsoaplabel.grid(row=0,column=0,pady=9,padx=10)
bathsoapentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
bathsoapentry.grid(row=0,column=1,pady=9,padx=10)
bathsoapentry.insert(0,0)

facecreamlabel = Label(cosmeticframe,text='Face Cream',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
facecreamlabel.grid(row=1,column=0,pady=9,padx=10)
facecreamentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
facecreamentry.grid(row=1,column=1,pady=9,padx=10)
facecreamentry.insert(0,0)

facewashlabel = Label(cosmeticframe,text='Face Wash',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
facewashlabel.grid(row=2,column=0,pady=9,padx=10,sticky='s')
facewashentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
facewashentry.grid(row=2,column=1,pady=9,padx=10)
facewashentry.insert(0,0)

hairspraylabel = Label(cosmeticframe,text='Hair spray',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
hairspraylabel.grid(row=3,column=0,pady=9,padx=10,sticky ='s')
hairsprayentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
hairsprayentry.grid(row=3,column=1,pady=9,padx=10)
hairsprayentry.insert(0,0)



hairgellabel = Label(cosmeticframe,text='Hair Gel',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
hairgellabel.grid(row=4,column=0,pady=9,padx=10,sticky = 's')
hairgelentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
hairgelentry.grid(row=4,column=1,pady=9,padx=10)
hairgelentry.insert(0,0)


bodylotionlabel = Label(cosmeticframe,text='Body Lotion',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
bodylotionlabel.grid(row=5,column=0,pady=9,padx=10,sticky = 's')
bodylotionentry= Entry(cosmeticframe,font=('times new roman',15,'bold'),width=13,bd=2)
bodylotionentry.grid(row=5,column=1,pady=9,padx=10)
bodylotionentry.insert(0,0)


Groceryframe = LabelFrame(productframe,text="Grocery",font=('times new roman',15,'bold'),fg='gold',relief='groove',bd=12,bg='gray20')
Groceryframe.grid(row=0,column=1)

Ricelabel=Label(Groceryframe,text='Rice',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Ricelabel.grid(row=0,column=0,pady=9,padx=10)
Riceentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
Riceentry.grid(row=0,column=1,pady=9,padx=10)
Riceentry.insert(0,0)

oillabel=Label(Groceryframe,text='Oil',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
oillabel.grid(row=1,column=0,pady=9,padx=10)
oilentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
oilentry.grid(row=1,column=1,pady=9,padx=10)
oilentry.insert(0,0)

Daallabel=Label(Groceryframe,text='Daal',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Daallabel.grid(row=2,column=0,pady=9,padx=10)
Daalentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
Daalentry.grid(row=2,column=1,pady=9,padx=10)
Daalentry.insert(0,0)

Wheatlabel=Label(Groceryframe,text='wheat',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Wheatlabel.grid(row=3,column=0,pady=9,padx=10)
Wheatentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
Wheatentry.grid(row=3,column=1,pady=9,padx=10)
Wheatentry.insert(0,0)


Sugarlabel=Label(Groceryframe,text='Sugar',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Sugarlabel.grid(row=4,column=0,pady=9,padx=10)
Sugarentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
Sugarentry.grid(row=4,column=1,pady=9,padx=10)
Sugarentry.insert(0,0)


Tealabel=Label(Groceryframe,text='Tea',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Tealabel.grid(row=5,column=0,pady=9,padx=10)
Teaentry= Entry(Groceryframe,font=('times new roman',15,'bold'),width=13,bd=2)
Teaentry.grid(row=5,column=1,pady=9,padx=10)
Teaentry.insert(0,0)


drinksframe = LabelFrame(productframe,text="Cold Drinks",font=('times new roman',15,'bold'),fg='gold',relief='groove',bd=12,bg='gray20')
drinksframe.grid(row=0,column=2)

Maalabel=Label(drinksframe,text='Maaza',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Maalabel.grid(row=0,column=0,pady=9,padx=10)
Maaentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
Maaentry.grid(row=0,column=1,pady=9,padx=10)
Maaentry.insert(0,0)


peplabel=Label(drinksframe,text='Pepsi',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
peplabel.grid(row=1,column=0,pady=9,padx=10)
pepentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
pepentry.grid(row=1,column=1,pady=9,padx=10)
pepentry.insert(0,0)
splabel=Label(drinksframe,text='Sprite',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
splabel.grid(row=2,column=0,pady=9,padx=10)
spentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
spentry.grid(row=2,column=1,pady=9,padx=10)
spentry.insert(0,0)
Dewlabel=Label(drinksframe,text='Dew',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
Dewlabel.grid(row=3,column=0,pady=9,padx=10)
Dewentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
Dewentry.grid(row=3,column=1,pady=9,padx=10)
Dewentry.insert(0,0)
frlabel=Label(drinksframe,text='Frooti',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
frlabel.grid(row=4,column=0,pady=9,padx=10)
frentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
frentry.grid(row=4,column=1,pady=9,padx=10)
frentry.insert(0,0)

cclabel=Label(drinksframe,text='Coca Cola',font=('Times new roman',15,'bold'),bg='gray20',fg='white')
cclabel.grid(row=5,column=0,pady=9,padx=10)
ccentry= Entry(drinksframe,font=('times new roman',15,'bold'),width=13,bd=2)
ccentry.grid(row=5,column=1,pady=9,padx=10)
ccentry.insert(0,0)


billframe= Frame(productframe,bd=8,relief='groove')
billframe.grid(row=0,column=3)

Billarealabel= Label(billframe,text="Label Area",font=("Times new roman",15,'bold'),bd=7,relief='groove',width=20)
Billarealabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient='vertical')
scrollbar.pack(side='right',fill=Y)

textarea=Text(billframe,height=18, width=48,yscrollcommand=scrollbar.set)
textarea.pack(pady=10)
scrollbar.config(command=textarea.yview)
billmenuframe = LabelFrame(root,text="Bill Menu",font=('times new roman',15,'bold'),fg='gold',relief='groove',bd=12,bg='gray20')
billmenuframe.pack()


cosmeticpricelabel=Label(billmenuframe,text='Cosmetic price',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
cosmeticpricelabel.grid(row=0,column=0,pady=9,padx=10)
cosmeticpriceentry= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
cosmeticpriceentry.grid(row=0,column=1,pady=9,padx=10)


grocerypricelabel=Label(billmenuframe,text='Grosery price',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
grocerypricelabel.grid(row=1,column=0,pady=9,padx=10)
groserypricelabel= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
groserypricelabel.grid(row=1,column=1,pady=9,padx=10)

drinkspricelabel=Label(billmenuframe,text='Cold Drinks price',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
drinkspricelabel.grid(row=3,column=0,pady=9,padx=10)
drinkspricelabel= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
drinkspricelabel.grid(row=3,column=1,pady=9,padx=10)

cosmetictaxlabel=Label(billmenuframe,text='Cosmetic Tax',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
cosmetictaxlabel.grid(row=0,column=2,pady=9,padx=10)
cosmetictaxlabel= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
cosmetictaxlabel.grid(row=0,column=3,pady=9,padx=10)


groserytaxlabel=Label(billmenuframe,text='Grosery Tax',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
groserytaxlabel.grid(row=1,column=2,pady=9,padx=10)
groserytaxlabel= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
groserytaxlabel.grid(row=1,column=3,pady=9,padx=10)



colddrinktaxlabel=Label(billmenuframe,text='Cold Drinks Tax',font=('Times new roman',14,'bold'),bg='gray20',fg='white')
colddrinktaxlabel.grid(row=3,column=2,pady=9,padx=10)
colddrinktaxlabel= Entry(billmenuframe,font=('times new roman',15,'bold'),width=13,bd=2)
colddrinktaxlabel.grid(row=3,column=3,pady=9,padx=10)


buttonframe=Frame(billmenuframe,bd=8,relief="groove")
buttonframe.grid(row=1,column=4)

totalButton=Button(buttonframe,text="Total",font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,command=total)
totalButton.grid(row=1,column=4,padx=20)

billButton=Button(buttonframe,text="Bill",font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,command=print_area)
billButton.grid(row=1,column=5,padx=20)


emailButton=Button(buttonframe,text="Email",font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,command=send_email)
emailButton.grid(row=1,column=6,padx=20)


printButton=Button(buttonframe,text="Print",font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,command=print_bill)
printButton.grid(row=1,column=7,padx=20)










root.mainloop()