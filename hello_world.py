from flask import Flask

app = Flask(__name__)


@app.route('/')  # 127.0.0.1:5000
def hello_world():
    return '<h1>Hello, World!</h1>'


@app.route('/country')  # 127.0.0.1:5000/country
def my_country():
    return '<h1>Hello Hungary!</h1>'


@app.route('/horde/<name>')  # 127.0.0.1:5000/horde/Garrosh e.g.
def hero(name):
    return '<h1>This is a page for {}!</h1>'.format(name)


@app.route('/error')  # 127.0.0.1:5000/error
def my_error():
    message = '<h1>Testing debug</h1>'
    return message[100]


if __name__ == '__main__':
    app.run(debug=True)
