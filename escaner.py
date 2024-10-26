#escaner de puertos IP
#importamos libreria
import socket
#Pedimos al usuario
ip = input("Ingrese la dirección IP a escanear: ")
#Creamos un bucle  FOR para escanear los puertos
for puerto in range(1, 65535):
    #Especifica que ip estamos usando, socket stream es porque usamos el socket tcp
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    #Para conectarnos al puerto
    result = sock.connect_ex((ip, puerto))

    if result == 0:
        print("Puerto Abierto: " + (puerto))
        sock.close()
    else:
        #si no es 0 colocamos que este cerrado
        print("Puerto Cerrado: " + str(puerto))

#para hacer que funcione le damos a enter y espacio, no le damos a ejecutar; mejorar.
#40.127.217.108 ip de prueba


