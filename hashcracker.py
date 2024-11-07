import hashlib
hashFile = "9f86d081884c7d59a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"

dicFiles = input("Ingrese la direccion del archivo del diccionario: ")

with open(dicFiles, "r")as file:
    diccionario = [line.strip() for line in file]
    for password in diccionario:
        hashCalculado = hashlib.sha256(password.encode()).hexdigest()
        if hashCalculado == hashFile:
            print("La contraseña original es: " + password)
            break
        else:
            print("La contraseña no se encuentra en el diccionario")