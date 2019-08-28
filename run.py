from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/callback')
def callback():
    return "Callback!"

if __name__ == '__main__':
    app.run()