import streamlit as st
from multiapp import MultiApp
from apps import hhi,growth,trading_view_db,competitive_analysis,about,status

def main():

    app = MultiApp()
    #app.add_app("Competitive Analysis",topic_model.app)
    
    app.add_app("Home",about.app)
    app.add_app("HHI ",hhi.app)
    app.add_app("Growth",growth.app)
    app.add_app("Status",status.app)
    app.add_app("Competitive Analysis",competitive_analysis.app)
    app.add_app("Trading View Dashboard",trading_view_db.app)
    app.run()

if __name__ == "__main__":
    main()