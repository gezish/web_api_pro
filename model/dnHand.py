# dictionary-api-python-flask/app.py
from flask import Flask, request, jsonify, render_template
from model.dbHandler import match_exact, match_like

app = Flask(__name__)


@app.get("/")
def index():
    """
    DEFAULT ROUTE
    This method will
    1. Provide usage instructions formatted as JSON
    """
    response = {"usage": "/dict?=<word>"}
    # Since this is a website with front-end, we don't need to send the usage instructions
    return jsonify(response)


@app.get("/dict")


def dictionary():
    """
    DEFAULT ROUTE
    This method will
    1. Accept a word from the request
    2. Try to find an exact match, and return it if found
    3. If not found, find all approximate matches and return
    """
    words = request.args.getlist("word")
    if not word:
        response = {"status": "error", "word": "words","data": "Word not Found"})
        return jsonify(response)

    response = {"words":[]}   
    for word in words:

        definitions = match_exact(word)

        if definitions:
            response["words"].append({"status": "success", "data": definitions,"words":word})
        else:
            definitions = match_like(word)
            if definitions:
                response["words"].append({"status": "partial", "data": definitions, "words":word})
            else:
                response["words"].append({"status": "error", "data":"word not found","word": "words"})
    return jsonify

       

if __name__ == "__main__":
    app.run()