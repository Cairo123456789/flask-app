from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Mundo'

@app.route('/uic')
def uic_fun():
    return 'UIC'

if __name__ == '__main__':
    app.run(debug=True)