import pyodbc
import os.path
from tkinter import *
ventana = Tk()
ventana.geometry("700x400")
ventana.title("Guatemala Monitoreo")
# comprobar si existe un archivo
ruta_icono = os.path.abspath('./imagenes/chart.ico')
#comprueba si existe la ruta del icono para cargarlo
if os.path.isfile(ruta_icono):
    ventana.iconbitmap(ruta_icono)
encabezado = Label(ventana , text="encabezado")
informacion_label = Label(ventana, text="informacion")
def read(conn):
    print("Read")
    cursor=conn.cursor()
    cursor.execute("select TOP(20) * from Historico order by fecha desc ")
    c = 0
    for row in cursor:    
        # print(f'row = {row}')
        label = Label(ventana, text = row)
        c+=1
        label.grid(row=c, column=0, sticky = NW)
        label.config(fg="black", bg="red", font=("Arial", 18), padx=10, pady=20, bd=2 , relief=SOLID) 
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=DESKTOP-SQGOGNA;"
    "Database=GTDB;"
    "Trusted_Connection=yes;"
)

read(conn)
# create(conn)
# update(conn)
# delete(conn)
ventana.mainloop()
conn.close()