propietarios = {}
print("-"*8 + "Bienvenido usuario" + "-"*8)
vehiculos = int(input("Ingrese cuantos vehiculos desea ingresar: "))
for i in range(vehiculos):
    print(f"Vehiculo #{i + 1}")
    ID = int(input("Ingrese el su numero de NIT: "))
    full_name = input("Ingrese nombre completo: ")
    phone_number = input("Ingrese numero de telefono: ")
    cant_cars = int(input("Ingrese cantida de vehiculos: "))
    for y in range(cant_cars):
        print(f"Vehiculo #{y + 1}")
        placa = input("Ingrese numero de placa: ")
        marca = input("Ingrese marca: ")
        model = input("Ingrese modelo del carro: ")
        year = int(input("Ingrese año del vehiculo: "))
        tax = input("¿Pago impuesto al vehiculo?: ")
