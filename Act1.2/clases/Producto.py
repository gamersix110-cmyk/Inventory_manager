class Producto:
    def __init__(self, nombre, precio, stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    #Getters
    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    #Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_precio(self, precio):
        if precio >= 0: #validación
            self.__precio = precio
        else:
            print("El precio no puede ser negativo")

    def set_stock(self, stock):
        if stock >= 0:
            self.__stock = stock
        else:
            print("El stock no puede ser negativo")

    #Metodo
    def __str__(self):
        return f"- {self.__nombre} - ${self.__precio} ({self.__stock} en stock)"