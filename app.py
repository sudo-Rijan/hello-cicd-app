from flask import Flask
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "CI/CD app is running",
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
