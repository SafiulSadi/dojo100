from flask import Flask, render_template
import random
from datetime import datetime
import requests

GENDERIZE_ENDPOINT = "https://api.genderize.io"
AGIFY_ENDPOINT = "https://api.agify.io"
BLOG_URL = "https://api.npoint.io/5abcca6f4e39b4955965"


app = Flask(__name__)

blog_data = [
  {
    "id": 1,
    "title": "The Life of Cactus",
    "subtitle": "Who knew that cacti lived such interesting lives.",
    "body": "Nori grape silver beet broccoli kombu beet greens fava bean potato quandong celery. Bunya nuts black-eyed pea prairie turnip leek lentil turnip greens parsnip. Sea lettuce lettuce water chestnut eggplant winter purslane fennel azuki bean earthnut pea sierra leone bologi leek soko chicory celtuce parsley jícama salsify."
  },
  {
    "id": 2,
    "title": "Top 15 Things to do When You are Bored",
    "subtitle": "Are you bored? Don't know what to do? Try these top 15 activities.",
    "body": "Chase ball of string eat plants, meow, and throw up because I ate plants going to catch the red dot today going to catch the red dot today. I could pee on this if I had the energy. Chew iPad power cord steal the warm chair right after you get up for purr for no reason leave hair everywhere, decide to want nothing to do with my owner today."
  },
  {
    "id": 3,
    "title": "Introduction to Intermittent Fasting",
    "subtitle": "Learn about the newest health craze.",
    "body": "Cupcake ipsum dolor. Sit amet marshmallow topping cheesecake muffin. Halvah croissant candy canes bonbon candy. Apple pie jelly beans topping carrot cake danish tart cake cheesecake. Muffin danish chocolate soufflé pastry icing bonbon oat cake. Powder cake jujubes oat cake. Lemon drops tootsie roll marshmallow halvah carrot cake."
  }
]

@app.route("/blog")
def blog():
    response = requests.get(BLOG_URL)
    all_posts = blog_data
    return render_template("blog.html",all_posts=all_posts )
    



def agify_api(name):
    genderize_body = {"name":{name}}    
    response = requests.get(AGIFY_ENDPOINT,params=genderize_body)
    return response.json()



def genderize_api(name):
    genderize_body = {"name":{name}}    
    response = requests.get(GENDERIZE_ENDPOINT,params=genderize_body)
    return response.json()

@app.route("/")
def hi():
    return render_template("index.html")



@app.route("/guess/<name>")
def hello(name):
    name = name.title()
    date = datetime.now()
    copyright_year = date.year
    gender = genderize_api(name)['gender']
    age = agify_api(name)['age']
    print(copyright_year)
    rand = random.randint(1, 10)
    return render_template('index.html',random_number=rand, copyright_year=copyright_year, gender=gender, age=age, name=name)






if __name__ == "__main__":
    app.run(debug=True)