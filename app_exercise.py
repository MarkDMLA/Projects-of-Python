from tkinter import *
import random, datetime

from click import command

root = Tk()
root.title('Ejercicios diario')
root.geometry('700x400')
root.config(bg='green')

frame1 = LabelFrame(root,text='Ejercicios de acondicionamiento fisico', font=('calibri', 14))
frame2 = LabelFrame(root,text='Ejercicios para hoy', font=('calibri', 14))

frame1.pack(fill='both', expand='yes', padx='10', pady='5')
frame2.pack(fill='both', expand='yes', padx='20', pady='15')

#======================================Control Variables=========================================================

lagatigas = IntVar()
adopminales = IntVar()
sentadillas = IntVar()
fecha = StringVar()

#======================================Functions=========================================================
def Crear_R():
    chars_numbers = range(1, 101)
    lagatigas.set(str(random.choice(chars_numbers)))
    adopminales.set(str(random.choice(chars_numbers)))
    sentadillas.set(str(random.choice(chars_numbers)))

def Time():
    date = datetime.datetime.now()
    fecha.set(date.strftime('%d/%m/%Y'))

def Reiniciar():
    lagatigas.set('')
    adopminales.set('')
    sentadillas.set('')

#======================================Structure=========================================================

#Frame 1 Cuadro superior

lbl1 = Label(frame1, text="Fecha actual =", width=30)
lbl1.grid(row=1, column=0, padx=5, pady=3) 
entMat = Entry(frame1,textvariable=fecha, command=Time())   
entMat.grid(row=1, column=1, padx=5, pady=3) 

#Frame 2 Cuadro inferior

lbl1 = Label(frame2, text="Lagatijas", width=20)
lbl1.grid(row=3, column=0, padx=5, pady=3)
entMat = Entry(frame2,textvariable=lagatigas)   
entMat.grid(row=3, column=1, padx=5, pady=3) 

lbl1 = Label(frame2, text="Adopminales", width=20)
lbl1.grid(row=4, column=0, padx=5, pady=3)
entMat = Entry(frame2,textvariable=adopminales)   
entMat.grid(row=4, column=1, padx=5, pady=3) 

lbl1 = Label(frame2, text="Sentadillas", width=20)
lbl1.grid(row=5, column=0, padx=5, pady=3)
entMat = Entry(frame2,textvariable=sentadillas)   
entMat.grid(row=5, column=1, padx=5, pady=3) 

btn1 = Button(frame2, text="Crear rutina", width=15, height=2,command=Crear_R)
btn1.grid(row=6, column=2, padx=10, pady=10)

btn2 = Button(frame2, text="Reiniciar", width=15, height=2,command=Reiniciar)
btn2.grid(row=6, column=3, padx=10, pady=10)

root.mainloop()
