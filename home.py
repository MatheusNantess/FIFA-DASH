import pandas as pd
import streamlit as st
import datetime
#essa linha de código é necessária para carregar o estado da sessão em outros arquivos
if "key" not in st.session_state:
    # Read the dataframe from the CSV file
    df = pd.read_csv('CLEAN_FIFA23_official_data.csv', index_col=0)
    df = df[df['Contract Valid Until'] >=datetime.datetime.today().year]
    df = df[df['Value(£)'] > 0]
    df = df.sort_values(by='Overall', ascending=False)
    st.session_state["key"] = df

st.title('⚽FIFA23 OFFICIAL DATASET')
st.image('HD-wallpaper-all-new-features-in-fifa-23-fifa23.jpg', width=600)
st.write('The dataset contains +17k unique players and more than 60 columns, general information and all KPIs the famous videogame offers. As the esport scene keeps rising espacially on FIFA, I thought it can be useful for the community (kagglers and/or gamers)')

# Check if the dataframe is already stored in the session state

