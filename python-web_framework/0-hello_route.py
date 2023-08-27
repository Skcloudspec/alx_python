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
    
    Instructions:
    1. Save this code in a file named app.py.
    2. Open a terminal and navigate to the directory containing app.py.
    3. Execute the command `python3 app.py` to start the server.
    4. The server will listen on http://0.0.0.0:5000/.
    5. To test the server's correct output, open a new terminal window.
    6. Use the command `curl 0.0.0.0:5000` to see the expected output: 'Hello HBNB!'.
    7. Use the command `curl 0.0.0.0:5000/noroute` to see a 'Not Found' message with a 404 status code.
    8. To stop the server, go back to the terminal where it's running and press Ctrl + C.
    """

    app.run(host='0.0.0.0', port=5000)
