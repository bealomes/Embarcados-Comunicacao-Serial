import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

# Definição dos pinos dos LEDs
LED_VERDE = 18
LED_VERMELHO = 23

# Configuração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_VERMELHO, GPIO.OUT)

# Inicializa o leitor RFID
leitor = SimpleMFRC522()

# Lista de IDs permitidos (IDs cadastrados)
tags_cadastradas = [123456789012]  # Substitua pelos IDs válidos

def controle_acesso():
    try:
        while True:
            print("Aproxime a tag do leitor.")
            id, _ = leitor.read()

            if id in tags_cadastradas:
                GPIO.output(LED_VERDE, GPIO.HIGH)  # Aciona LED verde
                GPIO.output(LED_VERMELHO, GPIO.LOW)  # Apaga LED vermelho
                print("Acesso liberado")
            else:
                GPIO.output(LED_VERMELHO, GPIO.HIGH)  # Aciona LED vermelho
                GPIO.output(LED_VERDE, GPIO.LOW)  # Apaga LED verde
                print("Acesso negado")
            
            sleep(2)  # Aguarda 2 segundos antes da próxima leitura
            GPIO.output(LED_VERDE, GPIO.LOW)
            GPIO.output(LED_VERMELHO, GPIO.LOW)

    except KeyboardInterrupt:
        print("Programa encerrado.")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    controle_acesso()

