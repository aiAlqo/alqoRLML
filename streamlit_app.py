import streamlit as st
import pandas as pd
import datetime

st.title('🏉 AFL ML Predictor App')

st.info('This app is a machine learning prediction model for AFL and NRL')

with st.expander('AFL Data'):
  st.write('**Raw Data 2012 to 2021**')
  afl_df = pd.read_csv('https://https://raw.githubusercontent.com/aiAlqo/alqoRLML/master/data/AFL2012to24_2.csv')
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
weather_conditions =["Fine/Clear","Fair/Partly Cloudy","Cloudy/Overcast","Showery/Scattered Rain","Rainy/Wet","Windy/Breezy","Stormy","Severe"]

with st.sidebar:
  st.header('Input Features')
  st.markdown('**Fill out details of match for this ML model to run you prediction**')

  d = st.date_input("Date of Match", value=datetime.date.today())
  t = st.time_input("Time of Match", value=datetime.time(13, 0))
  
  home_team = st.sidebar.selectbox("Select Home Team", teams, key='home_team')
  away_team = st.sidebar.selectbox("Select Away Team", teams, key='away_team')
  
# Optional: Check to avoid selecting the same team
  if home_team == away_team:
      st.sidebar.warning("⚠️Home and Away teams must be different.")

  temp_range = st.slider("🌡️ Forecasted Temperature Range (°C)", -10.0, 38.0, (7.6, 16.0), step=0.1)
  weather_forecast = st.select_slider("🌤️ Forecasted Weather Condition", options=weather_conditions)

# Show selections
  st.subheader("Confirm below your selected Match details")
  st.write(f"**Match Date:** {d}")
  st.write(f"**Match Time:** {t}")
  st.write(f"**Home Team:** {home_team}")
  st.write(f"**Away Team:** {away_team}")
  st.write(f"**Forecasted Temp range:** {temp_range[0]}°C to {temp_range[1]}°C")
  st.write(f"**Forecasted Weather:** {weather_forecast}")

  
