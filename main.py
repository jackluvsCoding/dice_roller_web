from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Congratulations, it's a web app!"


# These two lines tell Python to start Flask’s development server when the script is executed from the command line.
# Start Flask's development server and interact with the Python app in browser via: $ 'python3 main.py'
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)