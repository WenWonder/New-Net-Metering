import streamlit as st
import pandas as pd

st.write('Net Metering Monitoring')

url_data = 'https://raw.githubusercontent.com/WenWonder/New-Net-Metering/refs/heads/main/sample.csv'
data_csv = pd.read_csv(url_data)
data_csv.head()

st.write(url_data)
