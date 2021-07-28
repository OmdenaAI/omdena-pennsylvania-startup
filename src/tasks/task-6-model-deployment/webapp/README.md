### High level overview of Streamlit App Deployment
- It consists of multiple pages to deliver multiple dashboards and models.
- `multiapp.py` contains the code for creating Multi Apps. No required to modify
- `apps` folder should contain all the scripts of different models and dashboards
- While creating a script in the `app` folder,define all your functionality in the `app()` function
- Then,add the corresponding app in the `app.py` 
-  ```streamlit run app.py``` to run the App
- Checkout existing apps for reference
