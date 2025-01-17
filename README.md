# AI_Project_1
End-to-End Recommendation System with Flask API Integration
Overview
This project demonstrates the development of an end-to-end recommendation system designed for e-commerce or content platforms. It includes synthetic data generation, product recommendations using rule-based and collaborative filtering approaches, and real-time deployment via a Flask API.

Features
Synthetic Data Generation: Simulated user interactions with the Faker library to mimic real-world data.
Exploratory Data Analysis: Identified popular products and calculated purchase conversion rates.
Rule-Based Recommendation: Recommended the top 5 most-clicked products based on user interactions.
Collaborative Filtering: Implemented an SVD-based recommendation engine using the surprise library.
Flask API: Deployed the recommendation system through a REST API for real-time predictions.
Model Evaluation: Measured the performance of the collaborative filtering model with RMSE.
Technologies Used
Programming Languages: Python
Libraries: Pandas, Faker, scikit-surprise, Flask
Frameworks: Flask (for API development)
Tools: Jupyter Notebook, Colab (for prototyping and development)
Deployment: Local Flask server with potential for cloud hosting.
How It Works
Synthetic Data: Generates user interaction data (clicks and purchases) for 20 products and 100 users.
Analysis & Recommendations:
Popular products are identified through click counts.
Collaborative filtering predicts personalized recommendations.
API Deployment: The Flask API serves recommendations to users based on their unique interactions.
