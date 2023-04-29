import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="registros"
)

def agregar_estudiante():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    curso = entrada_curso.get()

    cursor = mydb.cursor()
    consulta = "INSERT INTO estudiantes (nombre, edad, curso) VALUES (%s, %s, %s)"
    valores = (nombre, edad, curso)
    cursor.execute(consulta, valores)

    mydb.commit()

    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_curso.delete(0, tk.END)

ventana = tk.Tk()
ventana.title("Registro de estudiantes")

etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack()
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.pack()
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

etiqueta_curso = tk.Label(ventana, text="Curso:")
etiqueta_curso.pack()
entrada_curso = tk.Entry(ventana)
entrada_curso.pack()

boton_agregar = tk.Button(ventana, text="Agregar estudiante", command=agregar_estudiante)
boton_agregar.pack()

ventana.mainloop()
