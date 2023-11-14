import streamlit as st
import pandas as pd
from bokeh.plotting import figure

st.title("SF Trees")
st.write("This app analyzes trees in San Francisco using a Dataset kindly provided by SF DPW")
st.subheader("Bokeh Chart")

trees_df = pd.read_csv("trees.csv")
scatterplot = figure(title="SF Trees")
scatterplot.scatter(x=trees_df['dbh'], y=trees_df['site_order'])
scatterplot.xaxis.axis_label = "DBH"
scatterplot.yaxis.axis_label = "Site Order"
st.bokeh_chart(scatterplot)