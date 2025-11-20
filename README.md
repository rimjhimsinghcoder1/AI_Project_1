

---

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

Recommends the **Top 5 most-clicked products** using click frequency.

### **4. Collaborative Filtering Using SVD**

Implements a **matrix factorization** model from the **Surprise** library for personalized recommendations.

### **5. Model Evaluation**

Evaluates recommendation quality using **RMSE** on a train/test split.

### **6. Flask REST API**

Provides real-time recommendations via the endpoint:

```
GET /recommend?user_id=<user_id>
```

---

## **Technologies Used**

* **Python**
* **Pandas**
* **Faker**
* **scikit-surprise**
* **Flask**
* **Google Colab / Jupyter Notebook**

Deployment: Local Flask server, extendable to AWS/GCP/Azure.

---

## **How It Works**

### **1. Data Simulation**

Synthetic interaction logs for **100 users** and **20 products**.

### **2. Recommendation Logic**

* **Popularity-based** recommendations
* **Collaborative filtering (SVD)** for personalized ranking

### **3. API Deployment**

The ML pipeline and rule-based engine are exposed through Flask for real-time inference.

---

# **Project Structure **

```
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
│   └── Schema for interaction logs
│       Columns:
│       user_id, product_clicked, purchased
│
├── requirements.txt
│   └── Project dependencies for reproducibility
│
└── README.md
    └── Project documentation
```

*(Note: data/ and models/ folders were removed since they do not exist in repo and create confusion.)*

---

## **Use Cases**

* E-commerce recommendations
* Content and media platforms
* Behaviour analysis prototypes
* ML engineering portfolio projects

---

## **Status**

This is a working end-to-end ML system. Future improvements may include:

* Model persistence
* A/B testing
* Authentication
* Caching
* Cloud deployment

---

