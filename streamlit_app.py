import streamlit as st
import pandas as pd

st.title('🏉 AFL ML Predictor App')

st.info('This app is a machine learning prediction model for AFL and NRL')

with st.expander('AFL Data'):
  st.write('**Raw Data 2012 to 2021**')
  afl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/AFL2012to24_1.csv')
  afl_df
  #X = df.drop('HTWinner', axis=22, 'HTWinningMargin', axis=23, 'FTWinner', axis=24, 'FTWinningMargin', axis=25, 'TotalMatchPoints', axis=26, 'TotalMatchGoals', axis=27)
  cols_to_drop = ['HTWinner', 'HTWinningMargin', 'FTWinner', 'FTWinningMargin', 'TotalMatchPoints', 'TotalMatchGoals']
  
  st.write('**X**')
  X = afl_df.drop(cols_to_drop, axis=1)
  st.dataframe(X)
  
  st.write('**y**')
  y = afl_df[cols_to_drop]
  st.dataframe(y)

#Data preparations
with st.sidebar:
  st.header('Input Features')
  "Input match details below:"
  HomeTeam = st.selectbox('Home Team', ('Greater Western Sydney','Richmond','Hawthorn','Melbourne','Gold Coast','Fremantle','North Melbourne','Western Bulldogs','Port Adelaide','Brisbane Lions','Essendon','Sydney','West Coast','Adelaide','Collingwood','St Kilda','Geelong','Carlton'))
  AwayTeam = st.selectbox('Away Team', ('Greater Western Sydney','Richmond','Hawthorn','Melbourne','Gold Coast','Fremantle','North Melbourne','Western Bulldogs','Port Adelaide','Brisbane Lions','Essendon','Sydney','West Coast','Adelaide','Collingwood','St Kilda','Geelong','Carlton'))

