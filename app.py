import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

model = pickle.load(open('Travel.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('predict.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    Age = request.form['Age']
    EmploymentType = request.form['EmploymentType']
    
    # Handle EmploymentType options
    if EmploymentType == 'private':
        EmploymentType = 0
    elif EmploymentType == 'public':
        EmploymentType = 1
    elif EmploymentType == 'student':
        EmploymentType = 2
    elif EmploymentType == 'retired':
        EmploymentType = 3
    elif EmploymentType == 'unemployed':
        EmploymentType = 4
    
    AnnualIncome = request.form['AnnualIncome']
    graduated= request.form['graduated']
    if graduated == 'yes':
        graduated = 1
    if graduated == 'no':
        graduated = 0
    
    FamilyMembers = request.form['FamilyMembers']
    ChronicDiseases = request.form['ChronicDiseases']
    
    # Handle ChronicDiseases options
    if ChronicDiseases == 'yes':
        ChronicDiseases = 1
    if ChronicDiseases == 'no':
        ChronicDiseases = 0

    FrequentFlyer = request.form['FrequentFlyer']
    
    # Handle FrequentFlyer options
    if FrequentFlyer == 'yes':
        FrequentFlyer = 1
    if FrequentFlyer == 'no':
        FrequentFlyer = 0

    EverTravelledAbroad = request.form['EverTravelledAbroad']
    
    # Handle EverTravelledAbroad options
    if EverTravelledAbroad == 'yes':
        EverTravelledAbroad = 1
    if EverTravelledAbroad == 'no':
        EverTravelledAbroad = 0
    
    total = [[int(Age), int(EmploymentType), float(AnnualIncome), int(FamilyMembers), int(ChronicDiseases), int(FrequentFlyer), int(EverTravelledAbroad),int(graduated),0]]
    prediction = model.predict(total)
    '''if  prediction== '1':
         prediction= 'yes'
      if prediction== '0':
         prediction = 'No' '''
    return render_template('final.html',prediction_text= 'The customer interested') 
    
if __name__ == "__main__":
    app.run(debug=True)

    