# Análise de Dados de Jogos

Este é um projeto de análise de dados de jogos, que utiliza a biblioteca Streamlit para criar uma interface interativa para visualização e análise dos dados. A aplicação permite explorar informações sobre editoras, plataformas, jogos e vendas de videogames.

## Funcionalidades

- Visualização das 5 editoras de videogame mais populares;
- Visualização das 10 plataformas de games mais populares;
- Visualização do TOP 20 jogos mais populares em diferentes regiões;
- Seleção de um jogo para exibir as vendas em cada mercado;
- Seleção de um mercado para exibir os 5 gêneros mais populares e um exemplo de jogo de cada gênero;
- Seleção de um ano para obter a quantidade de jogos lançados e o jogo mais popular daquele ano.

## Pré-requisitos

- Python 3.x
- Bibliotecas: Streamlit, Numpy, Pandas, Matplotlib.pyplot e Seaborn

## Como executar o projeto

1. Clone este repositório:

git clone https://github.com/devrodrigocsoares/DataGamesStreamlit.git


2. Instale as dependências:

pip3 install numpy pandas matplotlib seaborn streamlit


3. Execute o aplicativo Streamlit:

streamlit run appGames.py

O aplicativo estará disponível em `http://localhost:8501`.

## Estrutura do projeto

- `AppGames.py`: Contém o código principal da aplicação em Streamlit.
- `vgsales.csv`: Arquivo CSV contendo os dados dos jogos.
