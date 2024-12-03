# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌾 Projeto de Sistema de Irrigação Inteligente - FarmTech Solutions

# Nome do projeto
Fase 4 - Cap 1 - Automação e Inteligência na FarmTech Solutions

## Nome do grupo
Grupo 44

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
Nesta fase do projeto FarmTech Solutions, o sistema de irrigação inteligente foi aprimorado para atingir um novo nível de eficiência e inteligência. O objetivo é monitorar as condições do solo em tempo real, prever a necessidade de irrigação e apresentar essas informações de forma clara e interativa. As principais melhorias incluem:
- Scikit-learn: para criar um modelo preditivo que sugere ações de irrigação.
- Streamlit: para desenvolver um dashboard interativo que mostra dados em tempo real.
- Banco de dados: aprimoramento da estrutura para permitir o armazenamento histórico dos dados dos sensores.
- Display LCD no Wokwi: para exibir as principais métricas em tempo real.
- Serial Plotter: para monitorar variáveis através de gráficos dinâmicos.
- Otimizações de memória: no código C/C++ do ESP32 para melhorar a eficiência do sistema.


## 📸 Imagens do Projeto
### Estrutura do Circuito 

<p align="center">
  <img src="assets/project4.png" alt="Estrutura do Circuito" border="0" width="50%" height="50%">
</p>

<p align="center">
  <strong>Figura 1:</strong> Estrutura do Circuito no Wokwi
</p>

### Simulação em Execução

<p align="center">
  <img src="assets/simulation4.png" alt="Simulação em Execução" border="0" width="50%" height="50%">
</p>

<p align="center">
  <strong>Figura 2:</strong> Simulação em Execução com Leitura dos Sensores
</p>

### Serial Plotter

<p align="center">
  <img src="assets/serialplotter4.png" alt="Serial Plotter" border="0" width="50%" height="50%">
</p>

<p align="center">
  <strong>Figura 3:</strong> Monitoriamento de Variáveis com Serial Plotter
</p>

### Bibliotecas do Projeto

<p align="center">
  <img src="assets/library4.png" alt="Bibliotecas do Projeto" border="0" width="50%" height="50%">
</p>

<p align="center">
  <strong>Figura 4:</strong> Bibliotecas do Projeto no Wokwi
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
### 💼 Pré-requisitos
Antes de iniciar, certifique-se de que você tem:

1. Simulador Wokwi configurado.
2. Python instalado, recomenda-se a versão 3.8 ou superior.
3. As bibliotecas necessárias: 'streamlit', 'scikit-learn' e 'mysql-connector-python'.
4. Banco de Dados MySQL configurado, localmente ou na nuvem, para armazenar os dados coletados.

### 🚀 Passo a Passo
**1. Executar a Simulação no Wokwi**
* Acesse o Wokwi.
* Importe o projeto utilizando o link disponível no arquivo 'link_projeto_wokwi.txt' localizado no repositório.
* Confira a conexão correta dos seguintes sensores:
  - DHT22: mede a umidade e a temperatura.
  - HC-SR04: mede a distância até um objeto, o que pode ser utilizado para monitorar o nível de um reservatório de água.
  - LDR: mede a intensidade da luz ambiente.
  - PIR: este sensor detecta movimento no ambiente, simulando um sistema de segurança.
* Inicie a simulação clicando no botão "Start Simulation".
  - O display LCD exibirá informações atualizadas sobre umidade e temperatura e status da irrigação. Se o valor de umidade estiver abaixo de um determinado limite (definido na variável 'IRRIGATION_THRESHOLD'), o status da irrigação é alterado para "SI" - Ativado. Caso contrário, o status permanece como "NA" - Desativado.
  - O Serial Plotter utilizado para monitorar as variáveis em tempo real, como a umidade e os níveis de luz.

**2. Executar o Dashboard com Streamlit**
* Baixe ou clone o repositório do projeto, onde está o código do dashboard.
* Abra o arquivo 'dashboard_streamlit.py' localizado na pasta 'src'.
* Execute o código no seu ambiente Python.
* O dashboard abrirá automaticamente no navegador ou exibirá um link para acesso.
* Explore as seguintes funcionalidades do dashboard:
  - Visualização de Dados em Tempo Real
  - Previsões do Modelo Preditivo
  - Insights de Desempenho

**3. Configurar e Usar o Banco de Dados**
* Configure o banco de dados SQL utilizando o script 'database_setup.sql' para criar as tabelas.
* Execute o código Python para inserir e consultar os dados dos sensores em tempo real.

### 🎥 Vídeo Demonstrativo 
O vídeo demonstrativo do projeto, está disponível no YouTube.
LINK

## 🗃 Histórico de lançamentos

* 0.1.0 - 03/12/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
