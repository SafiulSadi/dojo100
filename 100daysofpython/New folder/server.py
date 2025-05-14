from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    date = datetime.now()
    copyright_year = date.year

    print(copyright_year)
    rand = random.randint(1, 10)
    return render_template('index.html',random_number=rand, copyright_year=copyright_year)





if __name__ == "__main__":
    app.run(debug=True)