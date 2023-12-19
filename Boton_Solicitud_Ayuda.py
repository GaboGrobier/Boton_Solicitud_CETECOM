import tkinter as tk
from tkinter import messagebox
from socket import socket
import socket
from email.message import EmailMessage
import smtplib
from tkinter import *


app = tk.Tk()

imagen = PhotoImage(file="vina.png")
lbl_imagen = Label(app, image = imagen).place (x=100,y=50)


app.geometry('430x300')
app.configure(background='white')
tk.Wm.wm_title(app, "SOS Cetecom")
tk.Label (text='Ingrese su nombre: ', font=("Arial",10), bg="white", fg="black").grid(row=0, column=2)
txt_nombre=tk.Entry (width=50, bg="white")
txt_nombre.grid(row=0, column=4) 
tk.Button(text='Enviar Solicitud', command=lambda:(correo(txt_nombre.get())), font=("Arial", 10),
bg="orange", fg="black").grid(row=4, column=4)



def correo(nombre_docente):

    docente_val = (len(nombre_docente.replace(" ", "")))
    if docente_val != 0:
        nombre_host=socket.gethostname()
        remitente="salas.fol.vina@gmail.com"
        destinatario="cetecom_vina@duoc.cl"
        contenido="Docente que solicita ayuda: %s" % nombre_docente
        email=EmailMessage()
        email["From"]=remitente
        email["To"]=destinatario
        email["Subject"]="Solicitud Ayuda %s" % nombre_host
        email.set_content (contenido)
        smtp=smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, "")
        smtp.sendmail(remitente, destinatario, email.as_string())
        smtp.quit()
        messagebox.showinfo('Info', 'Solicitud Enviada')
    else:
        messagebox.showerror('¡CUIDADO!', '¡Recuerde escribir su nombre!')
        


app.mainloop()
