## Task 5 - Model Building


* Created ML Models for various objectives 

  - HHI score
  - Employee Growth %
  - Status (Acquired or Closed)

* Performed Hyperparameter tuning to improve results
* Used PyCaret AutoML Library to create models and quickly get results.
* Best Model obtained from PyCaret is choosen to re-train and deploy with same hyperparameters using scikit-learn to reduce the slug size of dependencies on Heroku (PyCaret is huge package to deploy it on Heroku).

### Results

> Regression Models

| Objective     | Model Used           | MAE | MSE | RMSE | R2   |
| ------------- | ---------------------| --- | --- | ---- | ---- |
| HHI           | AdaBoost Regressor   | 0.14| 0.03| 0.18 | 0.43 |   
| Growth %      | RandomForest Regressor | 27.3 |2142.39  |46.28  |0.48 |


> Classification Models

| Objective     | Model Used             | Accuracy | Recall | Precision | F1   |
| ------------- | --------------------  -| ---      | ---    | ----      | ---- |
| Status| RandomForest Classifier| 0.84     | 0.94   | 0.832     | 0.88 |
