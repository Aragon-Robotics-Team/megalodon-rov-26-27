void setup() {
  // put your setup code here, to run once:
  //speed of the message
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // telling the Arduino to keep seeking out and reading/sending messages in the serial monitor until it reaches the letter "s"
  if (Serial.available()>(0)) {
    Serial.println(Serial.readStringUntil(s));
  }

}
