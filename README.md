# Embarcados-Comunicacao-Serial

## __Parte 1: I2C - comunicação serial entre Raspberry Pi e microcontrolador__


Nesta parte da prática, foi implementada uma comunicação serial I2C entre uma Raspberry Pi, executando Linux embarcado, e um microcontrolador (como o Arduino ou ESP32). O objetivo era realizar a leitura de dados analógicos, como a posição de um potenciômetro, utilizando o microcontrolador para converter esses sinais e enviá-los à Raspberry Pi via I2C.
A Raspberry Pi não possui conversores analógico-digitais (ADC) integrados. Assim, o microcontrolador, com seu ADC e capacidade de operar em tempo real, foi empregado para coletar os dados analógicos. A comunicação ocorreu via barramento I2C, onde a Raspberry Pi atuou como dispositivo "controlador" e o microcontrolador como "controlado".
Encontrou-se na integração uma diferença nos níveis lógicos dos dispositivos: a Raspberry Pi opera a 3.3V, enquanto o Arduino trabalha com 5V. Por isso, foi necessário utilizar um conversor de nível lógico para proteger os componentes e garantir uma comunicação segura. O protocolo I2C utiliza duas linhas principais: SDA (dados) e SCL (clock), que possibilitam a troca de informações de forma sincronizada.
A parte prática envolveu a criação de um programa no Arduino para realizar a leitura analógica e enviar os dados via I2C. Na Raspberry Pi, foi desenvolvido um script em Python utilizando a biblioteca SMBus para receber e processar esses dados. Como o ADC do microcontrolador gera um valor de 10 bits, a transmissão foi dividida em dois bytes que, posteriormente, foram recombinados na Raspberry Pi para obter o valor correto e exibi-lo no terminal.


## __Parte 2: comunicação serial usando Tag RFID para controle de acessos em banco de dados__


Na segunda parte da prática, o foco foi implementar um sistema de controle de acesso utilizando a tecnologia de RFID (Radio Frequency Identification) em conjunto com a Raspberry Pi. Para isso, foi utilizado o módulo RFID-MFRC522, que opera via comunicação SPI (Serial Peripheral Interface). O objetivo era desenvolver um sistema que reconhecesse tags RFID e concedesse ou negasse acesso com base em informações previamente armazenadas.Nesse momento, a tag recebe energia do leitor e ambos iniciam a troca de informações. A comunicação SPI entre o módulo RFID e a Raspberry Pi foi estabelecida, sendo o SPI um protocolo de comunicação serial síncrona. Esse protocolo utiliza quatro linhas principais: MISO, MOSI, SCK e SS/CS, sendo que a Raspberry Pi atuou como dispositivo "controlador" e o módulo RFID como "controlado".
O desenvolvimento prático incluiu a escrita de um script em Python para controlar o sistema de acesso. Nele, as informações eram gravadas na tag RFID, permitindo ao sistema identificar a tag e verificar se ela estava cadastrada. Quando uma tag válida era detectada, o acesso era concedido (acionando um LED verde e exibindo a mensagem "acesso liberado" no terminal). Caso contrário, um LED vermelho era ativado e a mensagem "acesso negado" era exibida. Isso demonstrou o uso eficaz da comunicação SPI e da integração de um sistema de controle de acesso com RFID em sistemas embarcados.



Alunos: Beatriz Lomes da Silva - 12548038 Pedro Oliveira Torrente - 11798853