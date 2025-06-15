from tkinter import *
from tkinter import messagebox
from controlador import Controlador

root = Tk()
root.geometry("720x500")
root.configure(background="#ffffff")
root.title("Jardin de Infancia UNET")
root.iconbitmap("logo.ico") 
root.resizable(0,0)

op = IntVar()
vari = IntVar()

menuBar = Menu(root)
root.config(menu=menuBar)
style_letra = ("Arial", 8)
style_letra_label = ("arial", 11, "bold")
style_title = ("arial", 24, "bold")
style_letra_label2 = ("arial", 9, "bold")

registromenu = Menu(menuBar, tearoff=0)

def evaluar():
    op1 = op.get()
    
    if op1 == 1:
        text1= Label(root, text="Elija el tipo de personal: ", font=style_letra_label, background="#ffffff")
        text1.place(x=100, y=150)
        text_label= Label(root, text="Mostrar Personal Administrativo: ", background="#ffffff")
        text_label.place(x=20, y=180)
        radio_admi= Radiobutton(root, bd=2, value=1, variable = vari, background="#ffffff")
        radio_admi.place(x=200, y=180)
    if op1 == 2:
        text2=Label(root, text="dos")
        text2.pack()

def registro_personal():
    
    title_label = Label(root, text="Registro de Personal", font=style_title, background="#ffffff")
    title_label.pack()
    
    id_label = Label(root, text="ID: ", font=style_letra_label, background="#ffffff")
    id_label.place(x=100, y=80)

    id_entry = Entry(root, bd=2)
    id_entry.place(x=175, y=80)
    
    cedula_label = Label(root, text="Cedula: ", font=style_letra_label, background="#ffffff")
    cedula_label.place(x=100, y=120)

    cedula_entry = Entry(root, bd=2)
    cedula_entry.place(x=175, y=120)
    
    nombre_label = Label(root, text="Nombre: ", font=style_letra_label, background="#ffffff")
    nombre_label.place(x=100, y=160)

    nombre_entry = Entry(root, bd=2)
    nombre_entry.place(x=175, y=160)
    
    apellido_label = Label(root, text="Apellido: ", font=style_letra_label, background="#ffffff")
    apellido_label.place(x=400, y=80)

    apellido_entry = Entry(root, bd=2)
    apellido_entry.place(x=475, y=80)
    
    grupo_label = Label(root, text="Grupo: ", font=style_letra_label, background="#ffffff")
    grupo_label.place(x=400, y=120)

    grupo_entry= Entry(root, bd=2)
    grupo_entry.place(x=475, y=120)
    
    telefono_label = Label(root, text="Telefono: ", font=style_letra_label, background="#ffffff")
    telefono_label.place(x=400, y=160)

    telefono_entry= Entry(root, bd=2)
    telefono_entry.place(x=475, y=160)
    
    def registrar():
        id_val = id_entry.get()
        ced_val = cedula_entry.get()
        nom_val = nombre_entry.get()
        ap_val = apellido_entry.get()
        tel_val = telefono_entry.get()
        grup_val = ""
        
        if id_val and ced_val and nom_val and ap_val and tel_val:
            if id_val[-1].upper() == "P":
                grup_val = grupo_entry.get()
            
            controlador = Controlador()
            result = controlador.registrar_personal(id_val, ced_val, nom_val, ap_val, grup_val, tel_val)
            
            respuesta_entry.delete(0, END)
            respuesta_entry.insert(0, str(result))
        else:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            
    boton_almacenar = Button(root, text="Registrar", bd=2, background="#ffffff", font=style_letra_label, command=registrar)
    boton_almacenar.place(x=350, y=300)
    
    respuesta_entry = Entry(root)
    respuesta_entry.place(x=340, y=370)
    
    
def mostrar_personal():
    
    title2_label = Label(root, text="Personal Registrado", font=style_title, background="#ffffff")
    title2_label.pack()
    
    todo_per = Label(root, text="Mostrar la Informacion del Personal Registrado; ", font=style_letra_label2, background="#ffffff")
    todo_per.place(x=30, y=50)
    
    todo_radio = Radiobutton(root, bd=2, value=1,  variable = op, background="#ffffff")
    todo_radio.place(x=310, y=50)
    
    todo_per = Label(root, text="Mostrar la Informacion de uno en Concreto: ", font=style_letra_label2, background="#ffffff")
    todo_per.place(x=30, y=80)
    
    todo_radio = Radiobutton(root, bd=2, value=2,  variable = op, background="#ffffff")
    todo_radio.place(x=310, y=80)
    
    boton_mos = Button(root, text="Aceptar", background="#ffffff", command = evaluar)
    boton_mos.place(x=350, y=100)



registromenu.add_command(label="Registrar Personal", command=registro_personal)
registromenu.add_command(label="Ver Personal", command=mostrar_personal)
registromenu.add_command(label="Actualizar Personal")
registromenu.add_command(label="Eliminar Personal")
registromenu.add_command(label="Salir", command=root.quit)

registromenu.configure(background="white",font=style_letra)

menuBar.add_cascade(label="Personal", menu=registromenu, font=style_letra)
#menuBar.add_cascade(label="Asistencias", menu=editmenu)
#menuBar.add_cascade(label="Ayuda", menu=ayuda)
#fondo_imagen = PhotoImage(file="fondo_unet.png")

#fondo_label = Label(root, image=fondo_imagen )
#fondo_imagen.place(x=0, y=0, relwidth=1, relheight=1)


root.mainloop()
