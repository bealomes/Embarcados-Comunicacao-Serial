#include <Wire.h>

int potPin = A0;  // Pino analógico onde o potenciômetro está conectado
int valorPot;     // Variável para armazenar o valor do potenciômetro

void setup() {
  Wire.begin(0x8);  // Endereço I2C do Arduino
  Wire.onRequest(requestEvent);  // Função que será chamada quando a Raspberry requisitar dados
  Serial.begin(9600);  // Inicializa comunicação serial para monitoramento
}

void loop() {
  // O loop permanece vazio, pois a função `requestEvent` será chamada automaticamente
  delay(100);
}

// Função que é chamada quando a Raspberry solicita dados
void requestEvent() {
  valorPot = analogRead(potPin);  // Leitura do valor do potenciômetro (0 a 1023)
  
  // Dividindo o valor em dois bytes
  byte highByte = (valorPot >> 8);  // 8 bits mais significativos
  byte lowByte = valorPot & 0xFF;   // 8 bits menos significativos
  
  // Enviando os dois bytes via I2C
  Wire.write(highByte);
  Wire.write(lowByte);
  
  // Mostra o valor no monitor serial
  Serial.print("Valor do potenciômetro: ");
  Serial.println(valorPot);
}
