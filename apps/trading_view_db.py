from json import load
import streamlit as st
import streamlit.components.v1 as components
import os

def read_markdown(path,parent = 'about/'):
    with open(os.path.join(parent,path)) as f:
        return f.read()

def load_dataviz(path='./images/databoard.html'):
    with st.spinner("Loading the Dashboard......"):
        with open(path) as f:
            trading_view_db = f.read()
            check = 0
            return trading_view_db

def app():
    
    st.markdown(read_markdown("task7_2.md"))
    
    components.html(load_dataviz(),height = 600,width = 1600)
    
    