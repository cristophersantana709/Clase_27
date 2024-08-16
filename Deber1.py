#Carpeta con nombre que diga Clases27
 #tarea: considera que el jugador pueda escribir 
 # las opciones tambien en Mayusculas,
 # capital case(cuando solo la primera letra es mayuscula)
 
opciones = {
    "izquierda":"Te encontraste con un dragon",
    "derecha":"Encontraste un Tesoro",
    "adelante":"Caiste en un pozo"  
}

#solicitamos la opcion al usario
eleccion1 = input("Estas en un cruze. Quieres ir a la derecha, izquierda o adelante?: ").strip()
eleccion2 = eleccion1.lower()
if eleccion2 in opciones:
    print(f"Respuesta: {opciones[eleccion2]}")
else:
    print("opcion equivocada")