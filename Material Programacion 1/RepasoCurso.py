""""UTN TECHNOLOGIES
UTN Technologies, una reconocida software factory se encuentra en la búsqueda de ideas para su próximo desarrollo en Python, que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
Inteligencia artificial (IA),
Realidad virtual/aumentada (RV/RA),
Internet de las cosas (IOT)
Para ello, la empresa realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas.
A) Los datos a ingresar por cada empleado encuestado son:
nombre del empleado
edad (no menor a 18)
género (Masculino - Femenino - Otro)
tecnologia (IA, RV/RA, IOT)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.
Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
Nombre: BRUNO BUCHARDO
TURNO DIV: TM DIV 111 """

contador_ia_iot_masculino_25_50 = 0
contador_no_ia_no_femenino_33_40 = 0
nombre_max_edad_masculino = ""
edad_max_masculino = 0
tecnologia_max_edad_masculino = ""


for i in range(10):
    
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    while edad < 18:
        edad = int(input("Error: La edad debe ser mayor o igual a 18. Ingrese nuevamente la edad: "))

    genero = input("Ingrese genero (m - Masculino, f - Femenino, nb - Otro): ")
    while genero not in ['m', 'f', 'nb']:
        genero = input("Error: Género ingresado incorrecto. Ingrese nuevamente el género (m/f/nb): ")

    tecnologia = input("Ingrese tecnología (ia - Inteligencia Artificial, iot - Internet de las cosas, rv - Realidad virtual/aumentada): ")
    while tecnologia not in ['ia', 'iot', 'rv']:
        tecnologia = input("Error: Tecnología ingresada incorrecta. Ingrese nuevamente la tecnología (ia/iot/rv): ")

    
    if (genero == 'm') and (edad >= 25 and edad <= 50) and (tecnologia in ['ia', 'iot']):
        contador_ia_iot_masculino_25_50 += 1

    if (genero != 'f') and (edad >= 33 and edad <= 40) and (tecnologia != 'ia'):
        contador_no_ia_no_femenino_33_40 += 1

    if genero == 'm' and edad > edad_max_masculino:
        nombre_max_edad_masculino = nombre
        edad_max_masculino = edad
        tecnologia_max_edad_masculino = tecnologia


porcentaje_no_ia_no_femenino = (contador_no_ia_no_femenino_33_40 / 10) * 100


print("\nCantidad de empleados masculinos que votaron por IA o IOT y tienen entre 25 y 50 años:", contador_ia_iot_masculino_25_50)
print("Porcentaje de empleados que no votaron por IA y su género no es Femenino o su edad está entre 33 y 40:", porcentaje_no_ia_no_femenino)
print("Nombre y tecnología que votó de los empleados masculinos con mayor edad:", nombre_max_edad_masculino, "-", tecnologia_max_edad_masculino)
   
   