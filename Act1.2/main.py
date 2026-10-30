import tkinter as tk
from tkinter import messagebox
from clases.Producto import Producto 

class MenuAplicacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario por Sucursal")
        self.root.geometry("500x550")
        self.root.configure(bg="#194d75")

        
        self.productos = [] 

        
        titulo = tk.Label(root, text="Menú Principal", font=("Helvetica", 20, "bold"), bg="#498fc5", fg="#eeeeee")
        titulo.pack(pady=30)

        
        self.crear_boton("Agregar Producto a Inventario", self.ventana_agregar_producto)
        self.crear_boton("Mostrar Inventario", self.mostrar_inventario_en_ventana)
        self.crear_boton("Salir", self.salir)

    def crear_boton(self, texto, comando):
        boton = tk.Button(
            self.root, text=texto, command=comando,
            font=("Arial Black", 14), bg="#3498db", fg="white",
            width=30, height=2, relief="raised", bd=3
        )
        boton.pack(pady=10)

    def ventana_agregar_producto(self):
        
        self.ventana_agregar = tk.Toplevel(self.root)
        self.ventana_agregar.title("Agregar Producto a Sucursal")
        self.ventana_agregar.geometry("350x450")
        self.ventana_agregar.configure(bg="#f0f4f7")

        tk.Label(self.ventana_agregar, text="Agregar Producto a Sucursal", font=("Helvetica", 14, "bold"), bg="#f0f4f7", fg="#2c3e50").pack(pady=20)

        tk.Label(self.ventana_agregar, text="Nombre del Producto:", bg="#f0f4f7").pack()
        self.entrada_producto = tk.Entry(self.ventana_agregar, width=30)
        self.entrada_producto.pack(pady=5)

        tk.Label(self.ventana_agregar, text="Precio del Producto: $", bg="#f0f4f7").pack()
        self.entrada_precio = tk.Entry(self.ventana_agregar, width=30)
        self.entrada_precio.pack(pady=5)

        tk.Label(self.ventana_agregar, text="Existencia:", bg="#f0f4f7").pack()
        self.entrada_stock = tk.Entry(self.ventana_agregar, width=30)
        self.entrada_stock.pack(pady=5)

        
        btn_guardar = tk.Button(
            self.ventana_agregar, text="Guardar", command=self.agregar_producto,
            font=("Arial", 12), bg="#0a478d", fg="white",
            width=20, height=2, relief="raised", bd=3
        )
        btn_guardar.pack(pady=30)

    
    def validar_datos_producto(self, nombre_producto, precio_producto, stock_producto):
        
        if not nombre_producto or not precio_producto or not stock_producto:
            messagebox.showinfo("Error", "Todos los campos deben ser completados.", parent=self.ventana_agregar)
            return False
        
        
        try:
            precio_valido = float(precio_producto)
        except ValueError:
            messagebox.showinfo("Error", "El precio debe ser un número válido.", parent=self.ventana_agregar)
            return False
            
        
        try:
            stock_valido = int(stock_producto)
        except ValueError:
            messagebox.showinfo("Error", "El stock debe ser un número entero válido.", parent=self.ventana_agregar)
            return False

        
        return True

    
    def agregar_producto(self):
        nombre = self.entrada_producto.get()
        precio = self.entrada_precio.get()
        stock = self.entrada_stock.get()

        if (self.validar_datos_producto(nombre, precio, stock)):
            
            producto = Producto(nombre, float(precio), int(stock))
            self.productos.append(producto)
            messagebox.showinfo("Información", "¡Producto Agregado con exito!", parent=self.ventana_agregar)
            
            
            self.entrada_producto.delete(0, tk.END)
            self.entrada_precio.delete(0, tk.END)
            self.entrada_stock.delete(0, tk.END)
            self.ventana_agregar.destroy() 
        else:
            messagebox.showinfo("Error", "¡Verifica tus Datos!", parent=self.ventana_agregar)

    
    def mostrar_inventario_en_ventana(self):
        if len(self.productos) == 0:
            messagebox.showinfo("Inventario Completo", "El inventario está vacío.")
            return

        
        mensaje_inventario = ""
        for p in self.productos:
            mensaje_inventario += str(p) + "\n"
        
        messagebox.showinfo("Inventario Completo", mensaje_inventario)

    
    def salir(self):
        self.root.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = MenuAplicacion(ventana)
    ventana.mainloop()