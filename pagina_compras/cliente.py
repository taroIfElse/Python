from pagina_compras.carrito import Carrito

class Cliente:
    def _init_(self, nombre, correo, direccion):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.carrito = Carrito()

    def agregar_producto(self, producto):
        self.carrito.agregar_producto(producto)

    def eliminar_producto(self, producto):
        self.carrito.eliminar_producto(producto)

    def ver_carrito(self):
        print("Productos en el carrito:")
        for producto in self.carrito.productos:
            print(producto)

    def _str_(self):
        return self.nombre