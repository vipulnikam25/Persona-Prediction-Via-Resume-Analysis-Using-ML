from sklearn.preprocessing import StandardScaler
import joblib
import numpy as np
from sklearn import datasets, linear_model

model = joblib.load("train_model.pkl")
scaler = StandardScaler()


def predict():
    gender = 'male'
    if gender == "Female":
        gender_no = 1
    else:
        gender_no = 2
    age = 37
    openness = 8
    neuroticism = 7
    conscientiousness = 8
    agreeableness = 8
    extraversion = 6
    result = np.array([gender_no, age, openness, neuroticism,
                      conscientiousness, agreeableness, extraversion], ndmin=2)
    final = scaler.fit_transform(result)
    personality = str(model.predict(final)[0])
