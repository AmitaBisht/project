from tkinter import*
import random
import time

root = Tk()
root.title("RESTAURANT MANAGEMENT SYSTEM")

F1=Frame(root,width=1500,height=50,bg="blue")
F1.pack(side=TOP)
           
F=Frame(root)
F.pack(side=LEFT)

localtime=time.asctime(time.localtime(time.time()))

lbl=Label(F1,font=("arial",50,"bold"),text="RESTAURANT MANAGEMENT SYSTEM",fg="Blue",bd=10,anchor='w')
lbl.grid(row=0,column=0)
lbl=Label(F1,font=("arial",20,"bold"),text=localtime,fg="Blue",bd=10,anchor='w')
lbl.grid(row=1,column=0)

def price():
    root1 = Tk()
    root1.geometry("600x220+0+0")
    root1.title("Price List")
    lbl= Label(root1, font=('aria', 15, 'bold','underline'), text="ITEM", fg="black", bd=5)
    lbl.grid(row=0, column=0)
    lbl= Label(root1, font=('aria', 15, 'bold','underline'), text="PRICE", fg="black", anchor=W)
    lbl.grid(row=0, column=3)
    
    lbl= Label(root1, font=('aria', 15, 'bold','italic'), text="Fries Meal", fg="blue", anchor=W)
    lbl.grid(row=1, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="20", fg="blue", anchor=W)
    lbl.grid(row=1, column=3)

    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="Lunch Meal", fg="blue", anchor=W)
    lbl.grid(row=2, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="40", fg="blue", anchor=W)
    lbl.grid(row=2, column=3)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="Burger Meal", fg="blue", anchor=W)
    lbl.grid(row=3, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="35", fg="blue", anchor=W)
    lbl.grid(row=3, column=3)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="Pizza Meal", fg="blue", anchor=W)
    lbl.grid(row=4, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="50", fg="blue", anchor=W)
    lbl.grid(row=4, column=3)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="Cheese Burger", fg="blue", anchor=W)
    lbl.grid(row=5, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="50", fg="blue", anchor=W)
    lbl.grid(row=5, column=3)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="Drinks", fg="blue", anchor=W)
    lbl.grid(row=6, column=0)
    lbl = Label(root1, font=('aria', 15, 'bold','italic'), text="30", fg="blue", anchor=W)
    lbl.grid(row=6, column=3)

    root.mainloop()

def Totalcost():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    order.set(randomRef)

    costf =float(fries.get())
    costL= float(Lunch.get())
    costb= float(Burger.get())
    costp= float(pizza.get())
    costc= float(Cheesse.get())
    costd= float(Drinks.get())

    costoffries = costf*20
    costoflunch = costL*40
    costofburger = costb*35
    costofpizza = costp*50
    costofcheesse= costc*50
    costofdrinks = costd*30

    costofmeal = "Rs.",str('%.2f'% (costoffries +  costoflunch + costofburger + costofpizza + costofcheesse + costofdrinks))
    PayTax=((costoffries +  costoflunch + costofburger + costofpizza +  costofcheesse + costofdrinks)*0.3)
    Totalcost=(costoffries +  costoflunch + costofburger + costofpizza  + costofcheesse + costofdrinks)
    Ser_Charge=((costoffries +  costoflunch+ costofburger + costofpizza + costofcheesse + costofdrinks)/100)
    Servic="Rs.",str('%.2f'% Ser_Charge)
    Gst_charge=((costoffries +  costoflunch+ costofburger + costofpizza + costofcheesse + costofdrinks)/80)
    Gstp="Rs.",str('%.2f'% Gst_charge)
    OverAllCost="Rs.",str( PayTax + Totalcost + Ser_Charge+Gst_charge)
    PaidTax="Rs.",str('%.2f'% PayTax)

    Service.set(Servic)
    Cost.set(costofmeal)
    tax.set(PaidTax)
    Gst.set(Gstp)
    Total.set(OverAllCost)


def exit1():
    root.destroy()

def reset():
    order.set("")
    fries.set("")
    Lunch.set("")
    Burger.set("")
    pizza.set("")
    Cheesse.set("")
    Drinks.set("")
    Cost.set("")
    Service.set("")
    tax.set("")
    Gst.set("")
    Total.set("")
    

order=StringVar()

lbl1 = Label(F, font=( 'aria' ,16, 'bold','italic' ),text="Order No.",fg="Red",bd=10,anchor='w')
lbl1.grid(row=0,column=0)
txt1 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=order, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt1.grid(row=0,column=1)

fries=StringVar()

lbl2 = Label(F, font=( 'aria' ,16, 'bold','italic' ),text="Fries Meals",fg="Red",bd=10,anchor='w')
lbl2.grid(row=1,column=0)
txt2 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=fries , bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt2.grid(row=1,column=1)
Lunch=StringVar()

lbl3 = Label(F, font=( 'aria' ,16, 'bold','italic' ),text="Lunch Meals",fg="Red",bd=10,anchor='w')
lbl3.grid(row=2,column=0)
txt3 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Lunch , bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt3.grid(row=2,column=1)

Burger=StringVar()


lbl4 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Burger Meals",fg="Red",bd=10,anchor='w')
lbl4.grid(row=3,column=0)
txt4 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Burger, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt4.grid(row=3,column=1)

pizza=StringVar()

lbl5 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Pizza Meals",fg="Red",bd=10,anchor='w')
lbl5.grid(row=4,column=0)
txt5 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=pizza, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt5.grid(row=4,column=1)

Cheesse=StringVar()

lbl6 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Cheesse Burger",fg="Red",bd=10,anchor='w')
lbl6.grid(row=5,column=0)
txt6 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Cheesse, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt6.grid(row=5,column=1)

Drinks=StringVar()

lbl7 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Drinks",fg="Red",bd=10,anchor='w')
lbl7.grid(row=0,column=5)
txt7 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Drinks, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt7.grid(row=0,column=6)

Cost=StringVar()

lbl8 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Cost",fg="Red",bd=10,anchor='w')
lbl8.grid(row=1,column=5)
txt8 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Cost, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt8.grid(row=1,column=6)

Service=StringVar()

lbl9 = Label(F, font=( 'aria' ,16, 'bold','italic' ),text="Service tax",fg="Red",bd=10,anchor='w')
lbl9.grid(row=2,column=5)
txt9 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Service, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt9.grid(row=2,column=6)

tax=StringVar()

lbl10 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Tax",fg="Red",bd=10,anchor='w')
lbl10.grid(row=3,column=5)
txt10 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=tax, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt10.grid(row=3,column=6)

Gst=StringVar()

lbl11 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="GST",fg="Red",bd=10,anchor='w')
lbl11.grid(row=4,column=5)
txt11 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Gst, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt11.grid(row=4,column=6)

Total=StringVar()

lbl12 = Label(F, font=( 'aria' ,16, 'bold' ,'italic'),text="Total",fg="Red",bd=10,anchor='w')
lbl12.grid(row=5,column=5)
txt12 = Entry(F,font=('ariel' ,16,'bold','italic'), textvariable=Total, bd=6,insertwidth=4,bg="light blue" ,justify='right')
txt12.grid(row=5,column=6)

btnPrice=Button(F,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="light blue",command=price)
btnPrice.grid(row=7, column=0)

btnTotal=Button(F,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="light blue",command=Totalcost)
btnTotal.grid(row=7, column=1)

btnreset=Button(F,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="light blue",command=reset)
btnreset.grid(row=7, column=2)

btnexit=Button(F,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="light blue",command=exit1)
btnexit.grid(row=7, column=3)


root.mainloop()
