import streamlit as st
import pickle
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