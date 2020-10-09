import pyodbc
import os.path
import datetime
from tkinter import *
from tkcalendar import *

class InterfazWebService():
    #se crea la ventana
    #Atributos
    
    def __init__(self):  
        self.ventana = Tk()
        self.ventana.geometry("700x700")
        self.ventana.title("Guatemala Monitoreo")
        self.scrollbar = Scrollbar(self.ventana)
        self.scrollbar.grid(padx=5, pady=5)
        encabezado = Label(self.ventana , text="encabezado")
        informacion_label = Label(self.ventana, text="informacion")   
        
        # comprobar si existe un archivo
        self.ruta_icono = os.path.abspath('./imagenes/chart.ico')
        if os.path.isfile(self.ruta_icono):
            self.ventana.iconbitmap(self.ruta_icono)
        #date entry de Fecha inicio
        inicioLabel = Label(self.ventana, text="Fecha inicio")
        inicioLabel.grid(row=0,column =1 )
        self.fechainicio = DateEntry(width= 15, background = "blue", foreground="red", borderwidth = 3, date_pattern = "dd/mm/yyyy")
        self.fechainicio.grid(row=0, column=2, padx=5, pady=5 )
        finalLabel = Label(self.ventana, text="Fecha Fin")
        finalLabel.grid(row=0,column =3 )
        self.fechafin = DateEntry(width= 15, background = "blue", foreground="red", borderwidth = 3, date_pattern = "dd/mm/yyyy")
        self.fechafin.grid(row=0, column=4, padx=5, pady=5 )
        boton = Button(self.ventana, text="Consultar", command = self.ObtenerInformacion)
        boton.grid(row=1, column=1, sticky="w")
        boton.config(padx=10, pady=10, bg="green", fg="white" )
        self.ventana.mainloop()
    def obtenerfechaInicio(self):
            #elevar un nivel el calendario
            #top = Toplevel(self.ventana)
            #Poner el datetimepicker
            self.calInicio = Calendar(self.ventana, selectmode="day", year=2020, month=5, day=22, date_pattern = "yyyy-mm-dd")  
            self.calInicio.grid(row=0, column=2, pady=20, expand=True)
            #btnAceptar = Button(top, Text="Aceptar")
    def ObtenerInformacion(self):
        print("read.....")
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-SQGOGNA;"
        "Database=GTDB;"
        "Trusted_Connection=yes;")
        cursor=conn.cursor()      
        fechaInicio = self.fechainicio.get_date()
        fechaFin = self.fechafin.get_date()
        #falta poner la fecha final con un dia mas
        print(f"select TOP(20) * from Historico where fecha > '{fechaInicio}' and  fecha <'{fechaFin}' order by fecha desc ")
        cursor.execute(f"select TOP(20) * from Historico where fecha > '{fechaInicio}' and fecha <  '{fechaFin}' order by fecha desc ")
        c = 0
        listbox = Listbox(self.ventana, yscrollcommand = self.scrollbar.set)
        for row in cursor:    
            # print(f'row = {row}')
            listbox.insert("end", row)
            #label = Label(ventana, text = str(row))
            c+=1
            #label.grid(row=c, column=0, sticky = NW)
            #label.config(fg="black",  font=("Arial", 12), padx=10, pady=20, bd=2 , relief=SOLID) 
        listbox.config(width=150, height=50)
        listbox.grid(padx=5, pady=5, row=1, column = 1)
        self.scrollbar.config(command=listbox.yview)
        # create(conn)
        # update(conn)
        # delete(conn)
        self.ventana.mainloop()
        conn.close()
def main():
    inicio = InterfazWebService()
    #inicio.ObtenerInformacion()
if __name__ == "__main__":
    main()       