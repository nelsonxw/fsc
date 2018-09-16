# import dependencies
import os
import pandas as pd
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

# set up Flask
app = Flask(__name__)


# define different routes
@app.route("/")
def home():
    # render homepage
    return render_template("fsc.html")


if __name__ == '__main__':

    env_port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=env_port, debug=True)

