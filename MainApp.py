from flask import Flask, redirect, url_for, render_template, request
import pickle
import numpy as np

################################################333
### here is the pickle file

# model = pickle.load(open('#pickle file', 'rb'))

############################################33

app = Flask(__name__)


@app.route("/")  # this sets the route to this page --> Main/Home page
def home():

    return render_template('home.html')    


######## after the predict button is pressed he form will collect the values via this function

@app.route('/predict', methods=['POST'])
def home():


    ### collecting values
    Country_EE = request.form['Input 1']
    data2 = request.form['Input 2']
    data3 = request.form['Input 3']
    data4 = request.form['Input 4']
    data5 = request.form['Input 5']
    data6 = request.form['Input 6']
    data7 = request.form['Input 7']
    data8 = request.form['Input 8']
    data9 = request.form['Input 9']
    data10 = request.form['Input 10']

    #Encoding input
    #example

    if (Country_EE == "Yes"):
        Country_EE = 1

    if (Country_EE == "No"):
        Country_EE = 0



    arr = np.array([[data1, data2, data3, data4, data5,data6,data7,data8,data9,data10]])
    pred = model.predict(arr)
    # return render_template('after.html', data=pred)

    ## now just display the results


if __name__ == "__main__":
    app.run(debug=True)