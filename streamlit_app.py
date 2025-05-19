import streamlit as st
import pandas as pd

st.title('🏉 AFL ML Predictor App')

st.info('This app is a machine learning prediction model for AFL and NRL')

with st.expander('AFL Data'):
  st.write('**Raw Data 2012 to 2021**')
  afl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/AFL2012to24_2.csv')
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
teams = ['Adelaide Crows', 'Brisbane Lions', 'Carlton', 'Collingwood', 'Essendon','Fremantle', 'Geelong Cats', 'Gold Coast Suns', 'GWS Giants', 'Hawthorn','Melbourne', 'North Melbourne', 'Port Adelaide', 'Richmond', 'St Kilda','Sydney Swans', 'West Coast Eagles', 'Western Bulldogs']

with st.sidebar.header('Input Features'):

  home_team = st.sidebar.selectbox("Select Home Team", teams, key='home_team')
  away_team = st.sidebar.selectbox("Select Away Team", teams, key='away_team')

# Optional: Check to avoid selecting the same team
  if home_team == away_team:
      st.sidebar.warning("Home and Away teams must be different.")

# Show selections
  st.write(f"**Home Team:** {home_team}")
  st.write(f"**Away Team:** {away_team}")



