#include <SoftwareSerial.h>

SoftwareSerial blue(0, 1);

char NOMBRE[21] = "Protesis";
char BPS = '4';
char PASS[5] = "1234";

void setup()
{ 
blue.begin(9600);

pinMode(13, OUTPUT);
digitalWrite(13, HIGH);
delay(4000);

digitalWrite(13,LOW);

blue.print("AT");
delay(1000);

blue.print("AT+NAME");
blue.print(NOMBRE);
delay(1000);

blue.print("AT+BAUD");
blue.print(BPS);
delay(1000);

blue.print("AT+PIN");
blue.print(PASS);
delay(1000);

}

void loop()
{
  digitalWrite(13, !digitalRead(13));
  delay(300);
}


