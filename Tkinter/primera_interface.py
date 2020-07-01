from tkinter import *

raiz = Tk()

raiz.title("Ventana de prueba")

raiz.resizable(0,0)

raiz.geometry("650x350")

raiz.config(bg="gray")

# Creamos un Frame y le asignamos sus características particulares
miFrame = Frame()
miFrame.pack(fill="both", expand="false")
miFrame.config(bg="blue")
miFrame.config(width="650", height="350")
miFrame.config(bd=35)
miFrame.config(cursor="hand2")
#miFrame.config(relief="groove")

# Bucle infinito (para que se mantenga a la espera de eventos)
raiz.mainloop()