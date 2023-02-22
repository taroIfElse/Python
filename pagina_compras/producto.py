class Producto:
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def _str_(self):
        return self.nombre