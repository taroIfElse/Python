class Carrito:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    def ver_carrito(self):
        print("Productos en el carrito:")
        for producto in self.productos:
            print(producto)