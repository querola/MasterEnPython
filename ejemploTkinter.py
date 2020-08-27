from tkinter import *

#venta
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Web service")
#Pantallas
home_label =Label(ventana, text="Inicio")
añadir_label =Label(ventana, text="Añadir")
informacion_label =Label(ventana, text="informacion")
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=1 , column=1)
    añadir_label.grid_remove()
    informacion_label.grid_remove()
def Añadir():
    añadir_label.grid(row=1 , column=1)
    home_label.grid_remove()
    informacion_label.grid_remove()
def informacion():  
    informacion_label.grid(row=1 , column=1)
    añadir_label.grid_remove()
    home_label.grid_remove()
#cargar pantalla de inicio
home()

#menu

menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=Añadir)
menu_superior.add_command(label="Informacion", command=informacion)
menu_superior.add_command(label="Salir", command=ventana.quit)
#cargar el menu
ventana.config(menu=menu_superior)
ventana.mainloop()