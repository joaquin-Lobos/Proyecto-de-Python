import csv
import re

def guardar_en_RAM():

    with open('inventario.csv', newline='') as csvfile:
        codigos = []
        cantidad = []
        peso_individual = []
        descripciones = []
        reader = list(csv.DictReader(csvfile))
        for i in reader:
            codigos.append(i.get("codigo"))
            cantidad.append(i.get("cantidad"))
            peso_individual.append(i.get("peso_individual"))
            descripciones.append(i.get("descripcion"))
        return codigos, cantidad, peso_individual, descripciones        
            




def ingresar():

    codigos, cantidad2, peso_individual2, descripciones = guardar_en_RAM()
    print("ingresar")

    inventario_csv = open("inventario.csv", "w", newline='')
    header = ["codigo", "cantidad", "peso_individual", "descripcion"]
    writer = csv.DictWriter(inventario_csv, fieldnames=header)
    writer.writerow({"codigo": "codigo", "cantidad": "cantidad", "peso_individual": "peso_individual", "descripcion": "descripcion"})


    codigo_producto = int(input("Ingrese el codigo del producto\n"))
    verdadero = False
    contador = -1
    if len(codigos) > 0:
        for i in codigos:
            contador += 1
            if i == str(codigo_producto):
                respuesta = str(input("codigo ya existente, desea agregar más cantidad de ese producto? Y / N\n"))
                if respuesta == "Y":
                    verdadero = True
                    cantidad = int(input("Ingrese la cantidad que desea agregar\n"))
                    nueva_cantidad = float(cantidad2[contador]) + cantidad
                    cantidad2[contador] = nueva_cantidad
                    break
                elif respuesta == "N":
                    break
                else:
                    print("codigo no existente")
                    break
            elif contador + 1 == len(codigos) and verdadero == False:
                descripcion = str(input("Ingrese una descricion para el producto\n"))
                cantidad = int(input("Ingrese la cantidad de unidades del producto\n"))
                peso_individual = float(input("Ingrese el peso por unidad\n"))
                
                writer.writerow({"codigo": codigo_producto, "cantidad": cantidad, "peso_individual": peso_individual, "descripcion": descripcion})
    else:
        descripcion = str(input("Ingrese una descricion para el producto\n"))
        cantidad = int(input("Ingrese la cantidad de unidades del producto\n"))
        peso_individual = float(input("Ingrese el peso por unidad en kilogramos\n"))
                
        writer.writerow({"codigo": codigo_producto, "cantidad": cantidad, "peso_individual": peso_individual, "descripcion": descripcion})

    if len(codigos) > 0:
        contador = 0
        while True:
            writer.writerow({"codigo": codigos[contador], "cantidad": cantidad2[contador], "peso_individual": peso_individual2[contador], "descripcion": descripciones[contador]})
            contador += 1
            if contador == len(codigos):
                break



def retirar():

    codigos, cantidad2, peso_individual2, descripciones = guardar_en_RAM()
    print("retirar")
    codigo_producto = str(input("Ingrese el codigo del producto\n"))
    contador = -1
    if len(codigos) > 0:
        for i in codigos:
            contador += 1
            if i == codigo_producto:
                cantidad_deseada = float(input("Ingrese la cantidad que desea en kilogramos\n"))
                cantidad_retirada = cantidad_deseada / float(peso_individual2[contador])
                if cantidad_retirada < float(cantidad2[contador]):
                    nueva_cantidad = float(cantidad2[contador]) - cantidad_retirada
                    cantidad2[contador] = nueva_cantidad
                    print("usted retiró", cantidad_retirada, descripciones[contador])
                    break
                else:
                    print("no hay suficiente stock")
                    break
            elif contador + 1 == len(codigos):
                print("codigo no existente")
    
        inventario_csv = open("inventario.csv", "w", newline='')
        header = ["codigo", "cantidad", "peso_individual", "descripcion"]
        writer = csv.DictWriter(inventario_csv, fieldnames=header)
        writer.writerow({"codigo": "codigo", "cantidad": "cantidad", "peso_individual": "peso_individual", "descripcion": "descripcion"})
        
        contador = 0
        while True:
            writer.writerow({"codigo": codigos[contador], "cantidad": cantidad2[contador], "peso_individual": peso_individual2[contador], "descripcion": descripciones[contador]})
            contador += 1
            if contador == len(codigos):
                break         
    else:
        print("actualmente no hay objetos en el inventario para retirar")

while True:
    decision = str(input("Ingrese I para ingresar stock o R para retirar stock o nada para salir\n"))
    if decision == "I":
        ingresar()
    elif decision == "R":
        retirar()
    elif decision == "":
        break
    else:
        print("Comando inexistente, pruebe otra vez")