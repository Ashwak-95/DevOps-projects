from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Kubernetes(K8s)!"

@app.route("/health")
def health():
    return "Health is OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)