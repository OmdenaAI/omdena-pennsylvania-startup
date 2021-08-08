import streamlit as st
import os

def read_markdown(path,parent='about/'):
    with open(os.path.join(parent,path)) as f:
        return f.read()
    
def app():

    st.markdown(read_markdown("task7.md"))
    st.markdown(""" &nbsp """)
    st.markdown(""" **Check out the Demo** on [Hugging Face Spaces](https://huggingface.co/spaces/mlkorra/competitive-analysis) """)
    st.image('images/task7-ca.png',caption='Competitive Analysis demo on Hugging Face Spaces')
    