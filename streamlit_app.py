import streamlit as st
import pandas as pd

st.title('🏉 RL Machine Learning App')

st.info('This is app builds a machine learning model')

with st.expander('NRL Data'):
  st.write('**Raw Data 2017 to 2021**')
  nrl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/nrldata_2017to21.csv')
  nrl_df

with st.expander('AFL Data'):
  st.write('**Raw Data 2012 to 2021**')
  afl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/AFL2012to24.csv')
  afl_df

# Guide preparations
with st.sidebar:
  st.header('Tipping Guide')

  with st.expander('NRL'):
    st.write('**Round 12**')
    nrl_guide = pd.rea_excel('https://view.officeapps.live.com/op/view.aspx?src=https%3A%2F%2Fraw.githubusercontent.com%2FaiAlqo%2FalqoRLML%2Frefs%2Fheads%2Fmaster%2Fdata%2FNRL1.xlsx&wdOrigin=BROWSELINK')
    nrl_guide
