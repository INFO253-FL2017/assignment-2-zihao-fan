"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__, static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/<page_name>')
def show_top_pages(page_name):
    if not page_name.endswith('.html'):
        page_name += '.html'
    return render_template(page_name)

@app.route('/blog/<blog_title>')
def show_blog_pages(blog_title):
    if not blog_title.endswith('.html'):
        blog_title += '.html'
    return render_template('/blog/' + blog_title)