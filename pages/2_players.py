import pandas as pd
import streamlit as st

st.set_page_config(
    layout="wide"
)
df = st.session_state["key"] 

#lista de times
lista_clubes = df["Club"].unique()
#clube selecionado, vai ser usado para achar os jogadores de cada clube
clube_selecionado = st.sidebar.selectbox("Selecione um clube", lista_clubes)

#pra achar as linhas de jogadores aonde tem a string retornada na coluna club
lista_jogadores = df[df["Club"] == clube_selecionado]["Name"].unique()
jogador_selecionado = st.sidebar.selectbox("Selecione um jogador", lista_jogadores)

player_stats = df.loc[df["Name"] == jogador_selecionado].iloc[0]
st.image(player_stats["Photo"])
st.title(jogador_selecionado)
#a necessidade de usar o iloc é justamente pelo fato de que quando se usa loc, é retornado uma series e quando vc usa iloc é retornado a primeira linha da series que é o que eu quero
st.markdown(f"**Clube:** {player_stats["Club"]}")
#a necessidade de usar o iloc é justamente pelo fato de que quando se usa loc, é retornado uma series e quando vc usa iloc é retornado a primeira linha da series que é o que eu quero
st.markdown(f"**Posição:** {player_stats["Position"]}")

col1, col2, col3, = st.columns(3)

col1.markdown(f"**Idade:** {player_stats["Age"]}")

col2.markdown(f"**Altura (cm):** {player_stats["Height(cm.)"]}")

col3.markdown(f"**Peso (lbs)** {player_stats["Weight(lbs.)"]}")

st.divider()

st.subheader(f"**Overall:** {player_stats["Overall"]}")

st.progress(
    int(player_stats["Overall"]
))

col4, col5, col6 = st.columns(3)

jogador_salario = df.loc[df["Name"] == jogador_selecionado,"Value(£)"].iloc[0]
col4.metric("Valor de mercado", f"£ {jogador_salario:,}")

col5.metric("Remuneração Semanal", f"£ {player_stats["Wage(£)"]:,}")

col6.metric("Cláusula de Recisão", f"£ {player_stats["Release Clause(£)"]:,}")
