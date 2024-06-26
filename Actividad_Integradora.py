"""EJERCICIO N* 1:
    Escribir una función que calcule el máximo común divisor entre dos números"""

def calcular_mcd(num1, num2):
    # Verificar que los números sean enteros positivos
    if not isinstance(num1, int) or not isinstance(num2, int) or num1 < 0 or num2 < 0:
        return "Error: Los números deben ser enteros positivos"

    # Si uno de los números es cero, el MCD es el otro número
    if num2 == 0:
        return num1

    # Aplicar el algoritmo de Euclides para calcular el MCD
    resto = num1 % num2
    return calcular_mcd(num2, resto)

#Llamamos a la función para comprobar:

mcd = calcular_mcd(48,72)
print(mcd)  # Output: 24


"""EJERCICIO N* 2:
    Escribir una función que calcule el mínimo común múltiplo entre dos números"""

def calcular_mcm(num1, num2):
    # Verificar que los números sean enteros positivos
    if not isinstance(num1, int) or not isinstance(num2, int) or num1 < 0 or num2 < 0:
        return "Error: Los números deben ser enteros positivos"

    # Calcular el MCM utilizando la fórmula: MCM = (num1 * num2) / MCD
    mcd = calcular_mcd(num1, num2)
    mcm = (num1 * num2) // mcd
    return mcm

def calcular_mcd(num1, num2):
    # Verificar que los números sean enteros positivos
    if not isinstance(num1, int) or not isinstance(num2, int) or num1 < 0 or num2 < 0:
        return "Error: Los números deben ser enteros positivos"

    # Caso base: si uno de los números es cero, el MCD es el otro número
    if num2 == 0:
        return num1

    # Aplicar el algoritmo de Euclides para calcular el MCD
    resto = num1 % num2
    return calcular_mcd(num2, resto)

#Llamamos a la función para comprobar:

mcm = calcular_mcm(12, 18)
print(mcm)  # Output: 36


"""EJERCICIO N* 3:
    Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
    que contiene y la cantidad de veces que aparece (frecuencia)"""

def contar_palabras(cadena):
    # Dividir la cadena en palabras y eliminar los caracteres especiales
    palabras = cadena.lower().split()
    palabras = [palabra.strip(",.¡!¿?") for palabra in palabras]

    # Crear un diccionario para almacenar las palabras y sus frecuencias
    frecuencia = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

# Ejemplo de uso
cadena = "Pancha plancha con 4 planchas. ¿Con cuántas planchas plancha Pancha?"
resultado = contar_palabras(cadena)
print(resultado)


"""EJERCICIO N* 4:
    Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra 
    que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba 
    el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida 
    y su frecuencia"""

def contar_palabras(cadena):
    # Dividir la cadena en palabras y eliminar los caracteres especiales
    palabras = cadena.lower().split()
    palabras = [palabra.strip(",.¡!¿?") for palabra in palabras]

    # Crear un diccionario para almacenar las palabras y sus frecuencias
    frecuencia = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

def palabra_mas_repetida(frecuencia):
    # Obtener la palabra más repetida y su frecuencia
    palabra_max = ""
    frecuencia_max = 0

    for palabra, frecuencia in frecuencia.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia

    return (palabra_max, frecuencia_max)

# Ejemplo de uso

cadena = "A Cuesta le cuesta subir la cuesta, y en medio de la cuesta, va y se acuesta."
frecuencia = contar_palabras(cadena)
palabra_repetida, frecuencia = palabra_mas_repetida(frecuencia)
print("La palabra más repetida es '{}' con una frecuencia de {}".format(palabra_repetida, frecuencia))


"""EJERCICIO N* 5:
    Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto 
    en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, 
    iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa 
    como recursiva"""

#Resolución de manera iterativa:

def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Error: El valor ingresado no es un entero válido. Intente nuevamente.")

#Resolución de manera recursiva:

def get_int():
    try:
        valor = int(input("Ingrese un valor entero: "))
        return valor
    except ValueError:
        print("Error: El valor ingresado no es un entero válido. Intente nuevamente.")
        return get_int()
 

"""EJERCICIO N* 6:
    Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes 
    métodos para la clase: Un constructor, donde los datos pueden estar vacíos.  Los setters y getters
    para cada uno de los atributos. Hay que validar las entradas de datos.  mostrar(): Muestra los datos
    de la persona.  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad"""

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    
    def get_edad(self):
        return self._edad
    
    def set_edad(self, edad):
        if edad >= 0:
            self._edad = edad
    
    def get_dni(self):
        return self._dni
    
    def set_dni(self, dni):
        self._dni = dni
    
    def mostrar(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("DNI:", self._dni)
    
    def es_mayor_de_edad(self):
        return self._edad >= 18
    
#Ejemplo de uso

# Crear una instancia de Persona
p = Persona()

# Establecer los atributos utilizando los setters
p.set_nombre("Daniel")
p.set_edad(23)
p.set_dni("11223344")

# Mostrar los datos de la persona
p.mostrar()

# Comprobar si la persona es mayor de edad
if p.es_mayor_de_edad():
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


"""EJERCICIO N* 7:
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) 
    y cantidad (puede tener decimales).El titular será obligatorio y la cantidad es opcional. 
    Crear los siguientes métodos para la clase: Un constructor, donde los datos pueden estar vacíos. 
    Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, 
    sólo ingresando o retirando dinero. mostrar(): Muestra los datos de la cuenta. ingresar(cantidad): 
    se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. 
    retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos"""


class Cuenta:
    def __init__(self, titular, cantidad=0):
        self._titular = titular
        self._cantidad = cantidad
    
    def get_titular(self):
        return self._titular
    
    def set_titular(self, titular):
        self._titular = titular
    
    def get_cantidad(self):
        return self._cantidad
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self._cantidad -= cantidad
    
    def mostrar(self):
        print("Titular:", self._titular.get_nombre())
        print("Cantidad:", self._cantidad)

#Ejemplo de uso:

# Crear una instancia de Persona
p = Persona("Daniel", 23, "11223344")

# Crear una instancia de Cuenta con el titular y una cantidad inicial
c = Cuenta(p, 2000)

# Mostrar los datos de la cuenta
c.mostrar()

# Ingresar dinero a la cuenta
c.ingresar(500)

# Mostrar los datos de la cuenta nuevamente
c.mostrar()

# Retirar dinero de la cuenta
c.retirar(200)

# Mostrar los datos de la cuenta una vez más
c.mostrar()


"""EJERCICIO N* 8:
    Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuentaJoven
    que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular 
    y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. 
    Crear los siguientes métodos para la clase: Un constructor. Los setters y getters para el nuevo atributo.
    En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que
    crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor
    de 25 años y falso en caso contrario. Además, la retirada de dinero sólo se podrá hacer si el titular
    es válido. El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta."""



class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self._bonificacion
    
    def set_bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
    
    def es_titular_valido(self):
        return self._titular.es_mayor_de_edad() and self._titular.get_edad() < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
    
    def mostrar(self):
        print("Cuenta Joven")
        print("Bonificación:", self._bonificacion)

 #Ejemplo de uso:

 # Crear una instancia de Persona mayor de edad
p = Persona("Daniel", 23, "11223344")

# Crear una instancia de CuentaJoven con el titular, una cantidad inicial y una bonificación
c = CuentaJoven(p, 1000, 10)

# Mostrar los datos de la cuenta
c.mostrar()

# Verificar si el titular es válido
if c.es_titular_valido():
    print("El titular es válido")
else:
    print("El titular no es válido")

# Retirar dinero de la cuenta
c.retirar(200)

# Mostrar los datos de la cuenta nuevamente
c.mostrar()
