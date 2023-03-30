class Habitacion:
    def __init__(self, num_habitacion, tipo_habitacion, capacidad, precio_noche):
        self.num_habitacion = num_habitacion
        self.tipo_habitacion = tipo_habitacion
        self.capacidad = capacidad
        self.precio_noche = precio_noche

    def registrar_habitacion(self):
        # código para almacenar la información de la habitación en la base de datos
        pass


class Cliente:
    def __init__(self, nombre, apellido, correo_electronico, num_telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo_electronico = correo_electronico
        self.num_telefono = num_telefono

    def registrar_cliente(self):
        # código para almacenar la información del cliente en la base de datos
        pass


class Pedido:
    def __init__(self, num_habitacion, fecha_pedido, productos_solicitados, precio_total):
        self.num_habitacion = num_habitacion
        self.fecha_pedido = fecha_pedido
        self.productos_solicitados = productos_solicitados
        self.precio_total = precio_total

    def registrar_pedido(self):
        # código para almacenar la información del pedido en la base de datos
        pass