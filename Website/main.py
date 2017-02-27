from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add_movie")
def add_movie():
    return render_template("add_movie.html")

@app.route("/movies")
def movies():
    return render_template("movie_library.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()