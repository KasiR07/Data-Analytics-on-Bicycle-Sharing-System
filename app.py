from flask import Flask, redirect, render_template

app  = Flask(__name__)
#Flask application instance
#special variable __name__ that holds the name of the current Python module

@app.route("/")
#turns a regular Python function into a Flask view function
#to signify that this function will respond to web requests for the URL /, which is the main URL.

def home():
    return render_template(r"index.html")
    #renders the html file

if __name__ == "__main__":
    app.run(debug=False, port=8000)
