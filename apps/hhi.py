import streamlit as st
import pandas as pd
import os
from pathlib import Path
import pickle
#from sklearn.ensemble import AdaBoostRegressor
import numpy as np
import time

def app():
    
    file = 'apps/cleaned_owler_data_data11.csv'
    path_to_file = (os.path.join((Path.cwd()),file))
    dataset = pd.read_csv(path_to_file)
    dataset.head()

    Title = "HHI"
    Description=r"> The Herfindahl index is a measure of the size of firms in relation to the industry they are in and an indicator of the amount of competition among them."
    st.title(Title)
    st.markdown(Description)

    @st.cache
    def load_data():
        data = pd.read_csv("apps/cleaned_owler_data_data11.csv")
        data.dropna(inplace=True)
        return data.iloc[:,1:]
    data = load_data()
    st.write(data)

    def load_model(path='apps/hhi_sklearn_final.pkl'):
        model = pickle.load(open(path,'rb'))
        return model

    clf = load_model()

    if st.sidebar.checkbox("Predit HHI", False):
        st.header("Predit HHI of a startup based on these features")
        # Declare a form and call methods directly on the returned object
        f = st.form(key='ml_form')
        
        competitor_count = f.slider("Competitor count (cap at 10)",1,10) 
        company_revenue = f.slider('Total Company Revenue in Millions',1,10000)
        competitor_revenue = f.slider('Total Competitor Revenue in Millions',1,10000)
        submitted = f.form_submit_button(label='Submit!')
        
        if submitted:
            with st.spinner("Finding the HHI score ....."):
                time.sleep(2.3)
                my_data = np.array([company_revenue,competitor_count,competitor_revenue])
                print(my_data)
                try:
                    prediction = clf.predict([my_data])
                    result = round(prediction[0],2)

                    st.markdown(""" ### HHI score : """ + str(result))


                except Exception as e:
                    f.error(f"Could not make prediction. {e}")
                

    

