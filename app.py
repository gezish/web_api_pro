from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return "TODO"

@app.get("/search")
def search():
    args = request.args.get("q")
    return redirect(f"https://www.oxfordlearnersdictionaries.com/definition/english/?q={args}")

@app.get("/registration")
def register():
    return render_template("registration.html")
    """
    TODO: Render the home page provided under templates/index.html in the repository
    """
    return "TODO"

if __name__ == "__main__":
    app.run()