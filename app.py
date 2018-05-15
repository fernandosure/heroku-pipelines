import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Johannes! Current Profile: %s" % os.getenv("CURRENT_PROFILE")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)