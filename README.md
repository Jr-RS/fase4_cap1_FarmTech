# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌾 Projeto de Monitoramento Agrícola - FarmTech Solutions

# Nome do projeto
Fase 3 - Cap 12 - A Eletrônica de uma IA

## Nome do grupo
Grupo 10

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/">Ana Beatriz Duarte Domingues</a>
- <a href="https://www.linkedin.com/in/jrsilva051/">Junior Rodrigues da Silva</a>
- <a href="https://www.linkedin.com/in/">Carlos Emilio Castillo Estrada</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi Chiovato</a>


## 📜 Descrição

O sistema utiliza quatro sensores conectados ao microcontrolador ESP32:

* DHT22: Sensor de temperatura e umidade.
* HC-SR04: Sensor ultrassônico para medir a distância (simulando um possível monitoramento de nível de água).
* PIR: Sensor de movimento para detectar presença.
* LDR: Sensor de luminosidade (simulando níveis de pH, onde variações de luz são interpretadas como alterações de pH).

Os dados coletados são exibidos no console e, no futuro, podem ser integrados com um banco de dados para armazenar e consultar informações históricas, além de integrar um sistema de irrigação.

<p align="center">
<img src="assets/project.png" alt="Estrutura do projeto" border="0" width=40% height=40%></a>
<img src="assets/screen1.png" alt="Estrutura do projeto" border="0" width=40% height=40%></a>
<img src="assets/simulation.png" alt="Estrutura do projeto" border="0" width=40% height=40%></a>
<img src="assets/library.png" alt="Estrutura do projeto" border="0" width=40% height=40%></a>
</p>


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).


## 🔧 Como executar o código

Você tem 2 opções para executar o projeto, importando o arquivo 'Fase3_Cap12_A_Eletronica_de_uma_IA' da pasta scr/ e seguindo os pasos abaixo

* 1 Acesse a plataforma Wokwi, crie um projeto e selecione o microcontrolador ESP32.
* 2 Conecte os sensores conforme a imagem do diagrama na sesão 'Descrição'.
* 3 Copie e cole o código do arquivo 'sketch.ino' editor de código da Wokwi.
* 4 Instale as dependencias.
* 5 Para iniciar a simulação, clique no botão de "Play" (executar).
* 6 O monitor serial mostrará os valores dos sensores em intervalos de 2 segundos.

ou, acessando o link disponibilizado no arquivo 'link_projeto_wokwi'.

### 💼 Pré-requisitos

Para que o código funcione corretamente, certifique-se de instalar a biblioteca DHT sensor library. No Wokwi, essa biblioteca geralmente já está incluída. No entanto, se você estiver executando o código em uma IDE como o Arduino IDE, será necessário instalar a biblioteca seguindo as etapas abaixo:

* 1 Abra a Arduino IDE.
* 2 Vá para Sketch > Include Library > Manage Libraries...
* 3 Procure por "DHT sensor library" de Adafruit e instale a versão mais recente.

### 🚀 Funcionalidades

O projeto inclui as seguintes funcionalidades:

* Leitura de Temperatura e Umidade:

* Utilizando o sensor DHT22, o sistema coleta dados de temperatura e umidade.
Esses valores são exibidos no console.
Medida de Distância:

* O sensor HC-SR04 mede a distância até um objeto, o que pode ser utilizado para monitorar o nível de um reservatório de água.
A distância é calculada com base no tempo de resposta do sensor e exibida no console.
Detecção de Movimento:

* O sensor PIR detecta movimento no ambiente, simulando um sistema de segurança.
O console exibe uma mensagem indicando se há ou não movimento detectado.
Leitura de Intensidade de Luz (LDR):

* O sensor LDR mede a intensidade da luz ambiente, representando variações como se fossem dados de pH.
A leitura do LDR é mostrada no console, simulando o nível de pH com base na luz.
Console com Dados:

Todos os dados são apresentados no console, com uma atualização a cada 2 segundos para facilitar a visualização em tempo real.


## 🗃 Histórico de lançamentos

* 0.1.0 - 26/10/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>