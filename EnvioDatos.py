import serial
import time

arduino_port = 'COM3'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

def enviar_comando_arduino(comando):
    ser.write(comando.encode())
    time.sleep(0.1) 

def mostrar_menu():
    print("Selecciona un gesto de la mano:")
    print("1. Agarre general")
    print("2. Celular")
    print("3. Multiherramienta")
    print("4. Pinza")
    print("5. Teclado")
    print("6. Poner y quitar")
    print("7. Apuntador")
    print("8. Gancho")
    print("9. Precision")
    print("10. Pinza con 3 dedos")
    print("11. Raton")
    print("12. Activador de 1 dedo")
    print("13. Activador de 2 dedos")
    print("14. Ok")
    print("15. Like")
    print("16. Gesto Rock")
    print("17. Saluda")
    print("18. Amor y paz")

while True:
    mostrar_menu()
    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == '1':
        enviar_comando_arduino('A')
    elif opcion == '2':
        enviar_comando_arduino('B')
    elif opcion == '3':
        enviar_comando_arduino('C')
    elif opcion == '4':
        enviar_comando_arduino('D')
    elif opcion == '5':
        enviar_comando_arduino('E')
    elif opcion == '6':
        enviar_comando_arduino('F')
    elif opcion == '7':
        enviar_comando_arduino('G')
    elif opcion == '8':
        enviar_comando_arduino('H')
    elif opcion == '9':
        enviar_comando_arduino('I')
    elif opcion == '10':
        enviar_comando_arduino('J')
    elif opcion == '11':
        enviar_comando_arduino('K')
    elif opcion == '12':
        enviar_comando_arduino('L')
    elif opcion == '13':
        enviar_comando_arduino('M')
    elif opcion == '14':
        enviar_comando_arduino('N')
    elif opcion == '15':
        enviar_comando_arduino('O')
    elif opcion == '16':
        enviar_comando_arduino('P')
    elif opcion == '17':
        enviar_comando_arduino('Q')
    elif opcion == '18':
        enviar_comando_arduino('R')
        
    elif opcion == '0':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")