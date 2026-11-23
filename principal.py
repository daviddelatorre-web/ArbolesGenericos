from arbol import ArbolBinario
from arbol import NodoArbol
from objetos import Incidente
from objetos import Alumno
from objetos import Producto

incidentesBase = [
    Incidente(50, "192.168.1.10", "Fuerza bruta", "Alto", "Abierto"),
    Incidente(25, "10.0.0.5", "Phishing", "Medio", "En analisis"),
    Incidente(75, "172.16.0.8", "DDoS", "Critico", "Mitigado"),
    Incidente(10, "192.168.1.44", "Malware", "Alto", "Cerrado"),
    Incidente(60, "10.0.0.99", "Inyeccion SQL", "Critico", "Abierto"),
    Incidente(85, "192.168.10.22", "Escaneo de puertos", "Bajo", "Cerrado")
]

alumnosBase = [
    Alumno(25110671, "David Lorenzo De la Torre Hernandez", "Ingenieria en Ciberseguridad"),
    Alumno(25110500, "Ana Sofia Lopez", "Ingenieria en Sistemas"),
    Alumno(25110890, "Carlos Ruiz", "Ingenieria en Ciberseguridad"),
    Alumno(25110412, "Maria Fernanda Diaz", "Ingenieria Industrial"),
    Alumno(25110730, "Luis Alberto Gomez", "Ingenieria en Ciberseguridad")
]

productosBase = [
    Producto(300, "Teclado mecanico", 1250.0),
    Producto(150, "Mouse inalambrico", 480.0),
    Producto(450, "Monitor 24 pulgadas", 3200.0),
    Producto(100, "Mousepad XL", 290.0),
    Producto(380, "Audifonos gamer", 890.0)
]

def pedirIncidente():
    idInc = int(input("ID: "))
    ip = input("IP: ")
    tipoAtaque = input("Tipo de ataque: ")
    nivelRiesgo = input("Nivel de riesgo: ")
    estado = input("Estado: ")
    return Incidente(idInc, ip, tipoAtaque, nivelRiesgo, estado)

def pedirAlumno():
    numControl = int(input("Numero de control: "))
    nombre = input("Nombre: ")
    carrera = input("Carrera: ")
    return Alumno(numControl, nombre, carrera)

def pedirProducto():
    codigo = int(input("Codigo: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    return Producto(codigo, nombre, precio)

def claveIncidente():
    idInc = int(input("ID: "))
    return Incidente(idInc, "", "", "", "")

def claveAlumno():
    numControl = int(input("Numero de control: "))
    return Alumno(numControl, "", "")

def claveProducto():
    codigo = int(input("Codigo: "))
    return Producto(codigo, "", 0)

def cargarLista(arbol, lista):
    for elemento in lista:
        arbol.insertarNodo(elemento)
    print("Datos de prueba cargados:", len(lista))

def menuOperaciones(nombreObjeto, arbol, pedirObj, pedirClave, listaBase):
    while True:
        print("\n--- OPERACIONES DE " + nombreObjeto + " ---")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Recorrido InOrden")
        print("5. Recorrido PreOrden")
        print("6. Recorrido PostOrden")
        print("7. Imprimir arbol")
        print("8. Cargar datos de prueba")
        print("9. Regresar al menu principal")
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            obj = pedirObj()
            arbol.insertarNodo(obj)
            print("Insertado:", obj)
        elif opcion == "2":
            buscado = arbol.buscarNodo(pedirClave())
            print("Resultado de busqueda:", buscado)
        elif opcion == "3":
            arbol.eliminarNodo(pedirClave())
            print("Eliminacion ejecutada.")
        elif opcion == "4":
            print("Recorrido InOrden:")
            arbol.inOrden()
        elif opcion == "5":
            print("Recorrido PreOrden:")
            arbol.preOrden()
        elif opcion == "6":
            print("Recorrido PostOrden:")
            arbol.postOrden()
        elif opcion == "7":
            print("Estructura del arbol:")
            arbol.imprimirArbol()
        elif opcion == "8":
            cargarLista(arbol, listaBase)
        elif opcion == "9":
            break
        else:
            print("Opcion no valida.")

def menuPrincipal():
    arbolIncidentes = ArbolBinario(clave=lambda x: x.id)
    arbolAlumnos = ArbolBinario(clave=lambda x: x.numeroControl)
    arbolProductos = ArbolBinario(clave=lambda x: x.codigo)
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Incidente")
        print("2. Alumno")
        print("3. Producto")
        print("4. Salir")
        opcion = input("Elige una opcion: ").strip()
        if opcion == "1":
            menuOperaciones("INCIDENTE", arbolIncidentes, pedirIncidente, claveIncidente, incidentesBase)
        elif opcion == "2":
            menuOperaciones("ALUMNO", arbolAlumnos, pedirAlumno, claveAlumno, alumnosBase)
        elif opcion == "3":
            menuOperaciones("PRODUCTO", arbolProductos, pedirProducto, claveProducto, productosBase)
        elif opcion == "4":
            break
        else:
            print("Opcion no valida.")

if __name__ == "__main__":
    menuPrincipal()