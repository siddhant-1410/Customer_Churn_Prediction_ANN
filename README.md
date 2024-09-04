# Customer_Churn_Prediction_ANN
Predicts whether the customer will churn or not. 
## Demo Video - 

https://github.com/user-attachments/assets/5c23b47d-d73e-40d2-bc31-9d2402d21697

# About
Predicting customer churn enables an organization to identify customers who are likely to discontinue their services, allowing the company to offer targeted discounts and special plans to retain them and boost business performance.

# Trying it out yourself
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
# Handling Imbalanced Dataset.
Handled the Imbalanced Datset by Evaluating 3 techinques-
* OverSampling
* UnderSampling
* SMOTE

SMOTE Performed the Best by increasing the f1-scores for both the classes to 81% each.
  
# Fine tuning
Fine tuned the MLP model using keras tuner to find out the best hyper-parameters
![image](https://github.com/user-attachments/assets/28525587-863e-4dba-b5d7-8ec42fc9a55b)

# Accuracy Graph
****![image](https://github.com/user-attachments/assets/22ade94f-a7ae-4b80-a255-1816f3f9b472)



