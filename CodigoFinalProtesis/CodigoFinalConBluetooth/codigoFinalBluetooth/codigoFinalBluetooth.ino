#include <SoftwareSerial.h>
#include <Servo.h>

const int emgPin = A0;

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

     Serial.println("Señal "+emgValue);
     delay(100);

  if(Serial.available()>0){
    char gestos = Serial.read();
    if(gestos == '1'){

    }
    else if(gestos == '2'){

    }
    else if(gestos == '3'){

    }
    else if(gestos == '4'){

    }
    else if(gestos == '5'){

    }
    else if(gestos == '6'){

    }
    else if(gestos == '7'){

    }
    else if(gestos == '8'){

    }
    else if(gestos == '9'){

    }
    else if(gestos == '10'){

    }
    else if(gestos == '11'){

    }
    else if(gestos == '12'){

    }
    else if(gestos == '13'){

    }
    else if(gestos == '14'){

    }
    else if(gestos == '15'){

    }
    else if(gestos == '16'){

    }
    else if(gestos == '17'){

    }
    else if(gestos == '18'){

    }
  }

   
}

