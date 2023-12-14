# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home', content='Welcome to my Flask app!')

@app.route('/about')
def about():
    return render_template('index.html', title='About', content='This is a simple Flask app.')

if __name__ == '__main__':
    app.run(debug=True)