import numpy as np
import sklearn
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle
import yfinance as yf

def linregModel(inp):
    nio = yf.Ticker(inp)
    history = nio.history(period = "Max")
    dataset = pd.DataFrame(history)
    #print(dataset)
    x = dataset[['Open', 'High','Low']]
    y = dataset["Close"]

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=.2, shuffle=False, random_state = 0)
    model = linear_model.LinearRegression()

    model.fit(x_train, y_train)
    accuracy = model.score(x_test, y_test)
    #print(accuracy)
    predicted = model.predict(x_test)
    #print(predicted)
    return model

def prediction(inp, opening, high, low):
    linregModel(inp)
    return linregModel(inp).predict([[opening, high, low]])

def plotData(inp):
    nio = yf.Ticker(inp)
    history = nio.history(period="Max")
    dataset = pd.DataFrame(history)

    return dataset



print (prediction('MSFT', 250, 252, 248))