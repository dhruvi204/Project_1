from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/user/<int:user_id>')
def get_user(user_id):
    users = {
        1: {"user_id": 1, "preferences": ["electronics", "books"]},
        2: {"user_id": 2, "preferences": ["clothing", "home appliances"]},
        3: {"user_id": 3, "preferences": ["sports", "outdoors"]}
    }
    return jsonify(users.get(user_id, {}))

@app.route('/product/<int:product_id>')
def get_product(product_id):
    products = {
        101: {"product_id": 101, "description": "A great electronic gadget."},
        102: {"product_id": 102, "description": "A stylish piece of clothing."},
        103: {"product_id": 103, "description": "A useful home appliance."},
        104: {"product_id": 104, "description": "A fun outdoor activity."},
        105: {"product_id": 105, "description": "A must-have sports item."},
        106: {"product_id": 106, "description": "An interesting book."}
    }
    return jsonify(products.get(product_id, {}))

if __name__ == '__main__':
    app.run(debug=True)
