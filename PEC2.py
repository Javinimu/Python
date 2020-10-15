# Ejercicio1 -Realizar un programa que sume dos listas de diferente longitud y retorne otra lista que contenga la suma de las originales elemento a elemento más los elementos sobrantes de la lista más larga

#Lo interpreto como que el señor me define las listas, mucho mas divertido.
def rellenar (lista):
    repeticiones1 = int(input("¿De cuantos valores quiere la lista?: "))
    for i in range (repeticiones1):
        valor = int(input("Escribe numero: "))
        lista.append(valor)

def sumal (lista):
    if len(lista1) < len(lista2): 
        diferencia = len(lista2) - len(lista1)
        print("La segunda lista tiene mayor longitud que la primera")
        for i in range (diferencia):
            lista1.append(0)
    elif len(lista1) > len(lista2):
        diferencia = len(lista1) - len(lista2)
        print("La primera lista tiene mayor longitud que la segunda")
        for i in range(diferencia):
            lista2.append(0)
    else:
        print("Las listas tienen la misma longitud")
    for i in range (len(lista1)):
        lista.append(lista1[i]+lista2[i])

if __name__ == "__main__":
    lista1 = []
    print("Vamos a rellenar la primera lista: ")
    rellenar (lista1)
    print(lista1)
    lista2 =[]
    print("Vamos a rellenar la segunda lista: ")
    rellenar (lista2)
    print(lista2)
    suma_lista=[]
    sumal (suma_lista)
    print( "La suma de las dos listas es", suma_lista)

# Ejercicio 2 - Realizar un programa que guarde los elementos en común que tienen dos listas.

#Para hacerlo mas ameno me he inventado que dos personas nos dicen que paises han visitado y el programa les devuelve los paises que tienen en comun.
def rellenar (lista): #Defino la funcion para crear listas pero esta vez con cadenas
    repeticiones1 = int(input("¿Cuantos paises ha visitado?: "))
    print("¿Cuales?")
    for i in range (repeticiones1):
        pais = str(input("Introduce el nombre del pais: "))
        lista.append(pais)

def match(x, y):
        matches = [item for item in x if item in y]
        if len(matches) == 0:
            print("¡Oops! No ha habido coincidencias")
        else:
            print("Ambos habeis estado en", set(matches)) 

if __name__ == "__main__":
    pais1 = []
    print("Vamos a rellenar la primera lista: ")
    rellenar (pais1)
    print("La primera persona ha visitado los siguientes paises", pais1)
    pais2 =[]
    print("Vamos a rellenar la segunda lista: ")
    rellenar (pais2)
    print("La segunda persona ha visitado los siguientes paises", pais2)
    match(pais1, pais2)


# Ejercicio 3 - Realizar un programa que retorne el número de elementos comunes iniciales de dos listas
# Sobre la base del ejercicio anterior, lo hago con elementos neutros esta vez.
def rellenar (lista):
    repeticiones1 = int(input("¿Cuantos elementos vas a introducir?: "))
    for i in range (repeticiones1):
        pais = (input("Introduce un elemento: "))
        lista.append(pais)

def matchs(x,y):
    matches = [item for item in x if item in y]
    if len(matches) == 0:
        print("¡Oops! No ha habido coincidencias")
    else:
        lisf = len(set(matches)) #Creamos esta variable que es la longitud de una lista de coincicendias que no se repiten. Asi averiguamos rapido el numero.
        print("¡Hay", lisf, "coincidencias!") 
        print("En ambas listas se repiten los elementos", set(matches))

if __name__ == "__main__":
    lis1 = []
    print("Vamos a rellenar la primera lista: ")
    rellenar (lis1)
    print("La primera lista es", lis1)
    lis2 =[]
    print("Vamos a rellenar la segunda lista: ")
    rellenar (lis2)
    print("La segunda lista es", lis2)
    matchs(lis1, lis2)


# Ejercicio 6 - Cuaderno 3
# Una universidad acaba de modificar su sistema de representación de la calificación de los alumnos,
# que como es sabido son valores entre 0 y 10. A partir de ahora, se calificarán como “A” las notas mayores
# o iguales a 8,5, “B” las mayores o iguales a 6,5, “C” las calificaciones mayores o iguales a 5, “D” las
# calificaciones mayores o iguales a 3,5, y “F” todas las demás. Programa una función que reciba una 
# calificación numérica y retorne la letra con la nueva calificación. 
# Asegúrate de que la calificación introducida es válida (idea: programa una función lo suficientemente genérica
# que se pueda luego reutilizar en programas que necesiten una validación similar).

def validar_nota():
    while True:
        try:
            x = float(input("¡Dime tu nota!: "))
            if x>10 or x<0:
                raise ValueError
            break
        except:
            print("Entrada no valida, introduce tu nota numerica del 1 al 10")
    print("Tu nota, del 1 al 10, es un:", x)
    return x

def transformar_nota(x):
    if x>=8.5:
        x = "A"
    elif x>=6.5:
        x = "B"
    elif x>=5:
        x = "C"
    elif x>=3.5:
        x = "D"
    else:
        x = "F"
    print("Tu nota con el nuevo sistema es:", x)
    return x

if __name__ == "__main__":
    nota = validar_nota()
    notaletra = transformar_nota(nota)
    print("Tu calificacion ha sido de", nota, "que equivale a una", notaletra)


# Ejercicios 1 - Cuaderno 5.
# Implementa las estructuras de datos que permitan almacenar información 
# anónima sobre personas con objeto de hacer un estudio estadístico. Así, se deberá almacenar
# el número de secuencia, sexo y edad de cada persona. Programe además un par de funciones 
# para (a) leer por teclado datos relativos a una persona y (b) para mostrar dichos datos por pantalla.

class Persona:
    def __init__(self,ns,sx,ed):
        self.num = ns
        self.sexo = sx
        self.edad = ed

def leer_datospersona():
    numsec=str(input("Introduce numero secuencia: "))
    while True:
        try:
            sexo = str(input("Introduce sexo (M/F):"))
            if sexo.lower()=="m" or sexo.lower()=="f":
                sexo=sexo.upper()
            else:
                raise ValueError
            break
        except:
            print("Introduce una M o una F")
    while True:
        try:
            edad = int(input("Introduce edad: "))
            if edad<0:
                raise ValueError
            break
        except:
            print("Introduce un valor positivo")
    p = Persona (numsec, sexo, edad)
    return p


def mostrar_datospersona(p):
    print(p.num,'/',p.sexo,'/',p.edad)

if __name__ == "__main__":
    p = leer_datospersona()
    mostrar_datospersona(p)

# Ejercicio 2 - Cuaderno 5.
# Sin utilizar listas, programa un software que utilice lo programado en el ejercicio 1 
# para leer la edad de 10 personas y calcular la media de edad general, la media por sexo,
# la cantidad de mujeres que tienen entre 13 y 16 años y el número de hombres menores de 20 años.

def mediageneral(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10):
    media=(p1.edad + p2.edad + p3.edad + p4.edad + p5.edad + p6.edad + p7.edad + p8.edad + p9.edad + p10.edad)/10
    return media

def sacardatom(p):
    if p.sexo=="M":
        sacadato=(p.edad)
    else:
        sacadato=0
    return sacadato
    
def sacardatof(p):
    if p.sexo=="F":
        sacadato=(p.edad)
    else:
        sacadato=0
    return sacadato

def divisorm(x):
    d=0
    if x>0:
        d=1
    else:
        d=d
    return d

def divisorf(x):
    d=0
    if x>0:
        d=1
    else:
        d=d
    return d

def f1316(x):
    d=0
    if 16>=x>=13:
        d=1
    else:
        d=d
    return d

def mu20(x):
    d=0
    if 0<x<20:
        d=1
    else:
        d=d
    return d

if __name__ == "__main__":
    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 = leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona(), leer_datospersona()
    print("La media de edad de las 10 personas es de: ", mediageneral(p1, p2,p3, p4, p5, p6, p7, p8, p9, p10), "años")
    edad1m, edad2m, edad3m, edad4m, edad5m, edad6m, edad7m, edad8m, edad9m, edad10m = sacardatom(p1), sacardatom(p2), sacardatom(p3), sacardatom(p4), sacardatom(p5), sacardatom(p6), sacardatom(p7), sacardatom(p8), sacardatom(p9), sacardatom(p10)
    d1m, d2m, d3m, d4m, d5m, d6m, d7m, d8m, d9m, d10m = divisorm(edad1m), divisorm(edad2m), divisorm(edad3m), divisorm(edad4m), divisorm(edad5m), divisorm(edad6m), divisorm(edad7m), divisorm(edad8m), divisorm(edad9m), divisorm(edad10m)
    mediasexom = (edad1m+edad2m+edad3m+edad4m+edad5m+edad6m+edad7m+edad8m+edad9m+edad10m)/(d1m+d2m+d3m+d4m+d5m+d6m+d7m+d8m+d9m+d10m)
    print("Hay", (d1m+d2m+d3m+d4m+d5m+d6m+d7m+d8m+d9m+d10m), "chicos y su media de edad es de", mediasexom, "edad")
    edad1f, edad2f, edad3f, edad4f, edad5f, edad6f, edad7f, edad8f, edad9f, edad10f = sacardatof(p1), sacardatof(p2), sacardatof(p3), sacardatof(p4), sacardatof(p5), sacardatof(p6), sacardatof(p7), sacardatof(p8), sacardatof(p9), sacardatof(p10)
    d1f, d2f, d3f, d4f, d5f, d6f, d7f, d8f, d9f, d10f = divisorf(edad1f), divisorf(edad2f), divisorf(edad3f), divisorf(edad4f), divisorf(edad5f), divisorf(edad6f), divisorf(edad7f), divisorf(edad8f), divisorf(edad9f), divisorf(edad10f)
    mediasexof = (edad1f+edad2f+edad3f+edad4f+edad5f+edad6f+edad7f+edad8f+edad9f+edad10f)/(d1f+d2f+d3f+d4f+d5f+d6f+d7f+d8f+d9f+d10f)
    print("Hay", (d1f+d2f+d3f+d4f+d5f+d6f+d7f+d8f+d9f+d10f), "chicas y su media de edad es de", mediasexof, "años")
    e1, e2, e3, e4, e5, e6, e7, e8, e9, e10 = f1316(edad1f), f1316(edad2f), f1316(edad3f), f1316(edad4f), f1316(edad5f), f1316(edad6f), f1316(edad7f), f1316(edad8f), f1316(edad9f), f1316(edad10f)
    entre=(e1+e2+e3+e4+e5+e6+e6+e8+e9+e10)
    print("Hay", entre, "chicas con edad comprendida entre los 13 y 16 años")
    mm1, mm2, mm3, mm4, mm5, mm6, mm7, mm8, mm9, mm10 = mu20(edad1m), mu20(edad2m), mu20(edad3m), mu20(edad4m), mu20(edad5m), mu20(edad6m), mu20(edad7m), mu20(edad8m), mu20(edad9m), mu20(edad10m)
    print("Hay", (mm1+mm2+mm3+mm4+mm5+mm6+mm7+mm8+mm9+mm10), "chicos con menos de 20 años")


# Ejercicio 3 - Cuaderno 5
# Amplíe el ejercicio anterior mostrando al final del proceso los datos completos de la mujer y
# el hombre más jóvenes de todos los introducidos.

def depuradorm(x):
    if x==0:
        x=777
    else:
        x=x
    return x

def depuradorf(x):
    if x==0:
        x=99
    else:
        x=x
    return x

def compararm(x, edadx1, edadx2, edadx3, edadx4, edadx5, edadx6, edadx7, edadx8, edadx9, edadx10):
    if ((edadx1<edadx2) and (edadx1<edadx3) and (edadx1<edadx4) and (edadx1<edadx5) and (edadx1<edadx6) and (edadx1<edadx7) and (edadx1<edadx8) and (edadx1<edadx9) and edadx1<edadx10):
        print("Los datos de la persona masculina mas joven es: ", (x.num,'/',x.sexo,'/',x.edad))

def compararf(x, edadx1, edadx2, edadx3, edadx4, edadx5, edadx6, edadx7, edadx8, edadx9, edadx10):
    if ((edadx1<edadx2) and (edadx1<edadx3) and (edadx1<edadx4) and (edadx1<edadx5) and (edadx1<edadx6) and (edadx1<edadx7) and (edadx1<edadx8) and (edadx1<edadx9) and edadx1<edadx10):
        print("Los datos de la persona femenina mas joven es: ", (x.num,'/',x.sexo,'/',x.edad))

if __name__ == "__main__":
    #Chicos
    edad1mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm=depuradorm(edad1m), depuradorm(edad2m), depuradorm(edad3m), depuradorm(edad4m), depuradorm(edad5m), depuradorm(edad6m), depuradorm(edad7m), depuradorm(edad8m), depuradorm(edad9m), depuradorm(edad10m)
    compararm(p1, edad1mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p2, edad2mm, edad1mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p3, edad3mm, edad1mm, edad2mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p4, edad4mm, edad1mm, edad2mm, edad3mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p5, edad5mm, edad2mm, edad3mm, edad4mm, edad1mm, edad6mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p6, edad6mm, edad2mm, edad3mm, edad4mm, edad5mm, edad1mm, edad7mm, edad8mm, edad9mm, edad10mm)
    compararm(p7, edad7mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad1mm, edad8mm, edad9mm, edad10mm)
    compararm(p8, edad8mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad1mm, edad9mm, edad10mm)
    compararm(p9, edad9mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad1mm, edad10mm)
    compararm(p10, edad10mm, edad2mm, edad3mm, edad4mm, edad5mm, edad6mm, edad7mm, edad8mm, edad9mm, edad1mm)
    #Chicas
    edad1ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff=depuradorf(edad1f), depuradorf(edad2f), depuradorf(edad3f), depuradorf(edad4f), depuradorf(edad5f), depuradorf(edad6f), depuradorf(edad7f), depuradorf(edad8f), depuradorf(edad9f), depuradorf(edad10f)
    compararf(p1, edad1ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p2, edad2ff, edad1ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p3, edad3ff, edad1ff, edad2ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p4, edad4ff, edad1ff, edad2ff, edad3ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p5, edad5ff, edad2ff, edad3ff, edad4ff, edad1ff, edad6ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p6, edad6ff, edad2ff, edad3ff, edad4ff, edad5ff, edad1ff, edad7ff, edad8ff, edad9ff, edad10ff)
    compararf(p7, edad7ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad1ff, edad8ff, edad9ff, edad10ff)
    compararf(p8, edad8ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad1ff, edad9ff, edad10ff)
    compararf(p9, edad9ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad1ff, edad10ff)
    compararf(p10, edad10ff, edad2ff, edad3ff, edad4ff, edad5ff, edad6ff, edad7ff, edad8ff, edad9ff, edad1ff)


