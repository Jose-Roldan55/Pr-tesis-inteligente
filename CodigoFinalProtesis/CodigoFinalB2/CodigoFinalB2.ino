#include <SoftwareSerial.h>
#include <Servo.h>

const int emgPin = A0;
const int umbral = 800;

unsigned int temp_value1;
unsigned int temp_value2;

const int servoPinDedo1 = 3;  
const int servoPinDedo2 = 5;
const int servoPinDedo3 = 6;
const int servoPinDedo4 = 9;
const int servoPinDedo5 = 10;

Servo menique;
Servo anular;
Servo medio;
Servo indice;
Servo pulgar;

void set_allservo(int value) {
  menique.write(value);
  anular.write(value);
  medio.write(value);
  indice.write(value);
  pulgar.write(value);
  delay(2);
}

void set_servo(int values) {
  if (values >= 0 && values <= 180) {
    int myservo1 = values;
    menique.write(myservo1);
    delay(2);
  }
  else if (values >= 181 && values <= 361) {
    int myservo2 = values;
    myservo2 = map(myservo2, 181, 361, 0, 180);
    anular.write(myservo2);
    delay(2);
  }
  else if (values >= 362 && values <= 542) {
    int myservo3 = values;
    myservo3 = map(myservo3, 362, 542, 0, 180);
    medio.write(myservo3);
    delay(2);
  }
  else if (values >= 543 && values <= 723) {
    int myservo4 = values;
    myservo4 = map(myservo4, 543, 723, 0, 180);
    indice.write(myservo4);
    delay(2);
  }
  else if (values >= 724 && values <= 904) {
    int myservo5 = values;
    myservo5 = map(myservo5, 724, 904, 0, 180);
    pulgar.write(myservo5);
    delay(2);
  }
  else if (values >= 11000 && values <= 11180) {
    set_allservo(values - 11000);
  }
}

void setup() {
  Serial.begin(9600);

  menique.attach(servoPinDedo1);
  anular.attach(servoPinDedo2);
  medio.attach(servoPinDedo3);
  indice.attach(servoPinDedo4);
  pulgar.attach(servoPinDedo5);

  menique.write(0);
  anular.write(0);
  medio.write(0);
  indice.write(0);
  pulgar.write(0);
}

void loop() {
  int emgValue = analogRead(emgPin);

  if(emgValue > umbral){
    menique.write(180);
    anular.write(180);
    medio.write(180);
    indice.write(180);
    pulgar.write(180);
    delay(100);
  }
  else{
    if(Serial.available() > 1){
    temp_value1 = Serial.read();
    temp_value2 = Serial.read();
    set_servo((temp_value2 * 256) + temp_value1);
  }
  }
     Serial.print("Señal ");
     Serial.println(emgValue);
     delay(100);
}


