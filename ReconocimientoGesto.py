import serial
import speech_recognition as sr

arduino_port = 'COM3'
arduino_baudrate = 9600
ser = serial.Serial(arduino_port, arduino_baudrate, timeout=1)

def enviar_comando_arduino(comando):
    ser.write(comando.encode())

def reconocer_comando_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = r.listen(source, timeout=5)

    try:
        print("Reconociendo...")
        command = r.recognize_google(audio, language='es-ES')  # Use Spanish language for recognition
        print("Comando reconocido:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el comando")
    except sr.RequestError as e:
        print("Error al solicitar resultados:", e)
    except Exception as e:
        print("Error:", e)

commands_mapping = {
    'agarré general': 'A',
    'celular': 'B',
    'multiherramienta': 'C',
    'pinza': 'D',
    'teclado': 'E',
    'poner y quitar': 'F',
    'apuntador': 'G',
    'gancho': 'H',
    'precisión': 'I',
    'pinza con tres dedos': 'J',
    'ratón': 'K',
    'activador de un dedo': 'L',
    'activador de dos dedos': 'M',
    'okay': 'N',
    'like': 'O',
    'rock': 'P',
    'saluda': 'Q',
    'amor y paz': 'R',
    'salir': 'exit'
}

while True:
    comando = reconocer_comando_voz()
    if comando:
        if comando in commands_mapping:
            enviar_comando_arduino(commands_mapping[comando])
        elif comando == 'salir':
            ser.close()
            print("Saliendo...")
            break
        else:
            print("Comando no reconocido:", comando)
