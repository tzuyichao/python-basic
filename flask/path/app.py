from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World"

@app.route('/user/<name>')
def user(name):
    return "接收到的名稱為: %s" % name

if __name__ == '__main__':
    app.run(debug=True)