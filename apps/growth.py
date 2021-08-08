import os
import streamlit as st
import pandas as pd
import pickle
import numpy as np
import json
import time
#from sklearn.ensemble import RandomForestRegressor

with open("apps/city_encode.json") as f:
    city_cfg = json.loads(f.read())
    #print(city_cfg.keys())

#@st.cache(allow_output_mutation=True)
def Load_Model(path = 'apps/growth_percentage_1.pkl'):

    model = pickle.load(open(path,'rb'))
    return model

@st.cache
def load_data():

   data = pd.read_csv('data/Startup_statewise_cleaned.csv')
   data.dropna(inplace=True)
   data['founded'] = data['founded'].astype('str')
   def clean(x):
       
       return x.split('.')[0]

   data['founded'] = data['founded'].apply(clean)
   #print(data['founded'][0].replace(',',''))
   return data

model = Load_Model()

def app():

    st.title("Predict Growth %")
    st.markdown(r"> Predict the Employee Growth percentage")
    st.write(load_data())

    if st.sidebar.checkbox("Predict Growth",False):
        st.markdown(""" ##  Predict Employee Growth of a startup based on the following features """)
          
        user = st.form(key = 'growth_predict_form')
        #city = float(user.number_input(label='City'))
        cities_list = list(city_cfg.keys())
        city  = str(user.selectbox("City",cities_list))
        city_encode = city_cfg[city]
        
        employees = (user.slider("Number of Employees",1,5000))
        founded_year = user.slider("Founded Year",2000,2020)
        city_ranking = (user.slider("City Rank of the Startup",1,100))
        estimated_revenue = float(user.slider("Estimated Revenue (in millions)",1,1000))
        job_openings  = (user.slider("No. of Job Openings",1,500))
  
        submit_bt  = user.form_submit_button(label='Submit!')
        if submit_bt:
            
            with st.spinner("Predicting the Employee Growth %"):
                time.sleep(2)
                user_input = np.array([city_encode,employees,founded_year,city_ranking,job_openings,estimated_revenue])
                try:
                    
                    prediction = model.predict([user_input])
                    result = round(prediction[0],2)

                    st.markdown(""" ### Employee Growth : """ + str(result) + "%")


                except Exception as exc:
                    user.error(f"Could not make prediction. {exc}")
                    print(exc)