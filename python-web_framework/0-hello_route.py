from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Route handler for the root URL (/).

    Returns:
        str: The greeting message 'Hello HBNB!'.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    """
    Start the Flask server.
    """

    app.run(host='0.0.0.0', port=5000)
