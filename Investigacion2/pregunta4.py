import socket
ip = input("IP: ")
inicio = int(input("Inicio:"))
final= int(input("Final:"))
print ("Escaneando desde el Puerto %s al puerto %s." % (inicio,final))
conexion = socket.socket()
for i in range(inicio,final+1):
	try:
		conexion.connect( (ip, i) )
		print ("Puerto : %s Abierto." % i)
	except:
			print ("Puerto : %s Cerrado." % i)
conexion.close()