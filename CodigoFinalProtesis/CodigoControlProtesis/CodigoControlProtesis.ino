#include <SoftwareSerial.h>
#include <Servo.h>

const int emgPin = A0;

const int umbral = 800;

const int servoPinDedo1 = 3;  
const int servoPinDedo2 = 5;
const int servoPinDedo3 = 6;
const int servoPinDedo4 = 9;
const int servoPinDedo5 = 10;
const int servoPinCodo = 11; 

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

  if(Serial.available()>0){
    char gestos = Serial.read();
    
    if(gestos == 'A'){
        menique.write(180);
        anular.write(180);
        medio.write(180);
    }
    else if(gestos == 'B'){

    }
    else if(gestos == 'C'){

    }
    else if(gestos == 'D'){

    }
    else if(gestos == 'E'){

    }
    else if(gestos == 'F'){

    }
    else if(gestos == 'G'){

    }
    else if(gestos == 'H'){

    }
    else if(gestos == 'I'){

    }
    else if(gestos == 'J'){

    }
    else if(gestos == 'K'){

    }
    else if(gestos == 'L'){

    }
    else if(gestos == 'M'){

    }
    else if(gestos == 'N'){

    }
    else if(gestos == 'O'){

    }
    else if(gestos == 'P'){

    }
    else if(gestos == 'Q'){

    }
    else if(gestos == 'R'){

    }
  }
else{
    menique.write(0);
    anular.write(0);
    medio.write(0);
    indice.write(0);
    pulgar.write(0);
    delay(100);
}
  
   
}

