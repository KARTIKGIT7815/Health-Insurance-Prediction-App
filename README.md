# 🏥 Health Insurance Prediction App

A Streamlit web application that predicts the estimated health insurance
premium based on a user's personal information such as age, BMI, smoking
habits, gender, and number of children.

The application uses a machine learning model trained on health
insurance data and provides an instant premium prediction through an
interactive user interface.

------------------------------------------------------------------------

## 📌 Features

-   Simple and interactive Streamlit UI
-   Accepts user inputs:
    -   Age
    -   Gender
    -   Body Mass Index (BMI)
    -   Smoking status
    -   Number of children
-   Predicts estimated health insurance premium
-   Displays results using Streamlit metrics
-   Fast ML inference using a pickled trained model

------------------------------------------------------------------------

## 🧠 Machine Learning Model

The application loads a pre-trained machine learning model stored in:

Health_model.pkl

### Model Input Features

  Feature    Description
  ---------- --------------------------------
  Age        Age of the person
  BMI        Body Mass Index
  Children   Number of children
  Gender     Encoded (Male = 0, Female = 1)
  Smoker     Encoded (No = 0, Yes = 1)

------------------------------------------------------------------------

## 🖥️ User Interface

The Streamlit interface includes:

-   Age Input
-   Gender Selection
-   BMI Input
-   Smoking Status
-   Children Slider
-   Submit Button

Once the user clicks **Submit**, the model predicts and displays:

**Your Insurance Premium is: \$XXXX**

------------------------------------------------------------------------

## 📂 Project Structure

    Health-Insurance-Prediction-App
    │
    ├── app.py
    ├── Health_model.pkl
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## ⚙️ Installation

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/health-insurance-prediction.git
```

### 2. Navigate to the project directory

``` bash
cd health-insurance-prediction
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the Application

``` bash
streamlit run app.py
```

Then open your browser and go to:

http://localhost:8501

------------------------------------------------------------------------

## 📦 Requirements

Example requirements.txt

    streamlit
    scikit-learn
    pandas
    numpy

------------------------------------------------------------------------

## 🚀 Future Improvements

-   Add region input
-   Improve model accuracy
-   Deploy using Streamlit Cloud, Docker, or AWS
-   Add data visualizations
-   Enable model retraining

------------------------------------------------------------------------

## 👨‍💻 Author

This project demonstrates how machine learning models can be integrated
into interactive web applications using Streamlit.

------------------------------------------------------------------------

## 📜 License

This project is open-source and available under the MIT License.
