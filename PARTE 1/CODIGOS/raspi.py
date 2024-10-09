import smbus
import time

# Endereço I2C do Arduino
address = 0x08

# Inicializa o barramento I2C
bus = smbus.SMBus(1)

def read_potentiometer():
    # Solicita 2 bytes do Arduino
    data = bus.read_i2c_block_data(address, 0, 2)
    
    # Converte os dois bytes de volta para um valor inteiro de 10 bits
    valor = data[0] * 256 + data[1]
    
    return valor

while True:
    # Lê o valor do potenciômetro
    pot_value = read_potentiometer()
    
    # Exibe o valor no terminal
    print(f"Valor do potenciômetro: {pot_value}")
    
    time.sleep(1)
