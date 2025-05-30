# 🏠 House Price Prediction App

This is a simple **Streamlit web application** built as part of a task by **Certura** to predict house prices in India using a regression model. The app estimates prices based on key housing features using machine learning models.

---

## ✨ Features

- Predict house prices based on:
  - 🛏️ Number of Bedrooms  
  - 🛁 Number of Bathrooms  
  - 📐 Living Area (sq. ft.)  
  - 🏚️ Condition of the House  
  - 🏫 Number of Nearby Schools
- Easy-to-use web interface built with **Streamlit**
- Real-time predictions using a trained **Random Forest** model

---

## 🤖 Models Trained

Three regression models were trained and evaluated:
- 🌳 Decision Tree Regressor  
- 🌲 Random Forest Regressor  
- 📉 Linear Regression

After comparison, **Random Forest** was selected for deployment due to its best Performance and Accuracy.

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/house-price-predictor.git
cd house-price-predictor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

### 4. Access in Browser

The app should open automatically. If not, go to:

```
http://localhost:8501
```

---

## 📷 How to Use

1. Enter the house details in the sidebar:
   - Bedrooms
   - Bathrooms
   - Living Area
   - Condition (1 to 5)
   - Number of Nearby Schools
2. Click **Predict Price**
3. The predicted house price will be displayed instantly

---

## 📂 Project Structure

```bash
house-price-predictor/
├── app.py                 # Main Streamlit application
├── model/                 # Saved model files (e.g., linear_model.pkl)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

---

## 🧠 Tech Stack

- Python
- Scikit-learn
- Pandas
- Joblib
- Streamlit
- Matplotlib / Seaborn (optional for visuals)

---

## 📊 Model Evaluation

All three models were evaluated on the same dataset using standard regression metrics:

| Model               | MAE                | MSE                | R² Score         |
|--------------------|--------------------|--------------------|------------------|
| **Random Forest**  | 155,514.31         | 56,645,253,843.50  | 0.5528       |
| **Decision Tree**  | 161,001.65         | 63,529,512,115.78  | 0.4873           |
| **Linear Regression** | 160,739.75      | 58,989,887,688.24  | 0.5239           |

> 📌 **Note**: Random Forest performed the best overall in terms of lower MAE , MSE and higher R²


---

## 🤝 Contribution

Feel free to fork this repo, suggest improvements, or raise issues!

---

## 📄 License

This project is open-source and available under the MIT License.
