import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

penguin_df = pd.read_csv("penguins.csv")
# print(penguin_df.head())
penguin_df.dropna(inplace=True)

output = penguin_df["species"]
features = penguin_df[["island", "bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "sex"]]
features = pd.get_dummies(features)
# print("Here are our output values:")
# print(output.head())
# print("Here are our features:")
# print(features.head())

output, uniques = pd.factorize(output) # transforms output into numbers
x_train, x_test, y_train, y_test = train_test_split(features, output, train_size=0.8, random_state=1)
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train.values, y_train)
y_pred = rfc.predict(x_test.values)
score = accuracy_score(y_pred, y_test)
print(f"Here is our accuracy score: {round(score*100, 2)}%")
# SAVE THE MODEL
rf_model = open("penguin-rf-model.pkl", "wb")
pickle.dump(rfc, rf_model)
rf_model.close()
output_pickle = open("penguin-output.pkl", "wb")
pickle.dump(uniques, output_pickle)
output_pickle.close()
fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
plt.title("Which features are most important?")
plt.xlabel("Feature Importance")
plt.ylabel("Features")
plt.tight_layout()
fig.savefig("feature_importance.png")