"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import requests
import os

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

@app.route('/email', methods=["POST"])
def send_email():
    notifications = []
    message = request.form.get("message")
    subject = request.form.get("subject")
    name = request.form.get("name")
    data = {
        'from': os.environ['INFO253_MAILGUN_FROM_EMAIL'],
        'to': os.environ['INFO253_MAILGUN_TO_EMAIL'],
        'subject': subject,
        'text': message,
    }

    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

    r = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
        auth=auth,
        data=data)

    if r.status_code == requests.codes.ok:
        notifications.append("Hi " + name + ", your message has been sent")
    else:
        notifications.append("You email was not sent. Please try again later")
    return render_template("contact.html", notification=notifications[0])