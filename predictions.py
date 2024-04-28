from flask import Flask, request
import pickle
import sklearn

model = open('classifier.pkl', 'rb')
clf = pickle.load(model)

app = Flask(__name__)

@app.route('/predict',methods=["POST"])
def predict():

    loan_req = request.get_json()

    # Encoding Gender
    if loan_req['Gender'] == 'Male':
        gender = 0
    else:
        gender = 1

    # Encoding Married
    if loan_req['Married'] == 'No':
        married = 0
    else:
        married = 1

    applicant_income = loan_req['ApplicantIncome']
    credit_history = loan_req['Credit_History']
    loan_amount = loan_req['LoanAmount']

    input_data = [[gender, married, applicant_income, credit_history, loan_amount]]
    prediction = clf.predict(input_data)

    if prediction == 1:
        pred = 'Accepted'
    else:
        pred = 'Rejected'

    return {"loan_approval_status": pred}






