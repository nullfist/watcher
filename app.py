from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Nothing interesting here also ."

@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /hidden_9473"

@app.route("/hidden_9473")
def secret():
    return "FLAG: NULLCTF{robots_are_bad_at_keeping_secrets}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
