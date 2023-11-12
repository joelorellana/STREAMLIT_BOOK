import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import time 

st.title("Palmer's Penguins")
# import data
st.markdown('Use this streamlit app to make your own scatterplot about penguins!')
# selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Chinstrap', 'Gentoo'])
penguin_file = st.file_uploader("Upload your penguin data", type=["csv"])
@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        penguins_df = pd.read_csv(penguin_file)
    else:
        penguins_df = pd.read_csv("penguins.csv")
    return penguins_df
    
# if penguin_file is not None:
#     penguins_df = pd.read_csv(penguin_file)
# else:
#     # penguins_df = pd.read_csv("penguins.csv")
#     st.warning("Please upload your penguin data")
#     st.stop()

penguins_df = load_file(penguin_file)

sns.set_style("darkgrid")
markers = {"Adelie": "X", "Chinstrap": "s", "Gentoo": "o"}

selected_x_var = st.selectbox('X axis variable', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('Y axis variable', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender would you like to visualize?', ['both', 'male', 'female'])
if selected_gender == 'male':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass
# st.write(penguins_df.head())
# penguins_df = penguins_df[penguins_df['species'] == selected_species]
alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color="species",
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)
