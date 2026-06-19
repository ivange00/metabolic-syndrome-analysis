# %%
import joblib
import pandas as pd
import streamlit as st

# %%

model = joblib.load("model.pkl")

# %%
st.title("Metabolic Syndrome Predictor")

st.write(
    "Estimate the probability of metabolic syndrome "
    "based on age, sex, alcohol consumption and smoking status."
)

gender = st.selectbox(
    "Gender",
    ["F", "M"]
)

age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=40
)

alcohol = st.selectbox(
    "Alcohol status",
    ["Non-drinker", "Drinker"]
)

smoking = st.selectbox(
    "Smoking status",
    ["Non-smoker", "Former smoker", "Current smoker"]
)

# %%
def predict_metabolic_syndrome(model, gender, age, alcohol, smoking):

    new_patient = pd.DataFrame({
        "Gender": [gender],
        "Age": [round((age/5) + 0.5)],
        "Alcohol_status": [alcohol],
        "Smoking_status": [smoking]
    })

    probability = model.predict(new_patient).iloc[0]

    return probability

# %%
if st.button("Predict probability"):

    p = predict_metabolic_syndrome(
        model,
        gender,
        age,
        alcohol,
        smoking
    )

    st.metric(
        label="Metabolic syndrome probability",
        value=f"{100*p:.2f}%"
    )


