from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/information')
def information():
    return '<h2> Puppies are cute.</h2>'


@app.route('/puppy/<name>')
def puppy(name):
    return '<h2> This page is for puppy {}</h2>'.format(name.upper())


if __name__ == '__main__':
    app.run(debug=True)
