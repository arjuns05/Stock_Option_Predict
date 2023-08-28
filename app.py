from flask import Flask, render_template, Response, request
from optionprice import Option
import model
import universalModel
import numpy as np
import sklearn
import pandas as pd
from sklearn import linear_model
from sklearn.utils import shuffle
import json
import plotly
import plotly.express as px

date2 = ""
price = ""
graphJSON= ""
app = Flask(__name__)

model.linregModel()

def newOption (option_inp):
    testOption = Option(european = False, kind = app.call_put, s0 = app.initial_price, k = app.strike_price, r=.05, sigma = .01, start = app.date_init, end = app.date_final, dv = 0)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/stock')
def stock():
    return render_template('stock.html',  data = date2)

@app.route('/stock', methods=['POST'])
def my_form_post():
    global date2
    global graphJSON
    name = request.form['name']
    opening = int(request.form['opening'])
    high = int(request.form['high'])
    low= int(request.form['low'])
    date2 = "$ " + str(round((universalModel.prediction(name, opening, high, low)[0]), 2))

    plotData = universalModel.plotData(name)
    print (plotData)
    fig = px.line(plotData, y='Close', title = "Closing Price over Time")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('stock.html', data = date2, graphJSON=graphJSON)


@app.route('/option')
def option():
    return render_template('option.html', opt = price)


@app.route('/option', methods=['GET','POST'])
def my_form_post1():
    global price

    initial_price = int(request.form["price"])
    strike_price = int(request.form['strike'])

    time = int(request.form['time'])

    print (initial_price)
    print(strike_price)
    print(time)


    # userOption = Option(european=False, kind="call", s0=initial_price, k=strike_price, sigma=.01, r=.05,
    #                     start=date_init, end=date_final, dv=0)

    testOption = Option(european=True, kind="put", s0=initial_price, k=strike_price, sigma=.01, r=.05, t= time)
    testPrice = round(testOption.getPrice(), 2)

    #price = userOption.getPrice()
    print (price)
    return render_template('option.html', opt= "$ " + str(testPrice))

if __name__ == "__main__":
    app.run(debug = True)


















