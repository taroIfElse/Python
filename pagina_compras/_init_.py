from pagina_compras.cliente import Cliente
from pagina_compras.producto import Producto

def main():
    cliente1 = Cliente("Juan Pérez", "juanperez@gmail.com", "Av. Libertador 123")
    producto1 = Producto("Camisa", 50)
    producto2 = Producto("Pantalón", 70)
    cliente1.agregar_producto(producto1)
    cliente1.agregar_producto(producto2)
    cliente1