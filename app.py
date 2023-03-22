from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)
# Define what the app does
@app.get("/greet")
def index():
    fname = request.args.get("fname")
    lname = request.args.get("lname")

    if not fname and not lname:
        return jsonify({"status" : "error"})
    elif fname and not lname:
        response = {"data" : f"Hello, {fname} !"}
    elif not fname and lname:
        response = {"data" : f"Hello, Mr. {lname} ?"}
    else:
        response = {"data" : f"Is your name , {fname} {lname} ?"}
    
    return jsonify(response)

    