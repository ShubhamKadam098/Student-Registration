from cgitb import text
from msilib.schema import ComboBox
from tkinter import *
from tkinter import font
from tkinter import ttk
import tkinter.messagebox as Messagebox
from turtle import clear
from webbrowser import get

#Screen Configuration
Screen = Tk()
Screen.resizable(False,False)
Screen.title("Python Project")
Screen.geometry("750x650")
Screen.config(bg="azure3")

#Submit Button Mechanism
def Submit():
    try:
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost", port=3306, user="root" , password="{Password}", database="Student_Info" )
        mycursor = mydb.cursor()
    except:
        Messagebox.showerror("Error In Connection", "Can't connect to the Database")

    First_Name=E1.get()
    Middle_Name=E2.get()
    Last_Name=E3.get()

    try:
        Roll_No=int(E4.get())
    except:
        Messagebox.showinfo("Field Error!","Enter valid Roll Number")

    Gender=int(Gen.get())

    Branch=E6.get()

    Year=E7.get()

    
    try:
        temp_contact=int(E8.get())
    except:
        Messagebox.showinfo("Field Error!","Enter valid Contact Number")

    Contact=E8.get()

    Email=E9.get()

    # Errors
    if First_Name=="" or Middle_Name=="" or Last_Name=="":
        Messagebox.showinfo("Field Error!","Name can't be Empty") 
    elif Email=="":
        Messagebox.showinfo("Field Error!","Email can't be Empty")
    elif len(Contact)!=10:
        Messagebox.showinfo("Field Error!","Contact Number is not Valid")
    elif Roll_No>120:
        Messagebox.showinfo("Field Error!","Invalid Roll Number")
    elif Branch=="Select the Branch":
        Messagebox.showinfo("Field Error!","Enter the valid Branch")
    elif Year=="Select the Year":
        Messagebox.showinfo("Field Error!","Enter the valid Year")
    else:
        
        try:
            Insert= ("INSERT INTO Registration(First_Name,Middle_Name,Last_Name,Roll_No, Gender,Branch,Year, Contact,Email)""VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
            Data = (First_Name,Middle_Name,Last_Name,Roll_No, Gender,Branch,Year, Contact,Email)
            mycursor.execute(Insert, Data)
            mydb.commit()
            Messagebox.showinfo("Registration","Information Registered Successfully")
        except:
            Messagebox.showinfo("Error 404!", "Error inserting registration data")
        

#Clear Button Mechanism
def Clear():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E6.current(0)
    E7.current(0)
    E8.delete(0,END)
    E9.delete(0,END)

#View Button Mechanism
def View():
    try:
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost", port=3306, user="root" , password="12345678", database="Student_Info" )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Registration;")
        result = mycursor.fetchall()
        for row in result:
            print(row,'\n')

    except:
        Messagebox.showerror("Error In Connection", "Can't connect to the Database")
    


#Interface
Message = Message(Screen, text="Student Registration", relief = RAISED, width=300, font="ariel 20 bold", bg='#873e23' , fg="white", bd=4)
Message.pack(pady=30)

Image=PhotoImage(file='E:\deskptop data\SHUBHAM\pp project\images\Kirti_Logo.png')
Logo=Label(Screen, image=Image, bd=5, bg ='azure3')
Logo.place(x=0, y=25)

Name=Label(Screen, text="Name: ", font="arial 10 bold" ,bg='azure3')
Name.place(x=40, y=150)

#First Name Label & Entry
N1=Label(Screen, text="First Name", font="arial 10 ",bg='azure3')
N1.place(x=170, y=120)
E1=Entry(Screen, bd=5,width=25)
E1.place(x=140, y=150)
#Middle Name Label & Entry
N2=Label(Screen, text="Middle Name", font="arial 10 ",bg='azure3')
N2.place(x=368, y=120)
E2=Entry(Screen, bd=5,width=25)
E2.place(x=340, y=150)
#Last Name Label & Entry
N3=Label(Screen, text="Last Name", font="arial 10 ",bg='azure3')
N3.place(x=575, y=120)
E3=Entry(Screen, bd=5,width=25)
E3.place(x=540, y=150)

#Roll No. Label & Entry
R1=Label(Screen, text="Roll No.", font="arial 10 bold",bg='azure3')
R1.place(x=40, y=250)
E4=Entry(Screen, bd=5,width=15)
E4.place(x=140, y=250)

#Gender Label & Entry
Gender=Label(Screen, text="Gender : ",font="arial 10 bold",bg='azure3')
Gender.place(x=350, y=250)

Gen=IntVar()
G1 = Radiobutton(Screen, text="Male",variable=Gen, value=1, cursor="hand2",bg='azure3')
G1.place(x=450, y=250)
G2 = Radiobutton(Screen, text="Female",variable=Gen, value=2, cursor="hand2",bg='azure3')
G2.place(x=550, y=250)
G3 = Radiobutton(Screen, text="Other",variable=Gen, value=3, cursor="hand2",bg='azure3')
G3.place(x=650, y=250)


#Branch
Branch=Label(Screen, text="Branch : ", font="arial 10 bold",bg='azure3')
Branch.place(x=40, y=350)
E6=ttk.Combobox(Screen, state='readonly',justify='center',width=30)
E6['values']=("Select the Branch","Bsc IT","Bsc CS","Other")
E6.current(0)
E6.place(x=140, y=350)

#Year
Year=Label(Screen, text="Year : ", font="arial 10 bold",bg='azure3')
Year.place(x=400, y=350)
E7=ttk.Combobox(Screen, state='readonly',justify='center',width=30)
E7['values']=("Select the Year","First Year","Second Year","Third Year")
E7.current(0)
E7.place(x=475, y=350)

# Contact Label & Entry
Contact=Label(Screen, text="Contact : ",font="arial 10 bold",bg='azure3')
Contact.place(x=40, y=450)
E8=Entry(Screen, bd=5,width=35)
E8.place(x=140, y=450)

#Email Label & Entry
Email=Label(Screen, text="Email : ", font="arial 10 bold",bg='azure3')
Email.place(x=400, y=450)
E9=Entry(Screen, bd=5,width=35)
E9.place(x=475, y=450)

#Submit Button
my_button = Button(Screen, text="Submit", command=Submit, font="bold" , bd=1)
my_button.place(x=350, y=600)

#Clear Button
my_button = Button(Screen, text="Clear", command=Clear ,font="bold")
my_button.place(x=550, y=600)

#View Button
my_button= Button(Screen, text="View",command=View,font="bold")
my_button.place(x=150, y=600)


Screen.mainloop()
