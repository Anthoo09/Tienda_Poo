from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # lista de Producto

    def _existe_id(self, id_buscar):
        return any(p.get_id() == id_buscar for p in self.productos)

    def agregar_producto(self, producto):
        if self._existe_id(producto.get_id()):
            print("❌ Error: El ID ya existe en el inventario.")
            return
        self.productos.append(producto)
        print("✅ Producto agregado con éxito.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("🗑️ Producto eliminado con éxito.")
                return
        print("❌ No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print("✏️ Producto actualizado con éxito.")
                return
        print("❌ No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        nombre = nombre.lower().strip()
        resultados = [p for p in self.productos if nombre in p.get_nombre().lower()]
        if resultados:
            print("🔎 Resultados de la búsqueda:")
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("📋 Inventario actual:")
            for p in self.productos:
                print(p)
