# 1. Introducción y Configuración
# Vamos a Preparar con python una cocina donde puedes cocinar varios platos (programas).

# La configuración implica preparar la cocina (instalar Python).
#Conculsta https://www.python.org/

# 2. Variables y Tipos de Datos
#Las variables son como contenedores que contienen diferentes tipos de datos (ingredientes).
gramos = 50  # Tipo numérico
kilos = 1.14  # Tipo float
ingrediente1 = "Harina"  # Tipo cadena de texto
ingrediente2 = "Sal"  # Tipo cadena de texto
disponible = True  # Tipo booleano = verdadero/falso

# 3. Operadores
# Los operadores realizan acciones en los ingredientes (variables).
resultado = gramos + kilos * 1000  # Suma gramos y kilos convertidos a gramos
precio_por_kilo = 2.5
precio_total = kilos * precio_por_kilo
mensaje_precio = f"El precio total de {kilos} kilos de {ingrediente1.lower()} es ${precio_total:.2f}"

# 4. Control de Flujo
# El control de flujo dirige la ejecución del programa basado en condiciones (pasos de la receta).
if disponible:
    print(ingrediente1)  # Imprimir si el ingrediente está disponible
else:
    print("No disponible")

# 5. Estructuras de Datos
# Por ejemplo, para un Libro de recetas organizando múltiples recetas.
# Las estructuras de datos almacenan y organizan datos (recetas).
lista_recetas = ["Pizza", "Pasta", "Ensalada"]  # Lista
tupla_recetas = ("Sopa", "Estofado", "Curry")  # Tupla
conjunto_recetas = {"Hamburguesa", "Sándwich", "Wrap"}  # Conjunto
diccionario_recetas = {"Postre": "Pastel", "Bebida": "Té"}  # Diccionario

# 6. Funciones
# Las funciones son como electrodomésticos que realizan acciones específicas (tareas).
def cocinar_receta(receta):
    print("Cocinando...", receta)

#Se invoca a la función enviándole un valor.
cocinar_receta("pizza")

# 7. Conceptos Básicos de Pruebas
# Las pruebas implican verificar y ajustar el programa para la corrección.
# Verifica si la salida de cocinar_receta(receta) coincide con la cadena esperada
# Si la afirmación es falsa, se generará una excepción
def prueba_receta(receta):
    assert cocinar_receta(receta) == "Cocinando " + receta

# 8. Módulos y Paquetes
# Los módulos contienen código reutilizable
# Los paquetes son directorios que agrupan varios módulos relacionados
# Los módulos son como secciones en un libro de recetas, y los paquetes son colecciones de libros.
import herramientas_cocina.modulo_cocina as cocina  # Importar un módulo
print(cocina.mezclar(ingrediente1,ingrediente2))

# 9. Manejo de Archivos
# Guardar recetas en un archivo de recetas.
with open("archivo_recetas.txt", "w") as archivo:
    archivo.write("Receta: Pasta\nIngredientes: Harina, Agua, Salsa")
# Leer el contenido del archivo_recetas.txt
with open("archivo_recetas.txt", "r") as archivo:
    contenido_archivo = archivo.read()
# Imprimir el contenido
print(contenido_archivo)


# 10. Manejo de Excepciones
# El manejo de excepciones es como manejar erroros inesperados de forma controlada.
try:
    resultado = gramos / 0  # División por cero generará un error
except ZeroDivisionError as e:
    print("El error controlado es:", e)

# 11. Programación Orientada a Objetos (OOP)
# Explicación: La POO implica crear objetos personalizados con propiedades y comportamientos específicos (tareas).
# Creamos un objeto de la clase "ElectrodomesticoCocina" de nombre "Horno" con una función de "Asar"
class ElectrodomesticoCocina:
    def __init__(self, nombre):
        self.nombre = nombre

    def asar(self):
        print(self.nombre, "está asando")

horno = ElectrodomesticoCocina("Horno")
horno.asar()

# 12. Librerías y Marcos de Trabajo
# Una librería es un conjunto de módulos y paquetes que ofrecen funciones y herramientas
import mezclas_especias as especias  # Importar una librería
print(especias.condimentar(ingrediente1))

# 13. Conceptos Básicos de Programación en Estilo Python
# Programar de manera pythonica implica usar el estilo único y limpio de Python.
numeros_al_cuadrado = [num**2 for num in range(5)]  # Comprensión de lista

# 14. Trabajo con APIs
# Trabajar con APIs es como hacer pedidos (órdenes) de datos en línea a otro programa, web, etc
# Por ejemplo para comprar ingredientes online en una tienda nos conectamos a la API de su Web

#Vemos si la API de la Web responde. 
import requests
x = requests.get('https://ikerbit.com')
print(x.status_code)

# 15. Desarrollo Web Básico con Python
# Por ejemplo para presentar menu de un restaurante (desarrollo web).
from flask import Flask  # Usar Flask para aplicaciones web
import threading

app = Flask(__name__)

@app.route("/")
def inicio():
    contenido_web=f"""
    <h1>Bienvenido al restaurante de Python</h1>
    <p>gramos:{gramos}</p>
    <p>kilos:{kilos}</p>
    <p>Ingrediente: {ingrediente1}</p>
    <p>Lista recetas:{lista_recetas}</p>
    <p>contenido_archivo:{contenido_archivo}</p>
    <p>especias.condimentar(ingrediente):{especias.condimentar(ingrediente1)}</p>
"""
    return contenido_web

def run_flask():
    app.run(debug=True, use_reloader=False)

# Iniciar Flask en un hilo
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Detener el servidor Flask y finalizar el programa
flask_thread.join()

