import pyodbc
from tkinter import *
ventana = Tk()
ventana.geometry("400x400")
ventana.title("Guatemala Monitoreo")
texto = ""

informacion_label = Label(ventana, text="informacion")
def read(conn):
    print("Read")
    cursor=conn.cursor()
    cursor.execute("select TOP(10) * from Historico")
    for row in cursor:    
        print(f'row = {row}')
        Label(ventana, text = row).pack()
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