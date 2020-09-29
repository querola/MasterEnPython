import pyodbc
import os.path
from tkinter import *

class InterfazWebService():
    #se crea la ventana
    #Atributos
    
    def __init__(self):  
        self.ventana = Tk()
        self.ventana.geometry("700x400")
        self.ventana.title("Guatemala Monitoreo")
        self.scrollbar = Scrollbar(self.ventana)
        self.scrollbar.grid(padx=5, pady=5,  row=0, column = 2 )
        encabezado = Label(self.ventana , text="encabezado")
        informacion_label = Label(self.ventana, text="informacion")     
        # comprobar si existe un archivo
        self.ruta_icono = os.path.abspath('./imagenes/chart.ico')
        if os.path.isfile(self.ruta_icono):
            self.ventana.iconbitmap(self.ruta_icono)
        #Poner un boton 
        
        
    def ObtenerInformacion(self, SqlIp):
        print("read.....")
        conn = pyodbc.connect(SqlIp)
        cursor=conn.cursor()
        cursor.execute("select TOP(20) * from Historico order by fecha desc ")
        c = 0
        listbox = Listbox(self.ventana, yscrollcommand=self.scrollbar.set)
        for row in cursor:    
            # print(f'row = {row}')
            listbox.insert("end", row)
            #label = Label(ventana, text = str(row))
            c+=1
            #label.grid(row=c, column=0, sticky = NW)
            #label.config(fg="black",  font=("Arial", 12), padx=10, pady=20, bd=2 , relief=SOLID) 
        listbox.config(width=150, height=50)
        listbox.grid(padx=5, pady=5, row=0, column = 1)
        self.scrollbar.config(command=listbox.yview)
        # create(conn)
        # update(conn)
        # delete(conn)
        self.ventana.mainloop()
        conn.close()
def main():
    inicio = InterfazWebService()
    inicio.ObtenerInformacion("Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-SQGOGNA;"
        "Database=GTDB;"
        "Trusted_Connection=yes;")
if __name__ == "__main__":
    main()       