from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name": "My item",
                "price": 15.99
            }
        ]
    }
]

# @app.route("/")
# def home():
#     return render_template("index.html")

# POST /store data: {name:}
@app.route("/store", methods=["POST"]) # http://127.0.0.1:5000/store
def create_store():
    request_data = request.get_json()
    
    new_store = {
        "name": request_data["name"],
        "items": []
    }


    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route("/store/<string:name>") # http://127.0.0.1:5000/store/some_name
def get_store(name):

    for store in stores:
        if name == store["name"]:
            return jsonify(store)
    
    return jsonify({"message": "store not found"})

# GET /store
@app.route("/store") # http://127.0.0.1:5000/store
def get_stores():
    return jsonify({"stores": stores})

# POST /store/<string:name>/item data: {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"]) # http://127.0.0.1:5000//store/some_name/item
def create_item_in_store(name):
    request_data = request.get_json()
    
    new_items = {
            "name": request_data["name"],
            "price": request_data["price"]
        }

    for store in stores:
        if store["name"] == name:
            store["items"].append(new_items)
            return jsonify(store)

    return jsonify({"message": "store not found"})

# GET /store/<string:name>/item
@app.route("/store/<string:name>/item") # http://127.0.0.1:5000//store/some_name/item
def get_item_in_store(name):

    for store in stores:
        if store["name"] == name:
            return jsonify({"items": store["items"]})

    return jsonify({"message": "item not found"})


app.run(port=5000)