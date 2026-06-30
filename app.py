from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    # The message requested for your backend validation test
    backend_message = "hello this is only ifr test from backend"
    return render_template("index.html", message=backend_message)

if __name__ == "__main__":
    # Your platform will inject a free port (like 5001). If none is found, it defaults to 8080.
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
