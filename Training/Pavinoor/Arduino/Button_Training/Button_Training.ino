void setup() {
  // put your setup code here, to run once:
  pinMode(13, OUTPUT);
  pinMode(52, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(52)==LOW) {
    digitalWrite(13, HIGH);
    //delay(1000);
  }
  else if (digitalRead(52)==HIGH) {
    digitalWrite(13, LOW);
  }
}
