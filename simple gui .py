#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
root=Tk()

#the title of the gui
root.title('JONEX HOSPITAL')
root.geometry('1000x800')  
Label(root, text="JONEX HOSPITAL\n PAYMENT RECIEPT", font="arial 18").pack(pady=50)
Label(text="Date", font=8).place(x=100, y=150)
Label(text="Name", font=8).place(x=100, y=200)
Label(text="Card Num",font=8).place(x=100, y=250)
Label(text="Pay Type", font=8).place(x=100, y=300)
Label(text="Old Bill", font=8).place(x=100, y=350)
Label(text="New Bill", font=8).place(x=100, y=400)
Label(text="Amount", font=8).place(x=100, y=450)
Label(text="Balance", font=8).place(x=100, y=500)
Label(text="Cashier", font=8).place(x=100, y=550)

#variable declaration
dateValue=StringVar()
nameValue=StringVar()
cardnumValue=StringVar()
paytypeValue=StringVar()
oldbillValue=IntVar()
newbillValue=IntVar()
amountValue=IntVar()
balanceValue=IntVar()
cashierValue=StringVar()

#getting input
dateEntry=Entry(root, textvariable=dateValue)
nameEntry=Entry(root, textvariable=nameValue)
cardnumEntry=Entry(root, textvariable=cardnumValue)
paytypeEntry=Entry(root, textvariable=paytypeValue)
oldbillEntry=Entry(root, textvariable=oldbillValue)
newbillEntry=Entry(root, textvariable=newbillValue)
amountEntry=Entry(root, textvariable=amountValue)
balanceEntry=Entry(root, textvariable=balanceValue)
cashierEntry=Entry(root, textvariable=cashierValue)

#spcifying where the various inputs should be
dateEntry.place(x=200,y=150, width=600)
nameEntry.place(x=200,y=200, width=600, height=200)
cardnumEntry.place(x=200,y=250, width=600)
paytypeEntry.place(x=200,y=300, width=600, height=10)
oldbillEntry.place(x=200,y=350, width=600)
newbillEntry.place(x=200,y=400, width=600)
amountEntry.place(x=200,y=450, width=600)
balanceEntry.place(x=200,y=500, width=600)
cashierEntry.place(x=200,y=550)

root.mainloop()


# In[ ]:





# In[ ]:




