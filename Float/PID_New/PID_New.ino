// pick starting servo position
//check change of depth
// read depth function, chexk movement function

//intialize current_depth, previous_depth, change_depth, neutral_bouyancy
//intialize linear servo
#include <ESP32Servo.h>
#include "MS5837.h"
#include <StackArray.h>
#include <Wire.h>
  
MS5837 depthSensor;
float current_depth = 0;
float previous_depth = 0;
float change_depth = 0;
StackArray <float> myStack;
int movement_val = 3;
int servo_pwm = 1450;
Servo linear_servo;

// need to wakw up teh sensor somewhere over here, dont know how t odo that
  float read_depth() {
    //i acc have zero idea how to right this, assuming we have the blue robotics one
    depthSensor.read();
    return depthSensor.depth();
}
  int check_movement() {
    float current_depth = myStack.pop();
    float previous_depth = myStack.peek();
    myStack.push(current_depth);
    change_depth = current_depth - previous_depth;
     if (abs(change_depth) < 0.05) {
      movement_val = 0;
    }
    else if (current_depth > previous_depth) {
      movement_val = 1;
    }
    else if (previous_depth > current_depth) {
      movement_val = -1;
    }
    else {
      Serial.println("ERROR: floats not moving in percieved directions?"); //should not occur but just making sure
    }
    return movement_val;
  }

void setup() {
  // put your setup code here, to run once:
  // make servo 1450 then half again andf again and again :))
  Serial.begin(9600)
  Wire.begin();
  depthSensor.init();

  myStack.push(read_depth()); 
  linear_servo.attach(17); // used from last year code, MEGA pin 9

  while (movement_val != 0) {
    linear_servo.writeMicroseconds(servo_pwm);
    delay (3000);
    previous_depth = myStack.peek();
    myStack.push(read_depth());
    if (check_movement() == 1){
      servo_pwm = (servo_pwm + 2300)/2;
    }
    else if (check_movement() == -1){
      servo_pwm = (servo_pwm + 600)/2;
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}
