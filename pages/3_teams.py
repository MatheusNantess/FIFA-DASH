import streamlit as st
import pandas as pd

df = st.session_state["key"]

lista_clubes = df["Club"].unique()
clube_selecionado = st.sidebar.selectbox("Clube", lista_clubes)
st.image(df.loc[df["Club"] == clube_selecionado, "Club Logo"].iloc[0], width=50)

st.title(df.loc[df["Club"] == clube_selecionado, "Club"].iloc[0])
df = df.set_index("Name")



st.dataframe(df.loc[df["Club"] == clube_selecionado, :], column_config={
    "Value(£)": st.column_config.NumberColumn(
        'Value(£)',
        min_value=0,
        max_value=df["Value(£)"].max(),
        format="£%f"
    ),
    "Wage(£)": st.column_config.ProgressColumn(
        "Weekly Wage", 
        min_value=0,
        max_value = df["Wage(£)"].max(),
        format="£%f"
    ),
    "Photo": st.column_config.ImageColumn(
        "Photo"
    ),
    "Flag": st.column_config.ImageColumn(
        "Flag"
    ),
    "Overall": st.column_config.ProgressColumn(
        "Overall",
        min_value= 0,
        max_value= 100,
        format= "%d"
    ),
    "Club Logo": st.column_config.ImageColumn()

})





