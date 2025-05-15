import streamlit as st
import pandas as pd

st.title('🏉 RL Machine Learning App')

st.info('This is app builds a machine learning model')

with st.expander('NRL Data'):
  st.write('**Raw Data 2017 to 2021**')
  nrl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/nrldata_2017to21.csv')
  nrl_df

afl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/AFL2012to24.csv')
afl_df
