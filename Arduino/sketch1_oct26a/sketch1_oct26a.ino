void setup() {
  // put your setup code here, to run once:
  // printed message "hello world" in serial monitor, only this time the two words come seperatly with the third word appearing on the same line as the second.
  //speed of message set to 9600 bits
Serial.begin(9600);
delay(3500);
Serial.println("hello");
Serial.print("world");

}

void loop() {
  // put your main code here, to run repeatedly:

}
