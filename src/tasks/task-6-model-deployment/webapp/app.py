import streamlit as st
from multiapp import MultiApp
from apps import topic_model,trading_view_db,hhi

def main():

    app = MultiApp()
    app.add_app("Competitive Analysis",topic_model.app)
    app.add_app("Trading View Dashboard",trading_view_db.app)
    app.add_app("HHI Model",hhi.app)
    app.run()

if __name__ == "__main__":
    main()