const int potInputs[] = {A0,A1};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i <= (sizeof(potInputs)-1)/2; i++) {
    pinMode(potInputs[i], INPUT);
    Serial.println(i);
  }
}

int last_second = 0;

void loop() {
  int potValues[sizeof(potInputs)];
  getPotValues(potValues);
  printSerial(potValues);
}

void getPotValues(int potValues[]) {
  for (int i = 0; i <= (sizeof(potInputs)-1)/2; i++) {
    potValues[i] = map(analogRead(potInputs[i]),0,1023,0,100);
  }
}

void printSerial(int potValues[]) {
  for (int i = 0; i <= (sizeof(potInputs)-1)/2; i++) {
    Serial.print(potValues[i]);
    Serial.print(" ");
  }
  Serial.println("");
}