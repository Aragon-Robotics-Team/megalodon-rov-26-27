const int analogPin = A0; 
int val = 0;
float correct = 1/4.19;
//Calibrated to lighting in Sipple's Room? Not exactly sure how it works

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  while(!Serial)
    delay(10);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(analogPin)*correct;
  Serial.print("Val: ");
  Serial.println(val);
  delay(10);
}
