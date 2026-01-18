const int enA = 11;
const int in1 = 6;
const int in2 = 9;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  Serial.begin(115200); 

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'w') {  //forward
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 255);
    } else if (command == 's') { //back
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      analogWrite(enA, 255);
    } else if (command == 'x') { //stop
      digitalWrite(in1, LOW);
      digitalWrite(in2, LOW);
      analogWrite(enA, 0);
    }
  }
}
