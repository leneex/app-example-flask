from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    # Local run: port from PORT, 8000 by default
    port = int(os.getenv("PORT", "8000"))
    app.run(debug=True,host='0.0.0.0',port=port)
