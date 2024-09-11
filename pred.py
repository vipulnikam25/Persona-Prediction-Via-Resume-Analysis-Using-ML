
import sklearn.preprocessing as pre
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle

warnings.filterwarnings("ignore")

data = pd.read_csv('train.csv')
data = np.array(data)

X = data[:, :-1]
y = data[:, -1]
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)


def predict_forest(gender_code, age, ope, neu, con, agr, ext):
    input = np.array(
        [[gender_code, age, ope, neu, con, agr, ext]]).astype(np.float64)
    prediction = log_reg.predict(input)
    # pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return prediction


gender_code = 0
age = 15
ope = 8
neu = 7
con = 9
agr = 6
ext = 6
output = predict_forest(gender_code, age, ope, neu, con, agr, ext)
print(output)
