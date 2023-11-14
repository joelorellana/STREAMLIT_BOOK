import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.title("Penguin Classifier")
st.write("This app uses 6 inputs to predict the species of penguin using"
        " a Random Forest Classifier.")

rf_pickle = open("penguin-rf-model.pkl", "rb")
map_pickle = open("penguin-output.pkl", "rb")
rfc = pickle.load(rf_pickle)
unique_penguin_map = pickle.load(map_pickle)
# st.write(rfc)
# st.write(unique_penguin_map)
rf_pickle.close()
map_pickle.close()


penguin_df = pd.read_csv("penguins.csv")
island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
sex = st.selectbox("Sex", options=["Female", "Male"])
bill_length_mm = st.number_input("Bill Length (mm)", min_value=0)
bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0)
flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0)
body_mass_g = st.number_input("Body Mass (g)", min_value=0)
user_input = [island, sex, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g]
st.write("User Input:", user_input)

island_biscoe, island_dream, island_torgerson = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgerson":
    island_torgerson = 1

sex_female, sex_male = 0, 0
if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = rfc.predict([[
    bill_length_mm,
    bill_depth_mm,
    flipper_length_mm,
    body_mass_g,
    island_biscoe,
    island_dream,
    island_torgerson,
    sex_female,
    sex_male
]])

prediction_species = unique_penguin_map[new_prediction][0]
st.write("The predicted species is:", prediction_species)
st.write("""
We use a Machine Learning (Random Forest) model
to predict the species of penguin.
The features used in this prediction are ranked by relative importance below.
""")
st.image("feature_importance.png")
st.write("""Below are the histograms for each continuous variable 
separated by penguin species. The vertical line represents your inputted value.
""")
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df.bill_length_mm, hue=penguin_df.species)
plt.axvline(x=bill_length_mm)
plt.title("Bill Length by Species")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df.bill_depth_mm, hue=penguin_df.species)
plt.axvline(x=bill_depth_mm)
plt.title("Bill Depth by Species")
st.pyplot(ax)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df.flipper_length_mm, hue=penguin_df.species)
plt.axvline(x=flipper_length_mm)
plt.title("Flipper Length by Species")
st.pyplot(ax)
