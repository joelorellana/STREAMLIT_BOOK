import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
st.title("SF Trees")
st.write("""
    This app analyses trees in San Francisco using a dataset kindly 
    provided by SF DPW
""")
# first_width = st.number_input('First Width', min_value=1, value=1)
# second_width = st.number_input('Second Width', min_value=1, value=1)
# third_width = st.number_input('Third Width', min_value=1, value=1)

trees_df = pd.read_csv("./pretty_trees/trees.csv")
df_dbh_grouped = pd.DataFrame(trees_df.groupby("dbh").count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])

with tab1:
    st.line_chart(df_dbh_grouped)
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)
