import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
st.sidebar.header("Welcome streamlit web view")
st.header("dengan saya dani")
dataMinyak = pd.read_csv('produksi_minyak_mentah.csv')
if st.checkbox("Lihat data"):
  st.write(dataMinyak)
