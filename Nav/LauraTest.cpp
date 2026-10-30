#include <Servo.h>

Servo motor;

int PWM = 1500;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  motor.attach(11);
  while(!Serial)
    delay(10);
}

void loop() {

  if (Serial.available()) {

    PWM = Serial.readStringUntil('-').toInt();
  }
  
}