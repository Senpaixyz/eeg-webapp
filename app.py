from flask import Flask, render_template, request
from flask import escape
import pickle
import random
app = Flask(__name__)


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route('/start', methods=['GET'])
def start():
    return render_template('menu.html')

if __name__ == "__main__":
    #app.run(debug=True, host='0.0.0.0', port='5000')
    app.run(debug=True)