import streamlit as st
import pandas as pd

st.title('🏉 AFL ML Predictor App')

st.info('This app is a machine learning prediction model for AFL and NRL')

with st.expander('AFL Data'):
  st.write('**Raw Data 2012 to 2021**')
  afl_df = pd.read_csv('https://raw.githubusercontent.com/aiAlqo/alqoRLML/refs/heads/master/data/AFL2012to24.csv')
  afl_df
  #X = df.drop('HTWinner', axis=22, 'HTWinningMargin', axis=23, 'FTWinner', axis=24, 'FTWinningMargin', axis=25, 'TotalMatchPoints', axis=26, 'TotalMatchGoals', axis=27)
  st.write('**X**')
  X = df.drop('HTWinner', axis=2)
  X
  
  st.write('**y**')
  y = df.HTWinner
  y

"""
# Sample data
data = {
    'Item': ['Apples', 'Bananas', 'Cherries'],
    'Price per unit': [1.5, 0.8, 2.0],
    'Available Qty': [100, 200, 150]
}
df = pd.DataFrame(data)

st.title("Interactive Table Selector")

# Display table with checkboxes
st.subheader("Select items:")
selected_items = []

for i, row in df.iterrows():
    if st.checkbox(f"{row['Item']} (${row['Price per unit']}/unit)", key=row['Item']):
        qty = st.number_input(f"Enter quantity for {row['Item']} (max {row['Available Qty']}):", 
                              min_value=0, 
                              max_value=row['Available Qty'], 
                              key=f"qty_{row['Item']}")
        selected_items.append({
            'Item': row['Item'],
            'Unit Price': row['Price per unit'],
            'Quantity': qty,
            'Total': qty * row['Price per unit']
        })

# Show result
if selected_items:
    st.subheader("Your Selection Summary")
    result_df = pd.DataFrame(selected_items)
    st.dataframe(result_df)

    grand_total = result_df['Total'].sum()
    st.success(f"**Grand Total: ${grand_total:.2f}**")
else:
    st.info("Select at least one item to see calculations.")

# Guide preparations
with st.sidebar:
  st.header('Tipping Guide')
"""
