from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)


# Homepage route
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API"}), 200


# GET all products or filter by category
@app.route("/products")
def get_products():
    category = request.args.get("category")

    if category:
        filtered = [
            product for product in products
            if product["category"].lower() == category.lower()
        ]
        return jsonify(filtered), 200

    return jsonify(products), 200


# GET a product by ID
@app.route("/products/<int:id>")
def get_product_by_id(id):
    for product in products:
        if product["id"] == id:
            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)