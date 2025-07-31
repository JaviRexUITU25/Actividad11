propietarios = {}
print("-"*8 + "Bienvenido usuario" + "-"*8)
vehiculos = int(input("Ingrese cuantos vehiculos desea ingresar: "))
for i in range(vehiculos):
    print(f"Vehiculo #{i + 1}")
    ID = input("Ingrese el su numero de NIT: ")
    full_name = input("Ingrese nombre completo: ")
    phone_number = input("Ingrese numero de telefono: ")
    cant_cars = int(input("Ingrese cantidad de vehiculos: "))
    for y in range(cant_cars):
        print(f"Vehiculo #{y + 1}")
        placa = input("Ingrese numero de placa: ")
        marca = input("Ingrese marca: ")
        model = input("Ingrese modelo del carro: ")
        year = int(input("Ingrese año del vehiculo: "))
        tax = input("¿Pago impuesto al vehiculo?: ")
    propietarios[ID] = {
            "nombre": full_name,
            "telefono": phone_number,
            "vehiculos": {
                "Placa": placa,
                "marca": marca,
                "modelo": model,
                "año": year,
                "impuesto_pagado": tax
                },
            }
print("-"*8 + "Vehiculos registrados:  " + "-"* 8)
for ID, table in propietarios.items():
    print(f"NIT: {ID}\n"
          f"Nombre: {table["full_name"]}\n"
          f"Telefono: {table["phone_number"]}\n"
          f"vehiculos: {table["cant_cars"]}")
