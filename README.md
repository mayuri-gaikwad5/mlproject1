## End to End machine learning project 
# Student Performance Prediction: End-to-End ML Project

## 🎯 Purpose of This Project

This project was implemented to:

- 📂 **Understand Project Structure**  
  Learn how real-world Machine Learning projects are organized using a clean and modular folder structure (components, pipelines, artifacts, etc.).

- ⚙️ **Learn End-to-End Implementation**  
  Gain hands-on experience in building a complete ML pipeline including:
  - Data Ingestion  
  - Data Transformation  
  - Model Training  
  - Prediction Pipeline  

- 🧠 **Apply Machine Learning Concepts**  
  Understand how different regression models work and how to select the best model based on performance metrics.

- 🌐 **Integrate with Web Application**  
  Learn how to deploy an ML model using Flask and make it accessible through a user-friendly interface.

- 🧪 **Follow Industry Practices**  
  Implement logging, exception handling, and reusable code to simulate real-world production-level ML systems.



## 📌 Project Overview
This project is an end-to-end Machine Learning solution designed to predict student performance (specifically Math scores) based on various demographic and academic factors. The project follows industry-standard practices, including modular coding, exception handling, logging, and a web-based interface for real-time predictions.

## 🏗️ Project Architecture
The project is divided into several modular components:
1.  **Data Ingestion**: Reads data from a source and splits it into training and testing sets.
2.  **Data Transformation**: Handles feature engineering, missing value imputation, and scaling using Scikit-Learn Pipelines.
3.  **Model Training**: Evaluates multiple regression algorithms to find the best-performing model.
4.  **Prediction Pipeline**: A dedicated pipeline to convert web input into a format suitable for the trained model to provide predictions.
5.  **Flask Web App**: A user-friendly interface for inputting data and viewing results.


---

## 🛠️ Features and Technologies
- **Python**: Core programming language.
- **Flask**: Web framework for the deployment.
- **Scikit-Learn**: For data preprocessing and model building.
- **CatBoost & XGBoost**: Advanced gradient boosting algorithms used for high accuracy.
- **Pandas & NumPy**: For data manipulation and numerical operations.

---

## 📁 Directory Structure
```text
├── artifacts/              # Stores raw, train, test data and serialized pickle files
├── notebook/               # Jupyter notebooks for EDA and Model Training
├── src/                    # Source code for the project
│   ├── components/         # Data Ingestion, Transformation, and Model Trainer
│   ├── pipeline/           # Training and Prediction Pipelines
│   ├── logger.py           # Logging configuration
│   └── exception.py        # Custom exception handling
├── templates/              # HTML files for the Flask web app
├── app.py                  # Flask application entry point
└── requirements.txt        # Project dependencies
```
## 🚀 Getting Started
# 1. Clone the repository
git clone <repository-url>
cd mlproject

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Training Pipeline
- To ingest data, transform it, and train the model, run:
python src/components/data_ingestion.py
- This will generate model.pkl and preprocessor.pkl in the artifacts/ folder.

# 5. Run the Web Application
- python app.py
Visit http://127.0.0.1:5000/ in your browser to use the application.

## 📊 Model Performance
- The ModelTrainer evaluates several models including:

- Random Forest
- Decision Tree
- Gradient Boosting
- Linear Regression
- XGBRegressor
- CatBoosting Regressor
- AdaBoost Regressor

The system automatically selects the model with the highest R2 Score (provided it is above 0.6) and saves it for production use.

## 📝 Usage
Once the web app is running:

Navigate to the Predict Data page.

Enter student details such as Gender, Race/Ethnicity, Parental Level of Education, Lunch Type, Test Prep Course, and Scores.

Click Predict to see the predicted Math Score.