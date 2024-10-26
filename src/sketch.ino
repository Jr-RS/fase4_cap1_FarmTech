// Configurações
#include <DHT.h>
#define DHTPIN 21       // Pino conectado ao DHT22
#define DHTTYPE DHT22   // Definindo o tipo de sensor DHT22
DHT dht(DHTPIN, DHTTYPE);  // Inicializa o sensor DHT22

const int trigPin = 23;  // Pino TRIG do HC-SR04
const int echoPin = 22;  // Pino ECHO do HC-SR04

const int pirPin = 19;   // Pino do sensor PIR

const int ldrPin = 34;   // Pino analógico do LDR

void setup() {
  Serial.begin(115200);
  Serial.println("Inicializando!");
  
  dht.begin();  // Inicializa o sensor DHT22

  // Inicializa o sensor HC-SR04
  pinMode(trigPin, OUTPUT);  // Configura o pino TRIG como saída
  pinMode(echoPin, INPUT);   // Configura o pino ECHO como entrada
  
  // Inicializa o sensor PIR
  pinMode(pirPin, INPUT);    // Configura o pino do PIR como entrada
}

void loop() {
  // Leitura do sensor DHT22 (umidade e temperatura)
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();
  Serial.print("Leitura do Sensor DHT22: ");

  if (isnan(temp) || isnan(hum)) {
    Serial.println("Falha ao ler do sensor DHT22!");
  } else {
    Serial.print("Temperatura: ");
    Serial.print(temp);
    Serial.print(" °C, ");

    Serial.print("Umidade: ");
    Serial.print(hum);
    Serial.println(" %");
  }

  // Leitura do sensor HC-SR04 (distância)
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);  // Calcula o tempo do pulso ECHO
  float distance = (duration / 2.0) * 0.0343;  // Calcula a distância em cm
  Serial.print("Leitura do Sensor HC-SR04: ");

  if (duration == 0) {
    Serial.println("Falha ao medir a distância!");
  } else {
    Serial.print("Distância: ");
    Serial.print(distance);
    Serial.println(" cm");
  }

  // Leitura do sensor PIR (movimento)
  int pirValue = digitalRead(pirPin);
  Serial.print("Leitura do Sensor PIR: ");
  if (pirValue == HIGH) {
    Serial.println("Movimento detectado!");
  } else {
    Serial.println("Nenhum movimento detectado.");
  }

  // Leitura do sensor LDR (luz)
  int ldrValue = analogRead(ldrPin);
  Serial.print("Leitura do Sensor LDR: ");
  Serial.print("Intensidade da luz: ");
  Serial.println(ldrValue);

  Serial.println("--------------");
  delay(2000); // velocidade da simulação (2 segundos)
}