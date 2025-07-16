import cv2
import mediapipe as mp
import numpy as np 
from math import acos, degrees
import math

def palm_centroid(coordinates_list):
     coordinates = np.array(coordinates_list)
     centroid = np.mean(coordinates, axis=0)
     centroid = int(centroid[0]), int(centroid[1])
     return centroid
 
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

#Read Camera
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Pulgar
thumb_points = [1, 2, 4]

# Índice, medio, anular y meñique
palm_points = [0, 1, 2, 5, 9, 13, 17]
fingertips_points = [8, 12, 16, 20]
finger_base_points =[6, 10, 14, 18]

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)


def nothing(x):
    pass
#window name
cv2.namedWindow("Ajustes de filtro",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Ajustes de filtro", (300, 300)) 
cv2.createTrackbar("Filtro2", "Ajustes de filtro", 0, 255, nothing)

#COlor Detection Track

cv2.createTrackbar("Bajar_H", "Ajustes de filtro", 0, 255, nothing)
cv2.createTrackbar("Bajar_S", "Ajustes de filtro", 0, 255, nothing)
cv2.createTrackbar("Bajar_V", "Ajustes de filtro", 0, 255, nothing)
cv2.createTrackbar("Aumentar_H", "Ajustes de filtro", 255, 255, nothing)
cv2.createTrackbar("Aumentar_S", "Ajustes de filtro", 255, 255, nothing)
cv2.createTrackbar("Aumentar_V", "Ajustes de filtro", 255, 255, nothing)

with mp_hands.Hands(
     model_complexity=1,
     max_num_hands=1,
     min_detection_confidence=0.5,
     min_tracking_confidence=0.5) as hands:

 while True:
    ret,frame = cap.read()
    if ret == False:
        break
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame,(600,500))
    height, width, _ = frame.shape
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    fingers_counter = "_"
    thickness = [2, 2, 2, 2, 2]
    
    if results.multi_hand_landmarks:
               coordinates_thumb = []
               coordinates_palm = []
               coordinates_ft = []
               coordinates_fb = []
               for hand_landmarks in results.multi_hand_landmarks:
                    
                    x_min, y_min, x_max, y_max = 10000, 10000, 0, 0
                    for landmark in hand_landmarks.landmark:
                         x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                         if x < x_min:
                              x_min = x
                         if x > x_max:
                              x_max = x
                         if y < y_min:
                              y_min = y
                         if y > y_max:
                              y_max = y
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
                    for index in thumb_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_thumb.append([x, y])
                    
                    for index in palm_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_palm.append([x, y])
                    
                    for index in fingertips_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_ft.append([x, y])
                    
                    for index in finger_base_points:
                         x = int(hand_landmarks.landmark[index].x * width)
                         y = int(hand_landmarks.landmark[index].y * height)
                         coordinates_fb.append([x, y])
                         
                         
                    ##########################
                    # Pulgar
                    p1 = np.array(coordinates_thumb[0])
                    p2 = np.array(coordinates_thumb[1])
                    p3 = np.array(coordinates_thumb[2])

                    l1 = np.linalg.norm(p2 - p3)
                    l2 = np.linalg.norm(p1 - p3)
                    l3 = np.linalg.norm(p1 - p2)

                    # Calcular el ángulo
                    angle = degrees(acos((l1**2 + l3**2 - l2**2) / (2 * l1 * l3)))
                    thumb_finger = np.array(False)
                    if angle > 150:
                         thumb_finger = np.array(True)
                    
                    ################################
                    # Índice, medio, anular y meñique
                    nx, ny = palm_centroid(coordinates_palm)
                    cv2.circle(frame, (nx, ny), 3, (0, 255, 0), 2)
                    coordinates_centroid = np.array([nx, ny])
                    coordinates_ft = np.array(coordinates_ft)
                    coordinates_fb = np.array(coordinates_fb)

                    # Distancias
                    d_centrid_ft = np.linalg.norm(coordinates_centroid - coordinates_ft, axis=1)
                    d_centrid_fb = np.linalg.norm(coordinates_centroid - coordinates_fb, axis=1)
                    dif = d_centrid_ft - d_centrid_fb
                    fingers = dif > 0
                    fingers = np.append(thumb_finger, fingers)
                    fingers_counter = str(np.count_nonzero(fingers==True))
                    
                    for (i, finger) in enumerate(fingers):
                         if finger == True:
                              thickness[i] = -1

                    mp_drawing.draw_landmarks(
                         frame,
                         hand_landmarks,
                         mp_hands.HAND_CONNECTIONS,
                         landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 165, 0), circle_radius=5),
                         connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2)
                    )
                    
    # Get hand data from the rectangle sub window
    cv2.rectangle(frame, (0,1), (300,500), (255, 0, 0), 0)
    crop_image = frame[1:500, 0:300]
    # Step  - 2 - 
    hsv = cv2.cvtColor(crop_image, cv2.COLOR_BGR2HSV)
    #detecting hand
    l_h = cv2.getTrackbarPos("Bajar_H", "Ajustes de filtro")
    l_s = cv2.getTrackbarPos("Bajar_S", "Ajustes de filtro")
    l_v = cv2.getTrackbarPos("Bajar_V", "Ajustes de filtro")

    u_h = cv2.getTrackbarPos("Aumentar_H", "Ajustes de filtro")
    u_s = cv2.getTrackbarPos("Aumentar_S", "Ajustes de filtro")
    u_v = cv2.getTrackbarPos("Aumentar_V", "Ajustes de filtro")
    
    #Step -3
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])
    
    #step -4
    #Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    #filter mask with image
    filtr = cv2.bitwise_and(crop_image, crop_image, mask=mask)
    
    #step - 5 
    mask1  = cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos("Filtro2", "Ajustes de filtro") #getting track bar value
    ret,thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
    dilata = cv2.dilate(thresh,(3,3),iterations = 6)
    
    #step - 6 
    #findcontour(img,contour_retrival_mode,method)
    cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    
    try:
        #print("try")
        
        #Step -7
        # Find contour with maximum area
        cm = max(cnts, key=lambda x: cv2.contourArea(x))
        #print("C==",cnts)
        epsilon = 0.0005*cv2.arcLength(cm,True)
        data= cv2.approxPolyDP(cm,epsilon,True)
        
        hull = cv2.convexHull(cm)
        
        cv2.drawContours(crop_image, [cm], -1, (50, 50, 150), 2)
        cv2.drawContours(crop_image, [hull], -1, (0, 255, 0), 2)
        
        #Step -8
        # Find convexity defects
        hull = cv2.convexHull(cm, returnPoints=False)
        defects = cv2.convexityDefects(cm, hull)
        count_defects = 0
        #print("Area==",cv2.contourArea(hull) - cv2.contourArea(cm))
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
           
            start = tuple(cm[s][0])
            end = tuple(cm[e][0])
            far = tuple(cm[f][0])
            
            #Cosin Rule
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14
            #print(angle)
            # if angle > 50 draw a circle at the far point
            if angle <= 50:
                count_defects += 1
                cv2.circle(crop_image,far,5,[255,255,255],-1)
           
    except:
        pass
    
    
    cv2.rectangle(frame, (150, 10), (200, 50), WHITE, thickness[0])
    cv2.putText(frame, "Pulgar", (150, 70), 1, 1, (255, 255, 255), 2)
          # Índice
    cv2.rectangle(frame, (210, 10), (260, 50), BLUE, thickness[1])
    cv2.putText(frame, "Indice", (210, 70), 1, 1, (255, 255, 255), 2)
          # Medio
    cv2.rectangle(frame, (270, 10), (320, 50), GREEN, thickness[2])
    cv2.putText(frame, "Medio", (270, 70), 1, 1, (255, 255, 255), 2)
          # Anular
    cv2.rectangle(frame, (330, 10), (380, 50), RED, thickness[3])
    cv2.putText(frame, "Anular", (330, 70), 1, 1, (255, 255, 255), 2)
          # Menique
    cv2.rectangle(frame, (390, 10), (440, 50), CYAN, thickness[4])
    cv2.putText(frame, "Menique", (390, 70), 1, 1, (255, 255, 255), 2)
        
    cv2.imshow("Filtro2", thresh)
    #cv2.imshow("mask==",mask)
    cv2.imshow("Filtro1",filtr)
    cv2.imshow("Reconocimiento", frame)

    key = cv2.waitKey(25) &0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
    
    
  