import pickle
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
import sys
sssname=[]
sssage=[]
sssreg=[]
sssuser=[]
ssspassword=[]
ssscount=[]
import sys


from tkinter import *
import sys
def efg():
    master = Tk()
    master.title("SignUp")

    master.geometry("700x600")
    def signup():
         f4=open("user100.txt","rb")
         sssuser=pickle.load(f4)
         f4.close();
         suser=e5.get()
         if(suser in sssuser):
            messagebox.showinfo("warning","user name is already in use")
            sys.exit()
         elif(e6.get()!=e7.get()):
            messagebox.showinfo("warning","password dont match with confirm password")
            sys.exit()

         else:
          f4=open("user100.txt","wb")

         sssuser.append(suser)
         pickle.dump(sssuser,f4)
         f4.close();

         f1=open("name100.txt","rb")
         sssname=pickle.load(f1)
         f1.close();
         f1=open("name100.txt","wb")
         sname=e1.get()

         sssname.append(sname)
         pickle.dump(sssname,f1)
         f1.close();

         f2=open("age100.txt","rb")
         sssage=pickle.load(f2)
         f2.close();
         f2=open("age100.txt","wb")
         sage=e3.get()
         sssage.append(sage)
         pickle.dump(sssage,f2)
         f2.close();

         f3=open("reg100.txt","rb")
         sssreg=pickle.load(f3)
         f3.close();

         f3=open("reg100.txt","wb")
         sreg=e4.get()
         sssreg.append(sreg)
         pickle.dump(sssreg,f3)
         f3.close();


         f5=open("password100.txt","rb")
         ssspassword=pickle.load(f5)
         f5.close();
         f5=open("password100.txt","wb")
         spassword=e6.get()

         ssspassword.append(spassword)
         pickle.dump(ssspassword,f5)
         f5.close();

         f6=open("valid100.txt","rb")
         ssscount=pickle.load(f6)
         f6.close();
         f6=open("valid100.txt","wb")
         scount=0
         ssscount.append(scount)
         pickle.dump(ssscount,f6)
         f6.close();
         #print("now you can log in \n\n")
         messagebox.showinfo("T&C Worning","BY SIGNING UP IN YOU AARE AGREEING TO ALL OUR TERMS AND CONDITIONS\nFOR T&C OR HELP PLZ CONTACT 1800 123 321 OR BLOCK NUMBER:32 ,203 ")
         
         messagebox.showinfo("Sign Up","Data stored successfully")
         master.destroy()



    Label(master, text="\n\n\n").grid(row=0)
    Label(master, text="\n\t Name\t\t\t\n ").grid(row=1)
    #Label(master, text="\n\t\tLast Name\t\t\t\n").grid(row=3)
    Label(master, text="\n\t\tAge\t\t\t\t\n").grid(row=3)
    Label(master, text="\n\t\tReg No\t\t\t\t\n").grid(row=9)
    Label(master, text="\n\t\tUser ID\t\t\t\t\n").grid(row=17)
    Label(master, text="\n\t\tPassword\t\t\t\n").grid(row=19)
    Label(master, text="\n\t\tConfirm Password\t\t\t\n").grid(row=21)

    Label(master, text="\n\t Choose ur Vehicle Type\t\t\t\n ").grid(row=11)
    r7=Radiobutton(master,text="Car",value=14)
    r7.grid(row=13,column=1)
    r8=Radiobutton(master,text="Bike",value=2000)
    r8.grid(row=15,column=1)
    #Button(master3, text='Submit\t\t',height=1,width=15 , command=a1,bg="skyblue").grid(row=11, column=1)


    
    a=StringVar()
    #b=StringVar()
    c=StringVar()
    d=StringVar()
    e=StringVar()
    f=StringVar()
    e1 = Entry(master)
    #e2 = Entry(master,textvariable=b)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master)
    e6 = Entry(master,show="#")
    e7 = Entry(master,show="#")

    e1.grid(row=1, column=1)
    #e2.grid(row=3, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=9, column=1)
    e5.grid(row=17, column=1)
    e6.grid(row=19, column=1)
    e7 .grid(row=20,column=1)
    Button(master, text='Submit\t\t',height=1,width=20 ,relief="solid",command=signup,bg="skyblue",).grid(row=23, column=1, sticky=W, padx=20,pady=20)


def abc(count):

    count1=count
    master = Tk()

    def status(kk1):
        f6=open("valid100.txt","rb")
        ssscount=pickle.load(f6)
        f6.close();
        kk=kk1
        def a10():
             messagebox.showinfo("Parking Status ","you are athorized to park ur vehicle")
        def a1():
            if(ssscount[kk]%2==0):
                a10()
                ssscount[kk]=ssscount[kk]+1
            else:
                messagebox.showinfo("Parking Status "," ur vehicle is unparked")
                ssscount[kk]=ssscount[kk]+1

            f6=open("valid100.txt","wb")

            pickle.dump(ssscount,f6)
            f6.close();

        master3=Tk()
        master3.title("Parking Management System")
        master3.geometry("400x400")
        Label(master3, text="\n\t Prefered Location\t\t\t\n ").grid(row=0)
        r1=Radiobutton(master3,text="Main Gate",value=1)
        r1.grid(row=1,column=0)
        r2=Radiobutton(master3,text="Block 32,33,34",value=2)
        r2.grid(row=2,column=0)
        r3=Radiobutton(master3,text="BH1",value=3)
        r3.grid(row=3,column=0)
        r4=Radiobutton(master3,text="BH5",value=4)
        r4.grid(row=4,column=0)
        r5=Radiobutton(master3,text="BH6",value=45)
        r5.grid(row=5,column=0)
        r6=Radiobutton(master3,text="Block 55,56",value=6)
        r6.grid(row=6,column=0)
        Button(master3, text='Go',height=1,width=10 ,relief="solid", command=a1,bg="skyblue").grid(row=8, column=5)
        master3.mainloop()
        master.destroy()



    def fair(kk1):
        f6=open("valid100.txt","rb")
        ssscount=pickle.load(f6)
        f6.close();
        kk=ssscount[kk1]//2
        dd=str(kk*20)
        messagebox.showinfo("Your Fair ","Total Fair is:"+dd)
        master.destroy()

    def login(count2):
     f1=open("user100.txt","rb")
     sssuser=pickle.load(f1)
     f1.close();
     #count=count2

     f5=open("password100.txt","rb")
     ssspassword=pickle.load(f5)
     f5.close();

     f6=open("valid100.txt","rb")
     ssscount=pickle.load(f6)
     f6.close();

     username=e1.get()
     password=e2.get()
     kk=sssuser.index(username)

     if(ssspassword[kk]==password):

         messagebox.showinfo("LogIn","u r Loged In")
       #  master.destroy()
         master = Tk()
         master.title("SignUp")
         master.geometry("600x300")
         Button(master, text='\t\tTotal Fair\t\t',height=2,width=20 ,relief="solid",command=lambda:fair(kk),bg="skyblue",).grid(row=2, column=1, sticky=W, padx=50,pady=80)
         Button(master, text='\tPark/Unpark\t\t',height=2,width=20 ,relief="solid",command=lambda:status(kk),bg="skyblue",).grid(row=2, column=5, sticky=W, padx=120,pady=80)




     else:
        
         if(count2<3):

            messagebox.showinfo("LogIn","Invalid password ")
            count2=count2+1
            



    master.geometry("600x550")
    master.title("LogIn")
    Label(master, text="\n\n\n\n\n\n\n").grid(row=9)
    Label(master, text="\n\t\tUser ID\t\t\t\n").grid(row=10)
    Label(master, text="\n\t\tPassword\t\t\n").grid(row=20)

    e1 = Entry(master)
    e2 = Entry(master,show="#")


    e1.grid(row=10, column=1)
    e2.grid(row=20, column=1)
    Button(master, text='LogIn\t\t',height=1,width=20 ,command=lambda:login(count1),relief="solid",bg="skyblue",).grid(row=30, column=1, sticky=W, padx=20,pady=20)
    Button(master, text='New Users\t\t',height=1,width=20 ,command=efg,bg="skyblue",relief="solid").grid(row=50, column=0, sticky=W, padx=40,pady=40)




    mainloop( )

def ccdisplay():
    f1=open("name100.txt","rb")
    sssname=(pickle.load(f1))
    length=len(sssname)
    #print(length)
    f1.close();
    f2=open("age100.txt","rb")
    sssage=(pickle.load(f2))
    f2.close();
    f3=open("reg100.txt","rb")
    sssreg=(pickle.load(f3))
    f3.close();
    f4=open("user100.txt","rb")
    sssuser=(pickle.load(f4))
    f4.close();
    f5=open("password100.txt","rb")
    ssspassword=(pickle.load(f5))
    f5.close();
    f6=open("valid100.txt","rb")
    ssscount=(pickle.load(f6))
    f6.close();
    master = Tk()
    master.geometry("800x720")
    master.configure(bg='white')
    master.title("Admin")
    count2=100
    master.title("Admin")
    for i in range(length):
        Label(master, text="user names:").grid(row=(count2+3),column=1,pady=2,padx=50)
        Label(master, text="user age:").grid(row=(count2+8),column=1,pady=2,padx=5)
        Label(master, text="user reg no:").grid(row=(count2+13),column=1,pady=2,padx=15)
        Label(master, text="user id:").grid(row=(count2+18),column=1,pady=2,padx=15)
        Label(master, text="password:").grid(row=(count2+23),column=1,pady=2,padx=15)
        Label(master, text="slot status is:").grid(row=(count2+28),column=1,pady=2,padx=15)
        Label(master, text="________________________________________").grid(row=(count2+38),column=1,pady=2,padx=15)
        Label(master, text="________________________________________").grid(row=(count2+38),column=3,pady=2,padx=15)
        
        Label(master, text=sssname[i]).grid(row=count2+3,column=3,pady=2,padx=15)
        Label(master, text=sssage[i]).grid(row=count2+8,column=3,pady=2,padx=15)
        Label(master, text=sssreg[i]).grid(row=count2+13,column=3,pady=2,padx=15)
        Label(master, text=sssuser[i]).grid(row=count2+18,column=3,pady=2,padx=15)
        Label(master, text=ssspassword[i]).grid(row=count2+23,column=3,pady=2,padx=15)
        Label(master, text=ssscount[i]).grid(row=count2+28,column=3,pady=2,padx=15)
        #Label(master, text="  ").grid(row=(count2+30),column=1,pady=0,padx=0)
        count2=count2+50

def ccxdisplay():
    f1=open("name100.txt","rb")
    sssname=(pickle.load(f1))
    length=len(sssname)
    #print(length)
    f1.close();
    f2=open("age100.txt","rb")
    sssage=(pickle.load(f2))
    f2.close();
    f3=open("reg100.txt","rb")
    sssreg=(pickle.load(f3))
    f3.close();
    f4=open("user100.txt","rb")
    sssuser=(pickle.load(f4))
    f4.close();
    f5=open("password100.txt","rb")
    ssspassword=(pickle.load(f5))
    f5.close();
    f6=open("valid100.txt","rb")
    ssscount=(pickle.load(f6))
    f6.close();
    master = Tk()
    master.geometry("800x720")
    master.title("Admin")
    count2=100
    master.title("Admin")
    Label(master, text="user names:").grid(row=(count2+3),column=1,pady=2,padx=50)
    Label(master, text="user age:").grid(row=(count2+8),column=1,pady=2,padx=5)
    Label(master, text="user reg no:").grid(row=(count2+13),column=1,pady=2,padx=15)
    Label(master, text="user id:").grid(row=(count2+18),column=1,pady=2,padx=15)
    Label(master, text="password:").grid(row=(count2+23),column=1,pady=2,padx=15)
    Label(master, text="slot status is:").grid(row=(count2+28),column=1,pady=2,padx=15)
    Label(master, text=sssname).grid(row=count2+3,column=3,pady=2,padx=15)
    Label(master, text=sssage).grid(row=count2+8,column=3,pady=2,padx=15)
    Label(master, text=sssreg).grid(row=count2+13,column=3,pady=2,padx=15)
    Label(master, text=sssuser).grid(row=count2+18,column=3,pady=2,padx=15)
    Label(master, text=ssspassword).grid(row=count2+23,column=3,pady=2,padx=15)
    Label(master, text=ssscount).grid(row=count2+28,column=3,pady=2,padx=15)
        #Label(master, text="  ").grid(row=(count2+30),column=1,pady=0,padx=0)
    #master5.destroy()
def c1list(ss):
    if(ss==1):
        ccdisplay()
    else:
        ccxdisplay()


def cccdisplay():
    def check():
        adminuser=str(e5.get())
        adminpass=str(e6.get())
        if((adminuser=='sayak205')and(adminpass=='iamadmin')):
            #ccdisplay()
            #master6=Tk()
            #master6.geometry("250x205")
            #master6.title("Admin Login")
            #Label(master5, text="\n").grid(row=9)
            messagebox.showinfo("ADMIN ","Welcome Back Sir ,Good To Have U Again!!!")
            
            Button(master5, text='Display in format',height=1,width=15 , command=ccdisplay,relief="solid",bg="skyblue").grid(row=50, column=1,pady=30,padx=30)
            Button(master5, text='Display Admin format',height=1,width=18, command=ccxdisplay,relief="solid",bg="skyblue").grid(row=60, column=1,pady=30,padx=30)
            


        else:
            messagebox.showinfo("warning","sorry something went wrong plz try again later")
            master5.destroy()
    master1.destroy()
    master5=Tk()
    master5.geometry("500x500")
    master5.title("Admin Login")
    Label(master5, text="\n").grid(row=9)
    Label(master5, text="Admin ID").grid(row=10,column=1,pady=30,padx=30)
    Label(master5, text="Password").grid(row=20,column=1,pady=20,padx=30)
    Label(master5, text=sssname).grid(row=10,column=3,pady=20,padx=30)
    Label(master5, text=sssage).grid(row=20,column=3,pady=20,padx=30)
    e5 = Entry(master5)
    e6 = Entry(master5,show="#")
    e5.grid(row=10, column=2)
    e6.grid(row=20, column=2)

    Button(master5, text='Get IN\t\t',height=1,width=15 , command=check,relief="solid",bg="skyblue").grid(row=40, column=6)





master1=Tk()
master1.title("Parking Management System")
master1.geometry("1500x1500")
master1.configure(bg='white')
label_1=Label(master1,text="PARKING MANAGMENT SYSTEM ",bd=0,relief="solid",font="Times 32",bg='green').grid(row=1, column=0)
#label_1=Label(master1,text="ProCuRatio ",bd=0,relief="solid",font="Times 32",bg='cyan').grid(row=0, column=11,padx=5)
#label_1=Label(master1,text="(PMS)_______",bd=0,relief="solid",font="Times 32",bg='cyan').grid(row=0, column=12)

#label_1.grid()

#label_one.config(fontsize='50')
#Label.config(font=("PMS",44))
#Label(master1, text="\n\nPMS\n\n").grid(row=0)
#Label(master1, text="\t\t\t").grid(column=10)
img = ImageTk.PhotoImage(file="3.jpg")
#Displaying it
imglabel = tk.Label(master1, image=img).grid(row=0, column=0)
Button(master1, text='LogIn\t\t',height=2,width=20 , command=lambda:abc(0),relief="solid",bg="skyblue",font="Times 11").grid(row=0, column=0, sticky=W,pady=80,padx=10)
Button(master1, text='Sign Up\t\t',height=2,width=20 ,command=efg,bg="skyblue",relief="solid",font="Times 11").grid(row=1, column=0, sticky=W,pady=30,padx=10)
Button(master1, text='Quit\t\t',height=2,width=15 , command=master1.destroy,bg="skyblue",relief="solid",font="Times 11").grid(row=0, column=1, sticky=W,pady=25,padx=50)
Button(master1, text='Admin\t\t',height=2,width=15 , command=cccdisplay,bg="skyblue",font="Times 11",relief="solid").grid(row=1, column=1,sticky=W,pady=10,padx=50)


mainloop()










