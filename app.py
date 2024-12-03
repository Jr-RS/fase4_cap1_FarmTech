import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from joblib import dump
from joblib import load
import numpy as np

# para executar o painel execute: streamlit run app.py

# Função para carregar os dados
@st.cache_data

def carregar_dados():
    return pd.read_csv('src/base_preparada.csv', sep=';')

figsize = (15, 8)

# Carregar os dados
base = carregar_dados()

# Configurar a interface
st.title("Dashboard do Sistema de Irrigação")
#st.sidebar.title("Opções do Dashboard")


# Gráficos interativos

# Melhores Dias para Irrigação
st.write("")
st.subheader("Gráfico: Melhores Dias para Irrigação")
st.write(
    "Este gráfico mostra a **taxa média de irrigação por dia da semana**. "
    "A taxa é calculada como a proporção de vezes em que a irrigação foi ativada para cada dia. "
    "Utilize este gráfico para identificar os dias mais e menos frequentes para irrigação, "
    "ajudando a planejar intervenções sustentáveis e otimizadas."
)

dia_irrigacao = base.groupby('dia')['irrigacao'].mean().reset_index()
dia_map = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
dia_irrigacao['dia'] = dia_irrigacao['dia'].map(dia_map)

fig, ax = plt.subplots(figsize=figsize)
sns.barplot(data=dia_irrigacao, x='dia', y='irrigacao', ax=ax)
ax.set_title("Taxa de Irrigação por Dia da Semana")
ax.set_ylabel("Taxa de Irrigação")
ax.set_xlabel("Dia da Semana")
st.pyplot(fig)


# Melhores Horários para Irrigação
st.write("---------------------------------------------------------")
st.write("")
st.subheader("Gráfico: Melhores Horários para Irrigação")
st.write(
    "Este gráfico apresenta a **taxa média de irrigação ao longo do dia**, com base nos horários em que a irrigação foi ativada. "
    "Você pode filtrar por um ou mais dias da semana e também visualizar a **média geral** para comparação."
)

dia_map = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
base['dia_nome'] = base['dia'].map(dia_map)
hora_dia_irrigacao = base.groupby(['hora', 'dia_nome'])['irrigacao'].mean().reset_index()
media_geral = base.groupby('hora')['irrigacao'].mean().reset_index()
media_geral['dia_nome'] = 'Média Geral'
hora_dia_irrigacao = pd.concat([hora_dia_irrigacao, media_geral], ignore_index=True)

dias_selecionados = st.multiselect(
    "Selecione os dias da semana para visualizar:",
    options=list(dia_map.values()) + ['Média Geral'],  # Incluindo a média geral como opção
    default=['Média Geral']  # Exibir apenas a média geral por padrão
)
dados_filtrados = hora_dia_irrigacao[hora_dia_irrigacao['dia_nome'].isin(dias_selecionados)]

fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=dados_filtrados, x='hora', y='irrigacao', hue='dia_nome', marker="o", ax=ax, palette="tab10")
ax.set_title("Taxa de Irrigação por Horário e Dia da Semana")
ax.set_ylabel("Taxa Média de Irrigação")
ax.set_xlabel("Hora do Dia")
ax.legend(title="Dia da Semana", loc='upper right')
st.pyplot(fig)


# Gráfico: Umidade ao Longo do Dia e Horário
st.write("---------------------------------------------------------")
st.write("")
st.subheader("Gráfico: Umidade ao Longo do Dia e Horário")
st.write(
    "Este gráfico apresenta um **mapa de calor**, que mostra a variação média da umidade ao longo do dia (por hora) e da semana. "
    "Os valores mais claros indicam baixa umidade, enquanto os mais escuros representam alta umidade. "
    "Use este gráfico para identificar períodos críticos em que a umidade está baixa e pode ser necessário ativar a irrigação."
)

dia_map = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
base['dia_nome'] = base['dia'].map(dia_map)
heatmap_data = base.pivot_table(index="dia_nome", columns="hora", values="umidade", aggfunc="mean")

fig, ax = plt.subplots(figsize=figsize)
sns.heatmap(heatmap_data, cmap="Blues", ax=ax, annot=True, fmt=".1f", linewidths=.5, cbar_kws={'label': 'Umidade Média'})
ax.set_title("Mapa de Calor: Umidade por Dia e Hora", fontsize=14)
ax.set_ylabel("Dia da Semana")
ax.set_xlabel("Hora do Dia")
st.pyplot(fig)


# Área de Inferência Preditiva
st.write("---------------------------------------------------------")
st.write("")
st.subheader("Análise Preditiva: Ativar Irrigação?")
st.write(
    """
    Nesta seção, você pode realizar uma **análise preditiva** para saber se a irrigação deve ser ativada com base em 
    condições específicas fornecidas por você. O modelo de Machine Learning foi treinado para analisar os seguintes fatores:
    
    - **Umidade (%):** Indica a umidade do ar ou do solo no momento da análise.
    - **Nutrientes:** Representa os níveis de nutrientes presentes no solo, com base em medições realizadas.
    - **Hora do Dia:** Refere-se ao horário em que os dados foram coletados, variando entre 0 (meia-noite) e 23 (23 horas).
    - **Dia da Semana:** Representa o dia em que os dados foram coletados, como Domingo, Segunda, etc.

    Preencha os valores abaixo e clique no botão **Prever** para obter a recomendação do sistema.
    """
)

# Carregar o modelo salvo
modelo = load('src/modelo.pkl')

# Entradas do usuário
umidade_input = st.number_input("Umidade (%)", min_value=0.0, max_value=100.0, value=50.0)
nutrientes_input = st.number_input("Nutrientes", min_value=0.0, max_value=100.0, value=20.0)
hora_input = st.slider("Hora do Dia", min_value=0, max_value=23, value=12)
dia_map = {0: 'Domingo', 1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado'}
dia_input = st.selectbox("Dia da Semana", list(dia_map.values()))
dia_input_num = {v: k for k, v in dia_map.items()}[dia_input]

if st.button("Prever"):
    nova_amostra = np.array([[umidade_input, nutrientes_input, hora_input, dia_input_num]])
    predicao = modelo.predict(nova_amostra)

    if predicao[0] == 1:
        st.success(
            """
            **Recomendação: Ativar a Irrigação!**
            O modelo analisou os dados fornecidos e determinou que a irrigação deve ser ativada 
            para manter as condições ideais no solo.
            """
        )
    else:
        st.info(
            """
            **Recomendação: Não é necessário ativar a irrigação agora.**
            O modelo concluiu que, com base nas condições atuais, a irrigação não é necessária.
            """
        )