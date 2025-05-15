import streamlit as st
import pandas as pd

st.title('🏉 RL Machine Learning App')

st.info('This is app builds a machine learning model')

with st.expander('NRL Data'):
  st.write('**Raw Data 2017 to 2021**')
  df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/nrldata_2017to21.csv')
  df
