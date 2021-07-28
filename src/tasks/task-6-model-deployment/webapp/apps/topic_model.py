import streamlit as st
import streamlit.components.v1 as components

#import torch

#from bertopic import BERTopic

#@st.cache(persist=True,suppress_st_warning=True)
#def load_topic_model(model_path):

#    pass

    #model = torch.load(model_path, map_location = torch.device('cpu'))
    #print(model.get_params())
    #fig = model.visualize_topics()

    #st.plotly_chart(fig)

    # >>> import plotly.express as px
    # >>> fig = px.box(range(10))
    # >>> fig.write_html('test.html')


def app():

    st.title("Competitive Analysis of Companies ")
    #model_path = './models/competitive_analysis_model'
    #load_topic_model(model_path)

    #st.header("test html import")
    HtmlFile = open("./plots/topicmodel.html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    #print(source_code)
    components.html(source_code,height = 700) 
    