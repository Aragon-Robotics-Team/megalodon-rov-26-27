// pick starting servo position
//check change of depth
// read depth function, chexk movement function

//intialize current_depth, previous_depth, change_depth, neutral_bouyancy
//intialize linear servo
#include <ESP32Servo.h>
#include "MS5837.h"
  
MS5837 depthSensor;
int current_depth = 0;
int previous_depth = 0;
int change_depth = 0;
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
    change_depth = current_depth - previous_depth; // do i need change depth? feel like it's not useful
    if (current_depth > previous_depth) {
      movement_val = 1;
    }
    else if (previous_depth > current_depth) {
      movement_val = -1;
    }
    else if (previous_depth == current_depth) { // need to figure out the way to make like a range 
      movement_val = 0;
    }
    else {
      Serial.println("ERROR: floats not moving in percieved directions?"); //should not occur but just making sure
    }
    return movement_val;
  }

void setup() {
  // put your setup code here, to run once:
  // make servo 1450 then half again andf again and again :))
  previous_depth = read_depth(); 
  linear_servo.attach(17); // used from last year code, MEGA pin 9

  while (movement_val != 0) {
    linear_servo.writeMicroseconds(servo_pwm);
    delay (3000);
    previous_depth = current_depth;
    current_depth = read_depth();
    if (check_movement(previous_depth, current_depth) == 1){
      servo_pwm = (servo_pwm + 2300)/2;
    }
    else if (check_movement(previous_depth, current_depth) == -1){
      servo_pwm = (servo_pwm + 600)/2;
    }
  }
}

void loop() {
  // put your main code here, to run repeatedly:
}
