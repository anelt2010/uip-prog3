direc_tel = {}
op = 0
while op != 5:
  print("(1)Ver numero de Telefono","\n(2)Agregar Numero de Telefono","\n(3)Eliminar numero de Telefono","\n(4)Buscar numero de Telefono","\n(5)Salir")
  op = int(input("\n\nseleccione la opcion a realizar:\n"))
  if op == 1:
    print("DIRECCTORIO DE CONTACTOS\n" + str(direc_tel) + "\n\n")
  elif op == 2:
    nombre = input("Introduzca el nombre del contacto: ")
    num = int(input("Introduzca el numero del contacto: "))
    direc_tel[nombre] = num
  elif op == 3:
    nombre = input("Introduzca el nombre del contacto: ")
    del direc_tel[nombre]
  elif op == 4:
    nombre = input("Introduzca el nombre del numero que desea ver: ")
    print(str(direc_tel[nombre]) + "\n\n")
