import streamlit as st
import pandas as pd
import numpy as np

st.title("SF Trees")
st.write("This app analyzes trees in San Francisco using a Dataset kindly provided by SF DPW")
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())

# STREAMLIT BUILT-IN GRAPHING FUNCTIONS
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

# CREATING A NEW COLUMN AND PLOTTING
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped))*500
st.line_chart(df_dbh_grouped)


