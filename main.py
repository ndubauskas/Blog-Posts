from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
post_data = response.json()

for post in post_data:
    print(post["title"])
app = Flask(__name__)

@app.route('/')
def get_posts():
    return render_template("index.html",post_data=post_data)


@app.route('/post/<int:id>')
def show_post(id):
    requested_post = None
    for blog_post in post_data:
        if int(blog_post["id"]) == id:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
