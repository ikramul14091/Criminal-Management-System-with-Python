from tkinter import*
from PIL import ImageTk   #pip install pillow
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("650x500+100+50")
        self.root.resizable(False,False)

        self.Password=StringVar()
        self.Username=StringVar()

        #----BG Image---
        self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #---Login Frame---
        Frame_login=Frame(self.root,bg="gray")
        Frame_login.place(x=170,y=80,height=350,width=300)

        title=Label(Frame_login,text="Login",font=("arial",20,"bold"),bg="#d25d17",fg="white").place(x=90,y=25,height=40,width=120)
        desc=Label(Frame_login,text="Log-in Criminal Management System",font=("Goudy old style",12,"bold"),bg="gray",fg="white").place(x=28,y=65)

        lbl_user=Label(Frame_login,text="Username:",font=("Goudy old style",15,"bold"),fg="white",bg="gray").place(x=30,y=110)
        self.txt_user=Entry(Frame_login,font=("times new roman",13),bd=0,bg="lightgray")
        self.txt_user.place(x=35,y=140,width=230,height=25)

        lbl_pass=Label(Frame_login,text="Password:",font=("Goudy old style",15,"bold"),fg="white",bg="gray").place(x=30,y=170)
        self.txt_pass=Entry(Frame_login,font=("times new roman",13),bd=0,bg="lightgray")
        self.txt_pass.place(x=35,y=200,width=230,height=25)

        forget_btn=Button(Frame_login,text="Forget Password?",bg="gray",fg="white",bd=0,font=("times new roman",12)).place(x=90,y=230)
        login_btn=Button(self.root,command=self.login_function,text="Log-in",fg="white",bg="#d25d17",bd=0,font=("times new roman",15)).place(x=243,y=360,width=150,height=28)


    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.txt_pass.get()!="@ikramul55" or self.txt_user.get()!="ikramul91":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        
        else:
            messagebox.showinfo("Welcome",f"Welcome to Criminal Management System\nName: {self.txt_user.get()}\nYour Password: {self.txt_pass.get()}",parent=self.root)




root=Tk()
obj=Login(root)
root.mainloop()