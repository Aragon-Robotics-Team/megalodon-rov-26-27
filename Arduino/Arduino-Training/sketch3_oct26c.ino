void setup() {
  // put your setup code here, to run once:
  // pin and output/inpur setup that connects button on breadboard to arduino (+pull-up for input for higher voltage!)
  pinMode(13, OUTPUT);
  pinMode(52, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  // computer checks to see if pin 52 voltage is low while button is pressed, pin 13 becomes high and sends power for LED on the Arduino to light up
  if (digitalRead(52) == LOW) {
    digitalWrite(13, HIGH);
  }
  //simply the other possibilty of the change in power when the actions of the pins are reversed.
  else if (digitalRead(52) == HIGH) {
    digitalWrite(13, LOW);
  }
  

  
}
