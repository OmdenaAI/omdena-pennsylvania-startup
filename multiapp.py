import streamlit as st

class MultiApp:

	def __init__(self):
		self.apps = []

	def add_app(self,title,func='nothing'):
		self.apps.append({"title":title,"function":func})
		
	def run(self):

		st.sidebar.header("Navigate")
		app = st.sidebar.radio("",self.apps,format_func = lambda app: app["title"])
		#app = st.sidebar.selectbox("",self.apps,format_func = lambda app: app["title"])
		app["function"]()