import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
st.sidebar.header("Welcome streamlit web view")
st.header("dengan saya dani")
dataMinyak = pd.read_csv('produksi_minyak_mentah.csv')
country = pd.read_json('kode_negara_lengkap.json')
mergeResult = pd.merge(left=country, right=dataMinyak, left_on='alpha-3', right_on='kode_negara')
data = dataHasil=mergeResult[['name','tahun','produksi','alpha-3','country-code','iso_3166-2','region','sub-region','intermediate-region','region-code','sub-region-code']]
dataset = data.rename({'name': 'Negara','produksi':'Jumlah Produksi' ,'tahun': 'Tahun','alpha-3':'Alias Negara','country-code':'Kode Negara','region':'Wilayah','sub-region':'Wilayah Bagian'}, axis='columns')

if st.checkbox("Lihat data"):
  st.write(dataset)
