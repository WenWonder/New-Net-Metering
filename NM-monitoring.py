import streamlit as st
import pandas as pd

st.write('Net Metering Monitoring')

url = 'https://raw.githubusercontent.com/WenWonder/New-Net-Metering/refs/heads/main/sample.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))
