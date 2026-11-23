class Incidente:
    def __init__(self, id, ip, tipoAtaque, nivelRiesgo, estado):
        self.id = id
        self.ip = ip
        self.tipoAtaque = tipoAtaque
        self.nivelRiesgo = nivelRiesgo
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id} | IP: {self.ip} | Ataque: {self.tipoAtaque} | Riesgo: {self.nivelRiesgo} | Estado: {self.estado}"

class Alumno:
    def __init__(self, numeroControl, nombre, carrera):
        self.numeroControl = numeroControl
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return f"No. Control: {self.numeroControl} | Nombre: {self.nombre} | Carrera: {self.carrera}"

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Codigo: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio}"