nombre = input("Ingrse el nombre del vendedor:")
ventt = 0
for x in range(3):
    ventm = int(input("Ingrese las ventas del mes"))
    ventt = ventt + ventm
    comi = (12.5/100) * ventt

print("\n\t\tINFORME DE COMISIONES"+"\nVendedor"+"\tVentas"+"\t\tComisiones\n" +(nombre) +"\t\t" + str(ventt) + "\t\t" + str(comi))
