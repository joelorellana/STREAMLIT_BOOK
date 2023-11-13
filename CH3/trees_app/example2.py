import numpy as np
import streamlit as st
import pandas as pd

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
    a Dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby(["dbh"]).count()["tree_id"]).reset_index()
df_dbh_grouped.columns = ["dbh", "tree_count"]
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")

# Map Graph
trees_df = trees_df.dropna(subset=["latitude", "longitude"])
trees_df = trees_df.sample(n=1000) # limit to 1000 points
st.map(trees_df)