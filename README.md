

# **AI_Project_1 – End-to-End Recommendation System with Flask API**

This project demonstrates a complete end-to-end **machine learning recommendation system** suitable for e-commerce or content platforms. It covers **synthetic data generation**, **rule-based and collaborative filtering algorithms**, and **real-time model deployment** using a **Flask REST API**.

---

## **Features**

### **1. Synthetic Data Generation**

Simulates realistic user interactions using the **Faker** library, including product clicks and purchase decisions.

### **2. Exploratory Data Analysis (EDA)**

Analyzes user behaviour to identify:

* Most-clicked products
* Purchase conversion rates
* User preference patterns

### **3. Rule-Based Recommendation Engine**

Recommends the **Top 5 most-clicked products** using click frequency as the ranking metric.

### **4. Collaborative Filtering (SVD)**

Implements a **matrix factorization** model using the **surprise** library for personalized recommendations.

### **5. Model Evaluation**

Evaluates collaborative filtering performance using **RMSE** on a train/test split.

### **6. Flask REST API**

Deploys the recommendation system through an endpoint:
`GET /recommend?user_id=<id>`
Returns real-time recommendations in JSON format.

---

## **Technologies Used**

* **Python**
* **Pandas**
* **Faker**
* **scikit-surprise**
* **Flask**
* **Jupyter Notebook / Google Colab**

Deployment: Local Flask server (extendable to cloud hosting platforms such as AWS, GCP, Azure).

---

## **How It Works**

### **1. Data Simulation**

Generates interaction logs for **100 users** across **20 products**.

### **2. Analysis & Recommendation Logic**

* Popularity-based recommendation (rule-based)
* Personalized recommendation using **SVD collaborative filtering**

### **3. API Deployment**

The trained model and rule-based system are served through a Flask API to provide real-time recommendations based on user history.

---

## **Project Structure**

```
AI_Project_1/
│
├── data/                   # Synthetic data generation (optional)
├── models/                 # Trained model artifacts (optional)
├── app.py                  # Flask API
├── notebook.ipynb          # Full pipeline development
├── README.md               # Project documentation
└── requirements.txt        # Dependencies
```

---

## **Use Cases**

* E-commerce product recommendations
* Content platforms (movies, books, articles)
* User-behaviour modeling prototypes
* ML engineering portfolio projects

---

## **Status**

This is a working end-to-end pipeline demonstrating the lifecycle of an ML recommendation system. It can be extended with:

* Model persistence
* A/B testing
* Authentication
* Caching
* Cloud deployment

---

📁 Project Structure
AI_Project_1/
│
├── app.py
│   └── Flask REST API serving real-time recommendations
│
├── recommendation_system.py
│   └── Core ML pipeline:
│       • Synthetic data generation
│       • Rule-based recommendations
│       • Collaborative Filtering (SVD)
│       • Model evaluation (RMSE)
│
├── interactions.csv
│   └── Schema for logged user interactions
│       Columns:
│       user_id, product_clicked, purchased
│
├── requirements.txt
│   └── Project dependencies for reproducibility
│
└── README.md
    └── Project documentation

