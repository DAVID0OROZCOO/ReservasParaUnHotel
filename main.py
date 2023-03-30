class Habitacion:
    def __init__(self, numero, disponible):
        self.numero = numero
        self.disponible = disponible


class Cliente:
    def __init__(self, id_cliente, nombre):
        self.id_cliente = id_cliente
        self.nombre = nombre


class Pedido:
    def __init__(self, id_pedido, cliente, habitacion, productos):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.habitacion = habitacion
        self.productos = productos


class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio


class SistemaHotel:
    def __init__(self):
        self.habitaciones = []
        self.clientes = {}
        self.pedidos = {}
        self.productos = {}
        self.facturas = []

    def registro_habitacion(self, numero, disponible):
        habitacion = Habitacion(numero, disponible)
        self.habitaciones.append(habitacion)

    def registro_cliente(self, id_cliente, nombre):
        cliente = Cliente(id_cliente, nombre)
        self.clientes[id_cliente] = cliente

    def registro_pedido(self, id_pedido, cliente, habitacion, productos):
        pedido = Pedido(id_pedido, cliente, habitacion, productos)
        self.pedidos[id_pedido] = pedido

    def consulta_habitaciones_disponibles(self):
        return [habitacion for habitacion in self.habitaciones if habitacion.disponible]

    def registro_producto(self, id_producto, nombre, precio):
        producto = Producto(id_producto, nombre, precio)
        self.productos[id_producto] = producto

    def consulta_precio_producto(self, id_producto):
        return self.productos[id_producto].precio

    def asignar_pedido_a_habitacion(self, id_pedido, numero_habitacion):
        pedido = self.pedidos[id_pedido]
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion), None)
        if habitacion and habitacion.disponible:
            pedido.habitacion = habitacion
            habitacion.disponible = False
        else:
            raise ValueError("Habitación no disponible.")

    def generar_factura(self, id_pedido):
        pedido = self.pedidos[id_pedido]
        total = sum([self.productos[p].precio for p in pedido.productos])
        factura = {
            'id_pedido': id_pedido,
            'id_cliente': pedido.cliente.id_cliente,
            'habitacion': pedido.habitacion.numero,
            'productos': [self.productos[p] for p in pedido.productos],
            'total': total
        }
        self.facturas.append(factura)
        return factura



