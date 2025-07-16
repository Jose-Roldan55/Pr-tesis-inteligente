import cv2
import mediapipe as mp
import serial
import time

# Configuración del puerto serial para Arduino
arduino = serial.Serial('COMX', 9600)  # Reemplaza 'COMX' con el puerto serial correcto
time.sleep(2)  # Espera a que el puerto se inicie

# Inicializar Mediapipe para la detección de manos
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Inicializar el detector de manos
hands = mp_hands.Hands(max_num_hands=1)

# Función para enviar comandos al Arduino para controlar el servo motor
def enviar_comando_arduino(posicion_servo):
    comando = str(posicion_servo) + '\n'  # Envía la posición del servo como un número seguido de un salto de línea
    arduino.write(comando.encode())

# Función para obtener la posición del dedo índice
def obtener_posicion_dedo_indice(landmarks):
    # La mano es detectada, obtiene la posición del dedo índice
    x = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
    y = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    return x, y

# Main loop para capturar video y controlar el servo
cap = cv2.VideoCapture(0)  # Inicia la captura de video desde la cámara (puede ser 0 o el índice de tu cámara)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Voltea el frame horizontalmente
    frame = cv2.flip(frame, 1)

    # Convierte la imagen a RGB para Mediapipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Si se detecta la mano, obtiene la posición del dedo índice
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x, y = obtener_posicion_dedo_indice(hand_landmarks)

            # Mapea las posiciones del dedo a los valores de servo (0 a 180)
            # Ajusta estos valores según la posición real del servo
            servo_pos = int(x * 180), int(y * 180)

            # Envía los datos al Arduino para controlar el servo
            enviar_comando_arduino(servo_pos)

            # Dibuja un círculo en la posición del dedo índice
            cv2.circle(frame, (int(x * frame.shape[1]), int(y * frame.shape[0])), 10, (0, 255, 0), -1)

    # Muestra el frame
    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera los recursos
cap.release()
cv2.destroyAllWindows()
hands.close()
