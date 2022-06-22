import flask

# Create the application instance
app = flask.Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Hello World!</h1>
    <p>This is the home page.</p>
    <p><a href="/about">About</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)