void setup() {
  // put your setup code here, to run once:
  // pin output setup
pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // power for pin that goes on and off between two seconds
digitalWrite(13, HIGH);
delay(2000);
digitalWrite(13,LOW);
delay(2000);

}
