from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage."""
    return render_template("mainpage.html")

if __name__ == "__main__":
	app.run(port=5002, host='0.0.0.0')