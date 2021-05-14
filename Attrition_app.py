
from flask import Flask, render_template,request
from flasgger import Swagger
import pickle
import pandas as pd

app = Flask(__name__)
test_df = pd.read_csv("test_dataset.csv")
pickle_file = open(Attrition.pkl','rb')
classifier = pickle.load(pickle_file)
Swagger(app)

@app.route("/")
def base_route():
    return "Welcome to Attrition prediction API",200

@app.route("/predictForSample",methods=['GET'])
def predictRate():
    """Swagger App for Attrition Prediction
    --------
    parameters:
    -   name: Age
        description: Age of the employees
        in: query
        type: integer
        required: true
    -   name: MonthlyIncome
        description : Salary of the employees
        in: query
        type: integer
        required: true
    -   name: TotalWorkingYears
        description : Total no. of years the employees have worked
        in: query
        type: integer
        required: true
    -   name: YearsAtCompany
        description : Total tenure the employees have worked there
        in: query
        type: integer
        required: true
    -   name: YearsWithCurrManager
        description : Total years the employees have worked with a particular manager
        in: query
        type: integer
        required: true
    -   name: DistanceFromHome
        description : How far the employee stays from the company
        in: query
        type: integer
        required: true
    -   name: Attrition
        description : Whether the employee is in company or did he leave
        in: query
        type: integer
        required: true
    responses:
        200:
            description : Predicted for Sample Employees
        201:
            description : Predicted for file containing all Customers
    """

    Age = request.args.get("Age")
    MonthlyIncome = request.args.get("MonthlyIncome")
    TotalWorkingYears = request.args.get("TotalWorkingYears")
    YearsAtCompany = request.args.get("YearsAtCompany")
    YearsWithCurrManager = request.args.get("YearsWithCurrManager")
    DistanceFromHome = request.args.get("DistanceFromHome")
    Attrition = request.args.get("Attrition")
    
    result = classifier.predict([[amount, length_employed, home_owner, income,
                                  income_verified,purpose,d2i,inquiries,open_accounts,
                                  total_accounts,gender,invalid_accounts,years2repay,
                                  deliquency,income_label1,income_label2,income_label3,
                                  loan_label1,loan_label2,loan_label3]])

    if(result in [0.0,"0"]) : return "No possibility for attrition"
    if(result in [1.0,"1.0"]) : return "Possible for Attrition"
   

if __name__ == "__main__":
    app.run(debug=True, host= "127.0.0.1", port= 5000)
