import tkinter as tk 
import matplotlib.pyplot as plt

x = [3,4,5,6,7]
y = [10,11,14,16,18]

plt.scatter(x,y, colorizer="red")
plt.title("Mi primera grafica")
plt.xlabel("eje x")
plt.ylabel("eje y")
plt.show()
"""
def saludar():
    nombre = nombre.entrada.get().strip()
    if not nombre:
        nombre = "mundo"
    lbl.config(text=f"Hola compa, {nombre} !!")
""""


root = tk.Tk()
root.title("Saludador")
root.geometry("360x220")

entrada = tk.Entry(root)
entrada.pack(pady=10)

lbl = tk.Label(root, text="Escribe tu nombre y presiona el boton",background="gray", foreground="black")
lbl.pack(pady=10)
bottom = tk.Button(root, text="Saludador")
bottom.pack(pady=10)
root.mainloop()