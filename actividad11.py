propietarios = {}
print("-"*8 + "Bienvenido usuario" + "-"*8)
cantidad = int(input("Ingrese cuantos propietarios desea ingresar: "))
for i in range(cantidad):
    print(f"Propietario #{i+1}")
    ID = input("Ingrese el su numero de NIT: ")
    full_name = input("Ingrese nombre completo: ")
    phone_number = input("Ingrese numero de telefono: ")
    cant_cars = int(input("Ingrese cantidad de vehiculos: "))
    vehiculos = {}
    for y in range(cant_cars):
        print(f"Vehiculo #{y+1}")
        placa = input("Ingrese numero de placa: ")
        marca = input("Ingrese marca: ")
        model = input("Ingrese modelo del carro: ")
        year = int(input("Ingrese año del vehiculo: "))
        tax = input("¿Pago impuesto al vehiculo?(Si/No): ").lower()
    propietarios[placa] = {
                "Placa": placa,
                "marca": marca,
                "modelo": model,
                "año": year,
                "impuesto_pagado": tax
    }
propietarios[ID] = {
    "Nombre": full_name,
    "Telefono": phone_number,
}
print("-"*8 + "Vehiculos registrados:  " + "-"* 8)
for ID, table in propietarios.items():
    print(f"NIT: {ID}\n"
          f"Nombre: {table["full_name"]}\n"
          f"Telefono: {table["phone_number"]}\n"
          f"vehiculos: {table["cant_cars"]}\n"
          f"Placa:{table["placa"]}\n"
          f"Marca:{table["marca"]}\n"
          f"modelo: {table["model"]}\n"
          f"año: {table["year"]}\n"
          f"¿Impuesto pagado?: {table["tax"]}")
print("-"*8 + "Busqueda de propietario: "+ "-"*8)
search = input("Ingrese NIT del propietario a buscar: ")
if search in propietarios:
    propietarios = propietarios[search]
    print(f"Propietario encontrado: \n"
          f"Nombre: {search["full_name"]}\n"
          f"Telefono: {table["phone_number"]}\n"
          f"vehiculos: {table["cant_cars"]}\n"
          f"Placa:{table["marca"]}\n"
          f"modelo: {table["model"]}\n"
          f"año: {table["year"]}\n"
          f"¿Impuesto pagado?: {table["tax"]}")
else:
    print("NIT no encontrado, intente de nuevo.")
