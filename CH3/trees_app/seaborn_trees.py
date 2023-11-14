import streamlit as st # import streamlit
import pandas as pd # import pandas
import seaborn as sns # import seaborn
import matplotlib.pyplot as plt # import matplotlib
import datetime as dt # import datetime

st.title("SF Trees")
st.write("This app analyzes trees in San Francisco using a Dataset kindly provided by SF DPW")
trees_df = pd.read_csv("trees.csv")
trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots() # create a figure
ax_sb = sns.histplot(trees_df.age) # create a histogram
plt.xlabel('Age (days)')
st.pyplot(fig_sb)
st.subheader("Matplotlib Chart")
fig_mpl, ax_mpl = plt.subplots() # create a figure
ax_mpl = plt.hist(trees_df.age) # create a histogram
plt.xlabel('Age (days)')
st.pyplot(fig_mpl)