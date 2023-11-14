import streamlit as st
import pandas as pd 
import plotly.express as px

st.title('SF Trees')
st.write(
    """This app analyzes trees in San Francisco using
    a Dataset kindly provided by SF DPW"""
)
st.subheader("Plotly Chart")
trees_df = pd.read_csv("trees.csv")
fig = px.histogram(trees_df, x="dbh")
st.plotly_chart(fig)
