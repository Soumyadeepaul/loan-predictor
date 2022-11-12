from flask import Flask,render_template,request
import pandas as pd
import pickle
import gspread
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route('/', methods=['GET','POST'])
def form_detail():
    if request.method=='POST':
        firstname=request.form.get('fname')
        lastname = request.form.get('lname')
        gender= request.form.get('gender')
        married = request.form.get('married')
        dependents=request.form.get('dependents')
        education = request.form.get('education')
        self_employed = request.form.get('self employed')
        property_area = request.form.get('property area')
        applicant_income = request.form.get('applicant income')
        coapplicant_income = request.form.get('coapplicant income')
        loan_amount = request.form.get('loan amount')
        loan_amount_term = request.form.get('loan amount term')
        credit_history=request.form.get('credit history')
        if request.form.get('submit')=='Submit':
            h = pd.DataFrame({'Gender': [gender], 'Married': [married], 'Dependents': [dependents], 'Education': [education], 'Self_Employed': [self_employed],
                              'ApplicantIncome': [float(applicant_income)], 'CoapplicantIncome': [float(coapplicant_income)], 'LoanAmount': [float(loan_amount)],
                              'Loan_Amount_Term': [float(loan_amount_term)], 'Credit_History': [credit_history], 'Property_Area': [property_area]})
            h1 = h[['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
                    'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']].values
            prediction=model.predict(h1)
            output=prediction[0]
            sa=gspread.service_account(filename='loan-data-368405-70ad9d328cad.json')
            sh=sa.open('Loan-data-user')
            wks=sh.worksheet('Sheet1')
            wks.insert_row([firstname,lastname,gender,married,dependents,education,self_employed,applicant_income,coapplicant_income,loan_amount,loan_amount_term,credit_history,property_area,output],wks.row_count)
            return render_template('result.html',ans=output)
    return render_template('loan.html')

if __name__=='__main__':
    app.run(debug=True)