num = 0
n = 0
convtc = 0
convtd = ""
while num != 6: #aqui inicia el ciclo repetitivo
    print("\n\n\t\tSELECCIONE LA OPCION QUE DESEA REALIZAR\n")
    print("(1)Introducir texto\t (2)Cifrar text\t (3)Decifrar texto\t (4)Imprimir texto Cifrado\t (5)Imprimir texto Decifrado\t (6)salir\n")    #aqui creamos el menu
    num = int(input())
    if num == 1:
        tex = input("Introduzca el texto que desea cifrar o desifrar")
    elif num == 2:      #esta es la opcion que cifra el texto
        n = int(input("cuantas letras tiene el texto:\t"))
        for x in range(n):
            print("Escriba el texto por letra para su cifrado:\t")
            texen = input()
            conv1 = (ord(texen)+1)  #En esta parte convierte el texto en su valor numerico
            conv2 = chr(conv1)      #En esta parte convierte el valor numerico a caracter
            convtc = str(convtc) + conv2  # aqui acumulamos las variables para conseguir el texto cifrado
    elif num == 3:      #esta es la opcion que decifra el texto
        n = int(input("cuantas letras tiene el cifrado:\t"))
        for x in range(n):
            print("Escriba el texto por letra para el decifrado:\t")
            texen = input()
            conv1 = (ord(texen)-1)  #En esta parte convierte el texto en su valor numerico
            conv2 = chr(conv1)      #En esta parte convierte el valor numerico a caracter
            convtd = str(convtd) + conv2    # aqui acumulamos las variables para conseguir el texto cifrado
    elif num == 4:      #esta es la opcion que te imprime el texto cifrado en pantalla
        print("el texto cifrado es:\t" + str(convtc))
    elif num == 5:      #esta es la opcion que te imprime el texto decifrado en pantalla
        print("el texto cifrado es:\t" + str(convtd))
