from flask import Flask, render_template_string
import random
import socket

app = Flask(__name__)

# HTML template with dynamic background color and hostname
template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title> {{ hostname }} Color Background</title>
    <style>
      body {
        background-color: {{ color }};
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-family: Arial, sans-serif;
      }
    </style>
  </head>
  <body>
    <h1>Hostname: {{ hostname }}</h1>
  </body>
</html>
"""

def random_color():
    """Generate a random hex color."""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

@app.route("/")
def index():
    color = random_color()
    hostname = socket.gethostname()
    return render_template_string(template, color=color, hostname=hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)