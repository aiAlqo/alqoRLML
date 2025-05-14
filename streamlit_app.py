import streamlit as st
import pandas as pd

st.title('🏉 RL Machine Learning App')

st.info('This is app builds a machine learning model')

df = pd.read_csv(r'C:\1 Coding Projects\Machine Learning\NRL\Dataset\nrldata_2017to21.csv')
df
