import streamlit as st
import pandas as pd
import os
import pycaret
from pathlib import Path
from pycaret.regression import *
from joblib import load

def app():
    
    file = 'apps/cleaned_owler_data_data11.csv'
    path_to_file = (os.path.join((Path.cwd()),file))
    dataset = pd.read_csv(path_to_file)
    dataset.head()

    Title = "HHI"
    Description="The Herfindahl index is a measure of the size of firms in relation to the industry they are in and an indicator of the amount of competition among them."
    st.title(Title)
    st.markdown(Description)

    @st.cache
    def load_data():
        data = pd.read_csv("apps/cleaned_owler_data_data11.csv")
        return data
    data = load_data()
    st.write(data)


    clf = load('apps/hhi.joblib')
    if st.sidebar.checkbox("Predit HHI", False):
        st.header("Predit HHI of a startup based on these features")
        # Declare a form and call methods directly on the returned object
        f = st.form(key='ml_form')
        competitor_count = [0,0,0,0,0,0,0,0,0,0]
        competitor_count[f.selectbox("Competitor count (cap at 10)", [1, 2, 3,4,5,6,7,8,9,10]) -1] = 1
        company_revenue = f.number_input(label='Total Company Revenue in Millions')
        competitor_revenue = f.number_input(label='Total Competitor Revenue in Millions')
        submitted = f.form_submit_button(label='Submit!')
        if submitted:
            my_data = np.array([company_revenue,competitor_count[0],competitor_revenue,competitor_count[9],competitor_count[5],competitor_count[3],competitor_count[8],competitor_count[7],competitor_count[6],competitor_count[1],competitor_count[2],competitor_count[4]])
            print(my_data)
            try:
                prediction = clf.predict([my_data])
            except Exception as e:
                f.error(f"Could not make prediction. {e}")
            st.write(prediction[0])

        pass

