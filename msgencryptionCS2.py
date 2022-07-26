from tkinter import *
from tkinter import messagebox #for popup incase wrong entry
import base64
screen = Tk()
screen.geometry("420x420")
screen.title("Encryption and Decryption")
screen.configure(bg="silver")
#label

def encrypt():
    global password1
    password1 = code.get()

    if (password1==""):
         messagebox.showerror("Error","Please create a password")
         exit()
    elif(len(password1)>=3):
        
        screen1=Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x250")
        screen1.configure(bg="cyan")

        message=text1.get(1.0,END)
        encryptmsg=message.encode("ascii")
        base64bytes=base64.b64encode(encryptmsg)
        encrypt = base64bytes.decode("ascii")

        Label(screen1,text="Text Is Encrypted\n",font="impack 10 bold").place(x=5,y=6)
        text2=Text(screen1,font="30",bd=4,wrap=WORD)
        text2.place(x=2,y=30,width=390,height=180)
        text2.insert(END,encrypt)
    else:
        messagebox.showerror("Error !","Password length Insuffcient !!!  atleast 3 characters required ")

def decrypt():
    password=code.get()
    if password==password1:
         screen2=Toplevel(screen)
         screen2.title("Encryption")
         screen2.geometry("400x250")
         screen2.configure(bg="cyan")

         message=text1.get(1.0,END)
         decryptmsg=message.encode("ascii")
         base64bytes=base64.b64decode(decryptmsg)
         decrypt = base64bytes.decode("ascii")

         Label(screen2,text="Text Is Decrypted",font="impack 10 bold").place(x=5,y=6)
         text2=Text(screen2,font="30",bd=4,wrap=WORD)
         text2.place(x=2,y=30,width=390,height=180)
         text2.insert(END,decrypt)
    elif(password==""):
        messagebox.showerror("Error","Please enter the password")   
    elif(password!=password1):
        messagebox.showerror("Error","Wrong password !!! please try again")  
    
    
def cls():
    text1.delete(1.0,END)
    code.set("")




Label(screen,text="This Is Encryption & Decryption Program.\n Enter The Message To Be Encrypted",font="impack 12 bold",bg="white").place(x=25,y=1,)

text1=Text(screen,font="20")
text1.place(x=5,y=45,width=400,height=120)
#label
Label(screen,text="Enter the secret key",font="impack 11 bold").place(x=135,y=175)
#entry
code=StringVar()
Entry(textvariable=code,bd=4,font="20",show="*").place(x=120,y=210)#text entry for password
#button
Button(screen,text="ENCRYPT",font="arial 14 bold",bg="green", fg="white",command=encrypt).place(x=40,y=280,width=150)
Button(screen,text="DECRYPT",font="arial 14 bold",bg="green", fg="white",command=decrypt).place(x=235,y=280,width=150)
Button(screen,text="CLEAR",font="arial 14 bold",bg="RED", fg="white",command=cls).place(x=125,y=370,width=190)

mainloop()
