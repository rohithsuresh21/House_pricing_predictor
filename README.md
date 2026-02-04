# House_pricing_predictor

## House Price Prediction using Linear Regression
## Project Overview
This project demonstrates a basic machine learning pipeline for predicting house prices using Linear Regression in Python.
The model estimates house prices (in lakhs INR) based on features such as:
Square footage (sqft)
Number of bedrooms
Age of house
City location (Mumbai, Delhi, Bangalore)

##The project also showcases:
Data preprocessing using pandas
One-hot encoding for categorical variables
Train-test split
Model evaluation using Mean Absolute Error

## Technologies Used
Python
pandas
numpy
scikit-learn



## Project Structure
house_pricing.py   # Main script containing dataset, model training, and prediction
README.md          # Project documentation

## Model Workflow
Create dataset using pandas DataFrame.
Apply one-hot encoding to the city column.
Split dataset into training and testing sets.
Train a Linear Regression model.
Predict price for a new house sample.
Output predicted price.



## Example Prediction
The script predicts the price for:
2100 sqft house
3 bedrooms
4 years old
Located in Bangalore

*Output example:*
predicted house price : ₹XXX.XX lakhs

