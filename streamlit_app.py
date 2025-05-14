import streamlit as st
import pandas as pd

st.title('🏉 RL Machine Learning App')

st.info('This is app builds a machine learning model')

df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/nrldata_2017to21.csv')
df
