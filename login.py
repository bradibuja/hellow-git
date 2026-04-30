import tkinter as tk
from tkinter import messagebox


def verificar_login():
    usuario = entrada_usuario.get().strip()
    contrasena = entrada_contrasena.get().strip()
    if usuario == "admin" and contrasena == "1234":
        messagebox.showinfo("Login", "Ingreso exitoso")
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")


ventana = tk.Tk()
ventana.title("Login sencillo")
ventana.geometry("300x180")
ventana.resizable(False, False)

etiqueta_usuario = tk.Label(ventana, text="Usuario:")
etiqueta_usuario.pack(pady=(20, 5))
entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack(fill="x", padx=40)

etiqueta_contrasena = tk.Label(ventana, text="Contraseña:")
etiqueta_contrasena.pack(pady=(10, 5))
entrada_contrasena = tk.Entry(ventana, show="*")
entrada_contrasena.pack(fill="x", padx=40)

boton_ingresar = tk.Button(ventana, text="Ingresar", command=verificar_login)
boton_ingresar.pack(pady=15)

ventana.mainloop()
