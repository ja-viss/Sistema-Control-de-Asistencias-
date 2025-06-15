from controlador import Controlador
import tkinter as tk
from tkinter import *
from tkinter import messagebox

controlador = Controlador()

style_title = ("arial", 24, "bold")
style_letra_label = ("arial", 19, "bold")
style_letra_button = ("arial", 15, "bold")

root = Tk()
root.geometry("720x500")
root.configure(background="#ffffff")
root.title("Jardin de Infancia UNET")
root.iconbitmap("logo.ico") 
root.resizable(0,0)

title_label_login = Label(root, text="Sistema de Control de Asistencias", font=style_title, background="#ffffff", fg="#1F3A93")
title_label_login.pack()
title_label_login = Label(root, text="J.I UNET", font=style_title, background="#ffffff", fg="#1F3A93")
title_label_login.pack()

usuario_label = Label(root, text="Usuario", background="#ffffff", font=style_letra_label)
usuario_label.place(x=450, y=120)

entry_usuario = Entry(root,bd=2, width=25, highlightthickness=2, highlightcolor="black")
entry_usuario.place(x=430, y=165)

pass_label1 = Label(root, text="Contraseña", background="#ffffff", font=style_letra_label, )
pass_label1.place(x=440, y=230)

entry_pass = Entry(root,bd=2, width=25, highlightthickness=2, highlightcolor="black")
entry_pass.place(x=430, y=275)

def verificar_usuario():
    usser = entry_usuario.get()
    pasword = entry_pass.get()
    resultado = controlador.verificacion(usser, pasword)
    if resultado == 1:
        messagebox.showinfo("Inicio de sesión", "Bienvenido")
    else:
        messagebox.showerror("Inicio de sesión", "El usuario o la contraseña son incorrectos")

button_login = Button(root,  text="continuar", bd=2, background="#1F3A93", fg="white", font=style_letra_button, command=verificar_usuario)
button_login.place(x=470, y=350)

image1 = PhotoImage(file="logo_login.png")
image_label = Label(root, image=image1)
image_label.image = image1
image_label.place(x=60,y=110)

root.mainloop()