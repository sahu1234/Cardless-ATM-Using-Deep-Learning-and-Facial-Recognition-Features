import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from tkinter import *
import tkinter as tk
from subprocess import call
from tkinter import ttk, LEFT, END
from tkinter.filedialog import askopenfilename
from PIL import Image , ImageTk

root=tk.Tk()
root.geometry("1000x1000")
root.configure(background="red2")

global file
#global f
def Browse():
    from PIL import Image
    file = askopenfilename(title='Select File To Send ',
                         filetypes=[('All files', '*.*'), ('all files','.txt')])

    f=file.split("/").pop()
    file=file.replace("/","\\")
    print(f)
    print(file)
    Selected=Label(root,text="Selected File :"+str(f),width=20,height=1,background="white",foreground="black",font=("Tempus Sans ITC",15,"bold"))
    Selected.place(x=5,y=400)
    #return f
    return file

def Send():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    #global f
    #global file
    fromaddr = entry1.get()
    toaddr = entry3.get()


    msg = MIMEMultipart()


    msg['From'] = fromaddr


    msg['To'] =  toaddr


    password = entry2.get()

    msg['Subject'] = "Patient Report :"


    body = body1.get('1.0', 'end-1c')


    msg.attach(MIMEText(body, 'plain'))


    #filename = f
    file=r"C:\Users\Admin\Desktop\PROJECTS\BREATH_DETECTION\Report.txt"
    attachment = open(file, "rb")


    p = MIMEBase('application', 'octet-stream')


    p.set_payload((attachment).read())


    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % file)


    msg.attach(p)


    s = smtplib.SMTP('smtp.gmail.com', 587)


    s.starttls()

    try:
        s.login(fromaddr,password)


        text = msg.as_string()


        s.sendmail(fromaddr, toaddr, text)

        Success = Label(root, text="Mail Sent Successfully !", width=20, height=1, background="white", foreground="black",
                         font=("Tempus Sans ITC", 15, "bold"))
        Success.place(x=10, y=500)
        print("Mail Sent Suucessfully !")

    except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
        Success = Label(root, text="Oops ! Mail Not Sent !", width=20, height=1, background="white",
                        foreground="black",
                        font=("Tempus Sans ITC", 15, "bold"))
        Success.place(x=10, y=500)
        print("Oops Mail Not Sent !")


    finally:
        s.quit()








#body = Text(root, font="Tahoma", bd=8,height=15)
#body.config(bg="pink", height=15)
#body.pack()

MESSAGE=Label(root,text="Message Body",width=15,height=1,background="white",foreground="black",font=("Tempus Sans ITC",15,"bold"))
MESSAGE.place(x=600,y=5)
body1=Text(root, font="Tahoma", bd=4,height=15,width=40)
body1.place(x=600,y=50)

S_MAIL=tk.Label(root,text="Enter Your Mail :",width=15,height=3,background="white",foreground="black",font=("Tempus Sans ITC",19,"bold"))
S_MAIL.place(x=5,y=5)
entry1=Entry(root,bd=2,width=50)
entry1.place(x=260,y=20)

PASS=tk.Label(root,text="Enter Password:",width=15,height=3,background="white",foreground="black",font=("Tempus Sans ITC",19,"bold"))
PASS.place(x=5,y=100)
entry2=Entry(root,bd=2,width=50,show="#")
entry2.place(x=260,y=120)

R_MAIL=tk.Label(root,text="Recievrs Mail ID : ",width=15,height=3,background="white",foreground="black",font=("Tempus Sans ITC",19,"bold"))
R_MAIL.place(x=5,y=200)
entry3=Entry(root,bd=2,width=50)
entry3.place(x=260,y=220)

BROWSE=tk.Button(root,text="Browse File",command=Browse)
BROWSE.place(x=400,y=400)

SEND=tk.Button(root,text="SEND MAIL",command=Send)
SEND.place(x=530,y=400)

root.mainloop()