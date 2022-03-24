from sqlite3 import Error
from pymongo import MongoClient

try:
    cluster = MongoClient(
        "mongodb+srv://JoseG859:1234@cluster0.xsicy.mongodb.net/Slang?retryWrites=true&w=majority")

    print("Conexion exitosa")
except Error:
    print("Conexion fallida")

try:
    db = cluster
    con = db
    print("Creacion exitosa")
except Error:
    print("Error en creacion")

print("DICCIONARIO DE SLANG 507")
print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES:")
print("1: Agregar")
print("2: Editar")
print("3: Eliminar")
print("4: Ver listado")
print("5: Buscar significado")
seleccion = int(input(""))

if seleccion == 1:

    id = int(input("ID: "))
    palabra = input("Slang: ")
    definicion = input("definicion: ")

    try:
        db = cluster["Slang"]
        con = db["Slang"]
        agregar = {"_id": id, "palabra": palabra, "definicion": definicion}
        con.insert_one(agregar)
        print("Insercion exitosa")
    except Error:
        print("Error en insercion")

elif seleccion == 2:

    try:
        editar_palabra = input("Palabra a editar: ")
        editar_definicion = input("Nueva definicion: ")
        db = cluster["Slang"]
        con = db["Slang"]
        buscar = con.update_one({"palabra": editar_palabra},{"$set":{"definicion":editar_definicion}})
        print("Actualizacion exitosa")
    except Error:
        print("Error al actualizar datos")

elif seleccion == 3:

    try:

        remover = input("Eliminar: ")
        db = cluster["Slang"]
        con = db["Slang"]
        eliminar = con.delete_one({"palabra": remover})
        print("Registro Eliminado")
    except Error:
        print("Error al eliminar")

elif seleccion == 4:
    try:
        db = cluster["Slang"]
        con = db["Slang"]
        buscar = con.find({})
        for busqueda in buscar:
            print(busqueda)

    except:
        print("Error al traer datos")

elif seleccion == 5:
    try:
        peticion = input("Buscar: ")
        db = cluster["Slang"]
        con = db["Slang"]
        buscar = con.find({"palabra":peticion})

        for busqueda in buscar:
            print(busqueda)

    except Error:
        print("Error al traer datos")