# Multiple-Disease-Prediction-System

This project is a **Machine Learning-based web application** that predicts **Diabetes, Heart Disease, and Kidney Disease** using patient health data.

![Screenshot 2025-05-01 204205](https://github.com/user-attachments/assets/3e652d4a-2e59-400b-bbe2-1931f5240157)
![Screenshot 2025-05-01 204931](https://github.com/user-attachments/assets/874b1a91-f24e-45f6-adba-8adc1aff7123)
![Screenshot 2025-05-01 204942](https://github.com/user-attachments/assets/44b53e83-a9da-4e36-af0e-29634811a68d)



## Features
- **Diabetes Prediction** using ML models trained on medical data.  
- **Heart Disease Detection** using patient health metrics.  
- **Kidney Disease Classification** with relevant attributes.  
- **Real-time prediction** powered by trained models.  
- **User-friendly interface** built with **Streamlit**.  
## ⚙️ Technologies Used  
- **Development IDEs:** Jupyter Notebook (for training), VS Code (for app) 
- **Frontend:** Streamlit UI  
- **Machine Learning Models:** Logistic Regression, Decision Tree, Random Forest, XGBoost, Gradient Boosting, SVM, KNN  
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn  
- **Model Saving:** Pickle  
## Installation
1. Clone the repository:
```bash
git clone https://github.com/Sarvesh7617/Multiple_Disease_Prediction_Using_Machine_Learning.git
```
2. Navigate to the project directory
```bash
cd Multiple_Disease_Prediction_Using_Machine_Learning
```
3. For Machine Learning Models (Jupyter Notebook)  
```bash
pip install numpy pandas seaborn statsmodels matplotlib scikit-learn xgboost
```
4. For Streamlit Web App (app.py)
```bash
pip install streamlit pickle-mixin os numpy streamlit-option-menu
```
5. Run the Streamlit Application
```bash
streamlit run app.py
```
## 🔎 Usage Guide  
1. **Select the disease type** from the sidebar (Diabetes, Heart Disease, or Kidney Disease).  
2. **Enter patient details** such as age, glucose level, blood pressure, etc.  
3. Click **"Predict"** to analyze health data.  
4. See **instant diagnosis results** based on ML predictions!
## 📊 Model Performance  

### 🔹 Diabetes Prediction Model  
| **Model**                     | **Score** |
|--------------------------------|----------|
| **Random Forest Classifier**   | 88.82%   |
| **Gradient Boosting Classifier** | 87.50%   |
| **XGBoost**                    | 86.84%   |
| **SVM**                        | 84.87%   |
| **KNN**                        | 83.55%   |
| **Decision Tree Classifier**    | 82.89%   |
| **Logistic Regression**         | 80.92%   |
### 🔹 Kidney Disease Prediction Model  
| **Model**                     | **Score** |
|--------------------------------|----------|
| **Random Forest Classifier**   | 98.75%   |
| **Gradient Boosting**          | 98.75%   |
| **Decision Tree Classifier**    | 97.50%   |
| **Logistic Regression**        | 91.25%   |
| **SVM**                        | 75.00%   |
| **KNN**                        | 66.25%   |
| **XGBoost**                    | 65.00%   |

### 🔹 Heart Disease Prediction Model  
| **Model**                     | **Score** |
|--------------------------------|----------|
| **Logistic Regression**        | 81.97%   |
| **Random Forest Classifier**   | 80.33%   |
| **Decision Tree Classifier**   | 77.05%   |
| **SVM**                        | 62.30%   |

---

## 🔮 Future Enhancements  
- **Add Liver Disease Prediction** module.  
- **Improve UI & Data Visualization**.  
- **Deploy to Cloud for Public Access**.  

---
