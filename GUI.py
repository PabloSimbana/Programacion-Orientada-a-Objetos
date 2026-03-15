import tkinter as tk

# Función para agregar datos a la lista
def agregar():
    texto = entrada.get()
    if texto != "":
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)

# Función para limpiar la lista
def limpiar():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Lista de Datos")
ventana.geometry("400x300")

# Label
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack()

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack()

# Botón agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
boton_agregar.pack(pady=5)

# Botón limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
