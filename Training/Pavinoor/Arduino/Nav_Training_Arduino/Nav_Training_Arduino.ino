#include <Servo.h>

int horizontal_frontright_PWM;
int horizontal_bottomright_PWM;
int horizontal_frontleft_PWM;
int horizontal_bottomleft_PWM;
int vertical_frontright_PWM;
int vertical_bottomright_PWM;
int vertical_frontleft_PWM;
int vertical_bottomleft_PWM;

int value = 1500;

Servo horizontal_frontright;
Servo horizontal_bottomright;
Servo horizontal_frontleft;
Servo horizontal_bottomleft;
Servo vertical_frontright;
Servo vertical_bottomright;
Servo vertical_frontleft;
Servo vertical_bottomleft;

void setup() {
  // put your setup code here, to run once:
    horizontal_frontright.attach(6);
    horizontal_frontleft.attach(7);
    horizontal_bottomright.attach(8);
    horizontal_frontright.attach(9);
    vertical_frontright.attach(10);
    vertical_frontleft.attach(11);
    vertical_bottomright.attach(12);
    vertical_bottomleft.attach(13);
}

void loop() {
  // put your main code here, to run repeatedly:
    if (Serial.available()) {
        int horizontal_frontleft_PWM = Serial.readStringUntil('/').toInt();
        horizontal_frontleft.writeMicroseconds(horizontal_frontleft_PWM);

        int horizontal_frontright_PWM = Serial.readStringUntil('+').toInt();
        horizontal_frontright.writeMicroseconds(horizontal_frontright_PWM);

        int horizontal_bottomleft_PWM = Serial.readStringUntil('=').toInt();
        horizontal_bottomleft.writeMicroseconds(horizontal_bottomleft_PWM);

        int horizontal_bottomright_PWM = Serial.readStringUntil('}').toInt();
        horizontal_bottomright.writeMicroseconds(horizontal_bottomright_PWM);

        int vertical_frontleft_PWM = Serial.readStringUntil('-').toInt();
        vertical_frontleft.writeMicroseconds(vertical_frontleft_PWM);

        int vertical_frontright_PWM = Serial.readStringUntil('*').toInt();
        vertical_frontright.writeMicroseconds(vertical_frontright_PWM);

        int vertical_bottomleft_PWM = Serial.readStringUntil(',').toInt();
        vertical_bottomleft.writeMicroseconds(vertical_bottomleft_PWM);
        
        int vertical_bottomright_PWM = Serial.readStringUntil('\\').toInt();
        vertical_bottomright.writeMicroseconds(vertical_bottomright_PWM);
    }


}
