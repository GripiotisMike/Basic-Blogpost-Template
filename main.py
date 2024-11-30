from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

API_URL = os.getenv("API_URL")  # Get the API URL from the .env file

@app.route('/')
def home():
    response = requests.get(API_URL)  # Fetch data from the API
    all_posts = response.json()  # Convert the response to JSON
    return render_template("index.html", all_posts=all_posts)  # Render the home page with posts

@app.route('/blog/<post_id>')
def blog(post_id):
    response = requests.get(API_URL)  # Fetch data from the API
    data = response.json()  # Convert the response to JSON
    selected_post = data[int(post_id) - 1]  # Get the specific post based on the post_id
    return render_template("post.html", num=post_id, content=selected_post)  # Render the post page

if __name__ == "__main__":
    app.run(debug=True)
