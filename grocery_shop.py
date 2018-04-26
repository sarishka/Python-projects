from tkinter import *
from tkinter import messagebox
grocery=Tk()
count=0
frame=Frame(grocery)
def addrec():
    f=open('projectdetail.txt','a')
    pid=s1.get()
    pname=s2.get()
    price=s3.get()
    man=s4.get()
    valid=s5.get()
    f.writelines(pid.ljust(20)+pname.ljust(10)+price.ljust(10)+man.ljust(10)+valid.ljust(10)+"\n")
    f.close()
    grocery.configure(background="lavender")
    print("Record added successfully!")
    messagebox.showinfo("Information","Record Added Successfully")
def nextrec():
    global count
    #print(count)
    f=open('projectdetail.txt','r')
    tr=len(f.readlines())
    tr=tr-1
    f.seek(0)
    i=0
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    print("The next record is:")
    print("Product Id:",l1[0])
    print("Product Name:",l1[1])
    print("Price:",l1[2])
    print("Manufacturing date:",l1[3])
    print("Validity",l1[4])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    if(count!=tr):
        count=count+1
    f.close()
    grocery.configure(background="bisque")

    
def prev():
    f=open('projectdetail.txt','r')
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])	# If we want to print on console screen
    s1.set(l1[0])	
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    if (count!=0):
        count=count-1
    f.close()
    grocery.configure(background="thistle2")
def update():
    pid=s1.get()
    pname=s2.get()
    price=s3.get()
    man=s4.get()
    valid=s5.get()
    f=open("projectdetail.txt","r")
    h=f.readlines()
    f.close()
    f=open("projectdetail.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=pid):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(10)+j[3].ljust(10)+j[4].ljust(10)+"\n")
        else :
            f.writelines(pid.ljust(20)+pname.ljust(10)+price.ljust(10)+man.ljust(10)+valid.ljust(10)+"\n")
            flag=1
    f.close()
    grocery.configure(background="thistle2")
    print("Record Updated Successfully!")
    messagebox.showinfo("Information","Record Updated Successfully")
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("projectdetail.txt","r")
    h=f.readlines()
    f.close()
    f=open("projectdetail.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(10)+j[3].ljust(10)+j[4].ljust(10)+"\n")
    f.close()
    grocery.configure(background="floral white")
    print("Record Deleted Successfully!")
    messagebox.showinfo("Information","Record Removed Successfully")
def search():
    k=s1.get()
    f=open("projectdetail.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            print(k)
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
    grocery.configure(background="pink1")
def lr():
    f=open("projectdetail.txt",'r')       
    de=sum(1 for i in open("projectdetail.txt"))-1
    print(de)
    k=f.readlines()[de]
    j=k.split()
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
    grocery.configure(background="orchid1")
def fr():
    global count
    count = 1
    f=open('projectdetail.txt','r')
    k=f.readlines()[0]
    j=k.split()
    print(j)
    s1.set(j[0])
    s2.set(j[1])
    s3.set(j[2])
    s4.set(j[3])
    s5.set(j[4])
    f.close()
    grocery.configure(background="PaleTurquoise1")
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l0=Label(grocery,text="---------EUROPA PYTHON--------")
l1=Label(grocery,text="PRODUCT ID")
l2=Label(grocery,text="PRODUCT NAME")
l3=Label(grocery,text="PRICE(in Rs.)")
l4=Label(grocery,text="MANUFACTURING DATE")
l5=Label(grocery,text="VALIDITY")
t1=Entry(grocery,textvariable=s1)
t2=Entry(grocery,textvariable=s2)
t3=Entry(grocery,textvariable=s3)
t4=Entry(grocery,textvariable=s4)
t5=Entry(grocery,textvariable=s5)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1=Button(grocery,text="Next Record", command=nextrec)
b2=Button(grocery,text="Insert Record", command=addrec)
b3=Button(grocery,text="Delete Record", command=delete)
b4=Button(grocery,text="Search Record", command=search)
b5=Button(grocery,text="Update Record", command=update)
b7=Button(grocery,text="Last Record", command=lr)
b6=Button(grocery,text="First Record", command=fr)
b8=Button(grocery,text="Previous Record", command=prev)
b1.grid(row=7,column=3)
b2.grid(row=9,column=1)
b3.grid(row=9,column=3)
b4.grid(row=4,column=3)
b5.grid(row=9,column=2)
b6.grid(row=7,column=1)
b7.grid(row=7,column=2)
b8.grid(row=2,column=3)
grocery.mainloop()
