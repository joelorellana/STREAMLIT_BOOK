import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


st.title("Penguin Classifier")
st.write("This app uses 6 inputs to predict the species of penguin using"
    " a Random Forest Classifier.")

penguin_file = st.file_uploader("Upload your own penguin data")

if penguin_file is None:
    rf_pickle = open("penguin-rf-model.pkl", "rb")
    map_pickle = open("penguin-output.pkl", "rb")
    rfc = pickle.load(rf_pickle)
    unique_penguin_map = pickle.load(map_pickle)
    rf_pickle.close()
    map_pickle.close()
else:
    penguin_df = pd.read_csv(penguin_file)
    penguin_df.dropna(inplace=True)
    output = penguin_df["species"]
    features = penguin_df[["island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]]
    features = pd.get_dummies(features)
    output, uniques = pd.factorize(output)
    x_train, x_test, y_train, y_test = train_test_split(features, output, train_size=0.8)
    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train.values, y_train)
    y_pred = rfc.predict(x_test.values)
    score = round(accuracy_score(y_pred, y_test),2)
    st.write(f"Here is our accuracy score: {score}")


with st.form('user_inputs'):
    island = st.selectbox("Penguin Island", options=["Biscoe", "Dream", "Torgerson"])
    sex = st.selectbox("Sex", options=["Female", "Male"])
    bill_length_mm = st.number_input("Bill Length (mm)", min_value=0)
    bill_depth_mm = st.number_input("Bill Depth (mm)", min_value=0)
    flipper_length_mm = st.number_input("Flipper Length (mm)", min_value=0)
    body_mass_g = st.number_input("Body Mass (g)", min_value=0)
    st.form_submit_button()

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

new_prediction = rfc.predict(
    [
        [
            bill_length_mm,
            bill_depth_mm,
            flipper_length_mm,
            body_mass_g,
            island_biscoe,
            island_dream,
            island_torgerson,
            sex_female,
            sex_male
        ]
    ]
)
prediction_species = unique_penguin_map[new_prediction][0]
st.write("The predicted species is:", prediction_species)
