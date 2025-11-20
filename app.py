from flask import Flask, request, jsonify
import pandas as pd
from surprise import SVD, Dataset, Reader
from surprise.model_selection import train_test_split

app = Flask(__name__)

# ---------------------------------------------------------
# Load or Create Synthetic Interaction Data
# ---------------------------------------------------------

def load_interaction_data():
    """
    Load synthetic or logged user interactions.
    If no data file exists, returns an empty DataFrame.
    """
    try:
        df = pd.read_csv("data/interactions.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["user_id", "product_clicked", "purchased"])


interaction_df = load_interaction_data()


# ---------------------------------------------------------
# Rule-Based Recommendation Engine
# ---------------------------------------------------------

def get_top_products(df, n=5):
    """
    Returns the top-N most clicked products.
    """
    if df.empty:
        return []
    return df["product_clicked"].value_counts().head(n).index.tolist()


# ---------------------------------------------------------
# Collaborative Filtering (SVD)
# ---------------------------------------------------------

def train_svd_model(df):
    """
    Train an SVD collaborative filtering model.
    """
    if df.empty:
        return None

    reader = Reader(rating_scale=(0, 1))
    data = Dataset.load_from_df(df[["user_id", "product_clicked", "purchased"]], reader)
    
    trainset, _ = train_test_split(data, test_size=0.2)
    
    model = SVD()
    model.fit(trainset)
    return model


svd_model = train_svd_model(interaction_df)


# ---------------------------------------------------------
# Hybrid Recommendation Logic
# ---------------------------------------------------------

def recommend_products(user_id):
    """
    Recommends products:
    - If user has previous interactions → personalized SVD
    - If user is new → rule-based fallback
    """
    # Fallback for empty dataset
    if interaction_df.empty:
        return []

    # Check user history
    user_history = interaction_df[interaction_df["user_id"] == user_id]

    if user_history.empty:
        # New user → popular products
        return get_top_products(interaction_df)

    # Existing user → use SVD predictions
    products = interaction_df["product_clicked"].unique()
    predictions = []

    for product in products:
        pred = svd_model.predict(user_id, product).est
        predictions.append((product, pred))

    # Sort by predicted score
    predictions.sort(key=lambda x: x[1], reverse=True)

    # Return top 5 products
    top_recommendations = [p[0] for p in predictions[:5]]

    return top_recommendations


# ---------------------------------------------------------
# Flask API Endpoint
# ---------------------------------------------------------

@app.route("/recommend", methods=["GET"])
def recommend():
    """
    GET /recommend?user_id=123
    Returns top recommendations for that user.
    """
    user_id = request.args.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    recommendations = recommend_products(user_id)

    return jsonify({
        "user_id": user_id,
        "recommendations": recommendations
    })


# ---------------------------------------------------------
# Run API
# ---------------------------------------------------------

if __name__ == "__main__":
    print("Starting Recommendation API...")
    app.run(host="0.0.0.0", port=5000, debug=False)
