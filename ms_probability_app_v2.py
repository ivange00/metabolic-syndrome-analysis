# %%
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# %%

model = joblib.load("model.pkl")

# %%
alc_smo_df = pd.read_csv("smoking_df_english.csv", sep=';')

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
class Subject:

    def __init__(self, gender, age, alcohol, smoking):

        self.gender = gender
        self.age = age
        self.alcohol = alcohol
        self.smoking = smoking

        self.probability = None

    def predict(self, model):

        df = pd.DataFrame({
            "Gender": [self.gender],
            "Real_age": [self.age],
            "Alcohol_status": [self.alcohol],
            "Smoking_status": [self.smoking]
        })

        self.probability = model.predict(df).iloc[0]

        return self.probability

# %%
subject = Subject(gender, age, alcohol, smoking)

if st.button("Predict probability"):

    prob = subject.predict(model)

    st.metric(
        label="Metabolic syndrome probability",
        value=f"{100*prob:.2f}%"
    )

    # -----------------------------
    # GRÁFICOS DENTRO DEL BOTÓN
    # -----------------------------

    plots = [
        {
            "hue": "Gender",
            "levels": ["F", "M"],
            "fixed": {
                "Alcohol_status": subject.alcohol,
                "Smoking_status": subject.smoking
            }
        },
        {
            "hue": "Smoking_status",
            "levels": alc_smo_df["Smoking_status"].unique(),
            "fixed": {
                "Gender": subject.gender,
                "Alcohol_status": subject.alcohol
            }
        },
        {
            "hue": "Alcohol_status",
            "levels": alc_smo_df["Alcohol_status"].unique(),
            "fixed": {
                "Gender": subject.gender,
                "Smoking_status": subject.smoking
            }
        }
    ]

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for ax, plot in zip(axes, plots):

        pred_rows = []

        for age in range(20, 91):

            for level in plot["levels"]:

                row = {
                    "Real_age": age,
                    **plot["fixed"],
                    plot["hue"]: level
                }

                pred_rows.append(row)

        pred_df = pd.DataFrame(pred_rows)

        pred_df["Probability"] = model.predict(pred_df)

        sns.lineplot(
            data=pred_df,
            x="Real_age",
            y="Probability",
            hue=plot["hue"],
            ax=ax
        )

        ax.scatter(
            subject.age,
            subject.probability,
            s=120,
            zorder=10,
            marker='o',
            color='black'
        )

        ax.set_title(plot["hue"])
        ax.set_ylabel("Probability")
        ax.set_ylim(0, 1)

    plt.tight_layout()

    st.pyplot(fig)