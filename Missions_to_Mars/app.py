from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from scrape_mars import scrape

# Create an instance of Flask
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Route that will trigger the scrape function
@app.route("/scrape")
def scrape


if __name__ == "__main__":
    app.run(debug=True)
