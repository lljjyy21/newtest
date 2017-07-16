from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/name')
def name(name = 'Tom'):
    return render_template('index.html', name = name)

@app.route('/<num>')
def add(num):
    result = "The number is {}".format(num)
    return render_template('index.html', name = result)


if __name__ == '__main__':
    app.run(debug= True)
