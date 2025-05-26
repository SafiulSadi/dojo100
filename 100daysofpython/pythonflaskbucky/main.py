from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return "This is the home page"

@app.route("/tuna")
def tuna():
    return "<h2>Tuna is good!</h2>"


if __name__ == "__main__":
    app.run(debug=True)