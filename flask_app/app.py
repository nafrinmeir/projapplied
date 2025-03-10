from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client["demo_db"]
collection = db["items"]

@app.route("/items", methods=["GET"])
def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_item():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    collection.insert_one({"name": data["name"]})
    return jsonify({"message": "Item added"}), 201

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
