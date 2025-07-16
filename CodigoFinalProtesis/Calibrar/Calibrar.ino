#include <Servo.h>

Servo dedo1;
Servo dedo2;
Servo dedo3;
Servo dedo4;
Servo dedo5;

void setup() {
  dedo1.attach(3);
   dedo2.attach(5);
    dedo3.attach(6);
     dedo4.attach(9);
      dedo5.attach(10);
      
}

void loop() {
  dedo1.write(0);
  delay(1000);
  dedo1.write(90);
  delay(2000);

  dedo2.write(0);
  delay(1000);
  dedo2.write(90);
  delay(2000);

  dedo3.write(0);
  delay(1000);
  dedo3.write(90);
  delay(2000);

  dedo4.write(0);
  delay(1000);
  dedo4.write(90);
  delay(2000);

  dedo5.write(0);
  delay(1000);
  dedo5.write(90);
  delay(3000);
  dedo5.write(180);
  delay(2000);

}
