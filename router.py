from flask import Flask, render_template

app = Flask(__name__)

@app.route('/news')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask
from flask.templating import render_template