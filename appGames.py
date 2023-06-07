import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Análise exploratória de dados de videogames e Jogos')

data = pd.read_csv('vgsales.csv');

data = data.dropna()

st.write(data)

st.subheader("Quais as 05 empresas editoras (publishers) de videogame são as mais populares? Represente usando gráfico.")

publishers_count = data['Publisher'].value_counts().head(5)

fig, ax = plt.subplots()
ax.bar(publishers_count.index, publishers_count.values)
ax.set_xlabel('Editora')
ax.set_ylabel('Número de Jogos')
ax.set_title('As 5 Empresas Editoras de Videogame Mais Populares')

plt.xticks(fontsize=5)

st.pyplot(fig)

st.subheader("Quais as 10 plataformas de videogame mais populares? Represente usando gráfico.")

platforms_count = data['Platform'].value_counts().head(10)

fig, ax = plt.subplots()
ax.bar(platforms_count.index, platforms_count.values)
ax.set_xlabel('Plataforma')
ax.set_ylabel('Número de Jogos')
ax.set_title('As 10 Plataformas Mais Populares de Jogos')

st.pyplot(fig)

st.subheader("Mostre o TOP 20 jogos mais populares conforme a seleção informada pelo usuário. O usuário poderá escolher entre as opções: “América do Norte”, ”União Europeia”; “Japão”, “Resto do mundo”, “Global”.")

region = st.selectbox('Selecione uma região:', ['América do Norte', 'União Europeia', 'Japão', 'Resto do Mundo', 'Global'])

region_columns = {
    'América do Norte': 'NA_Sales',
    'União Europeia': 'EU_Sales',
    'Japão': 'JP_Sales',
    'Resto do Mundo': 'Other_Sales',
    'Global': 'Global_Sales'
}

if region != 'Global':
    filtered_data = data.nlargest(20, region_columns[region])
else:
    filtered_data = data.nlargest(20, 'Global_Sales')

fig, ax = plt.subplots()
ax.barh(filtered_data['Name'], filtered_data[region_columns[region]])
ax.set_xlabel('Vendas')
ax.set_ylabel('Jogo')
ax.set_title(f'Top 20 Jogos Mais Populares - {region}')

ax.invert_yaxis()

st.pyplot(fig)

st.subheader("Crie uma visualização que permita o usuário escolher um jogo da lista e, em seguida, mostre um gráfico com o total de vendas em cada um dos mercados citados na questão anterior.")

unique_games = data['Name'].unique()

selected_game = st.selectbox('Selecione um jogo:', unique_games)

game_data = data[data['Name'] == selected_game]

sales_columns = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

sales_values = game_data[sales_columns].values.flatten()

fig, ax = plt.subplots()
ax.bar(sales_columns, sales_values)
ax.set_xlabel('Mercado')
ax.set_ylabel('Vendas')
ax.set_title(f'Total de Vendas por Mercado - {selected_game}')

st.pyplot(fig)

st.subheader("Top 05 gêneros de cada mercado: crie um filtro que permita ao usuário escolher um mercado (conforme a questão 3) e mostre o TOP 05 gêneros mais populares daquele mercado. Para cada gênero, mostre, ao lado, um exemplo de jogo daquele gênero.")

market = st.selectbox('Selecione um mercado:', ['América do Norte', 'União Europeia', 'Japão', 'Resto do Mundo', 'Global'])

market_columns = {
    'América do Norte': 'NA_Sales',
    'União Europeia': 'EU_Sales',
    'Japão': 'JP_Sales',
    'Resto do Mundo': 'Other_Sales',
    'Global': 'Global_Sales'
}

market_data = data.copy()
market_data = market_data[['Genre', 'Name', market_columns[market]]].groupby(['Genre', 'Name']).sum().reset_index()

top_5_genres = market_data.groupby('Genre')[market_columns[market]].sum().nlargest(5).index.tolist()

table_data = []
for genre in top_5_genres:
    games = market_data[market_data['Genre'] == genre]['Name'].tolist()
    example_game = games[0] if games else ''
    table_data.append((genre, example_game))

st.table(pd.DataFrame(table_data, columns=['Gênero', 'Exemplo de Jogo']))

st.subheader("Escolher um ano e mostrar quantos jogos foram lançados naquele ano e qual o mais popular.")

years = sorted(data['Year'].unique())

year = st.selectbox('Selecione um ano:', years)

filtered_data = data[data['Year'] == year]

num_games = len(filtered_data)

most_popular_game = filtered_data[filtered_data['Global_Sales'] == filtered_data['Global_Sales'].max()]['Name'].iloc[0]

st.write(f"Em {year} foram lançados {num_games} jogos.")
st.write(f"Jogo mais popular de {year} foi {most_popular_game} .")


