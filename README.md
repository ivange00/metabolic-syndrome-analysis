# Metabolic Syndrome Analysis

This project analyzes a large Korean public health dataset and builds a statistical model to estimate the probability of metabolic syndrome based on demographic and lifestyle factors.

It combines exploratory data analysis, statistical modelling, and an interactive web application built with Streamlit.

------------------------------------------------------------------------

## Project objectives

The objectives of this project are:

-   Compute metabolic syndrome risk factors per individual

-   Define metabolic syndrome based on clinical criteria

-   Explore relationships between lifestyle habits and health outcomes

-   Build a logistic regression model to estimate metabolic syndrome probability

-   Deploy an interactive Streamlit application for real-time prediction

------------------------------------------------------------------------

## Dataset

The dataset comes from a Korean public health database available via the Korean Public Data Portal.

It contains approximately 1 million records with demographic, lifestyle, and clinical variables.

**Note:** The dataset is not included in this repository due to file size. Please obtain it from the original source: https://www.data.go.kr/data/15007122/fileData.do.

------------------------------------------------------------------------

## Methods

### Data preprocessing

-   Data cleaning
-   Variable selection
-   Risk factor calculation
-   Metabolic syndrome classification

For the waist circumference cut-off value as a risk factor, I use The Korean Society for the Study of Obesity (KSSO) as a source. https://pmc.ncbi.nlm.nih.gov/articles/PMC2858833/

### Exploratory analysis

The notebook includes:

-   Descriptive statistics

-   Boxplots of the number of risk factors according to:

    -   Smoking status
    -   Alcohol consumption

### Statistical models

Two models are developed:

#### Linear regression

Predicts the number of metabolic syndrome risk factors.

#### Logistic regression

Predicts the probability of metabolic syndrome using:

-   Age
-   Sex
-   Smoking status
-   Alcohol consumption

The models were built using statsmodels.

------------------------------------------------------------------------

## Interactive Application

A Streamlit web application allows users to:
-    Input age, sex, smoking status and alcohol consumption
-    Obtain an estimated probability of metabolic syndrome

### Run the app locally

```bash
streamlit run app.py
```

------------------------------------------------------------------------

## Model

The trained model is saved using `joblib` with compression:

```python
joblib.dump(model, "model.pkl", compress=3)
```

The model is loaded in the Streamlit app for inference.

------------------------------------------------------------------------

## Repository Structure

```text
.
├── LICENSE
├── README.md
├── metabolic_syndrome_analysis.ipynb
├── model.pkl
├── ms_probability_app.py
└── requirements.txt
```

------------------------------------------------------------------------

## Technologies Used

- Python
- pandas
- numpy
- matplotlib
- statsmodels
- streamlit
- joblib

------------------------------------------------------------------------

## License

This repository is released under the MIT License.
