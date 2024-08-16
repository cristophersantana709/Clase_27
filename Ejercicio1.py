#declaramos un diccionario

opciones = {
    "izquierda":"Te encontraste con un dragon",
    "derecha":"Encontraste un Tesoro",
    "adelante":"Caiste en un pozo"  
}

#solicitamos la opcion al usario
eleccion = input("Estas en un cruze. Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta:" , opciones[eleccion])
else:
    print("opcion equivocada")