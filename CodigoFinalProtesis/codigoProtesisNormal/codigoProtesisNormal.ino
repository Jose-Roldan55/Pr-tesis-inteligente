#include <SoftwareSerial.h>
#include <Servo.h>

const int emgPin = A0; 
const int umbral = 800;

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

void setup() {
  Serial.begin(9600);

  menique.attach(servoPinDedo1);
  anular.attach(servoPinDedo2);
  medio.attach(servoPinDedo3);
  indice.attach(servoPinDedo4);
  pulgar.attach(servoPinDedo5);

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
    menique.write(0);
    anular.write(0);
    medio.write(0);
    indice.write(0);
    pulgar.write(0);
    delay(100);
    }
     Serial.print("Señal ");
     Serial.println(emgValue);
     delay(100);
}




