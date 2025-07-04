import streamlit as st
import pandas as pd 
import pickle as pk 


model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction App')

no_of_dep = st.slider('choose No of dependents',0,5)
grad = st.selectbox('choose Education',['Graduated','Not Graduate'])
self_emp = st.selectbox('self Employed ',['Yes','No'])
Annual_Income = st.slider('choose Annual Income',0,10000000)
Loan_Ammount = st.slider('choose Loan Amount',0,10000000)
Loan_Duration = st.slider('choose Loan Duration',0,20)
cibil = st.slider('choose Cibil score',0,1000)
Assets = st.slider('choose Assets',0,10000000)

if grad =='Graduated':
    grad_s =0
else:
    grad_s = 1

if self_emp =='No':
    emp_s =0
else:
    emp_s = 1

if st.button("Predict"):
    pred_data = pd.DataFrame([[no_of_dep,grad_s,emp_s,Annual_Income,Loan_Ammount,Loan_Duration , cibil ,Assets]],
                         columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Loan Is Approve')
    else:
        st.markdown('Loan Is Rejected')