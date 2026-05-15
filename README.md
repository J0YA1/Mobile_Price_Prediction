# 📱 Mobile Price Prediction

A Machine Learning project that predicts the price of mobile phones based on hardware specifications such as RAM, battery capacity, camera quality, processor performance, and display characteristics.

---

# 🚀 Project Overview

This project uses Regression Algorithms to estimate mobile phone prices using various technical specifications.

The project includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Outlier Detection
- Multicollinearity Handling using VIF
- Feature Scaling
- Model Training
- Model Evaluation
- Streamlit Deployment

---

# 📊 Dataset Features

The dataset contains the following features:

| Feature | Description |
|---|---|
| weight | Weight of the mobile phone |
| ppi | Pixel Per Inch (display quality) |
| cpu core | Number of CPU cores |
| cpu freq | CPU frequency |
| internal mem | Internal storage capacity |
| ram | RAM size |
| RearCam | Rear camera megapixels |
| Front_Cam | Front camera megapixels |
| battery | Battery capacity |
| thickness | Thickness of the phone |
| Price | Target variable (mobile price) |

---

# 🧠 Machine Learning Workflow

## 1. Data Cleaning
- Removed unnecessary columns:
  - `Product_id`
  - `resolution`
  - `Sale`

## 2. Handling Invalid Values
- Replaced impossible zero values with NaN
- Applied Median Imputation

## 3. Exploratory Data Analysis
Performed:
- Correlation Heatmap
- Boxplots
- Distribution Analysis

## 4. Multicollinearity Handling
Used:
- Variance Inflation Factor (VIF)

Detected severe multicollinearity among features.

## 5. Feature Scaling
Applied:
- StandardScaler

## 6. Models Used
- Linear Regression
- Ridge Regression
- Lasso Regression

## 7. Evaluation Metrics
- MAE
- RMSE
- R² Score

---

# 📈 Best Model

Linear Regression performed best because it handled multicollinearity effectively using regularization.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

# 📂 Project Structure

```bash
Mobile-Price-Prediction/
│
├── code.py
├── model.pkl
├── scaler.pkl
├── mobile_price_prediction.ipynb
├── requirements.txt
├── README.md
