# Solicitar el nombre del producto 

nombre = input ("Ingrese el nombre del progucto: ")

#solicitar y validar el precio 

while True:
    #se convierte el valor a float 
    valor = input ("Ingresa el valor del producto: ")
    try:
        precio = float (valor)
        if precio < 0:
            print ("El precio no puede ser negativo")
            continue
        break
    except ValueError:
        print ("Valores no validos")
    

#solicitar y validar la cantidad

while True:
    cantidad1 = input ("ingresa la cantidad del producto: " )
    try: 
        cantidad2 = int (cantidad1)
        if cantidad2 < 0:
            print ("La cantidad no puede ser negativa")

            continue
        break
    except ValueError:
        print ("Ingrese un numero valido")

#Calcularo costo total

precio_total = precio * cantidad2

#lo que se va a mostrar en la consola 

print (f"producto: {nombre} - Precio: {precio} - Cantidad: {cantidad2} - Total a pagar: {precio_total}")
