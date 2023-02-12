from flask import Flask, render_template

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')