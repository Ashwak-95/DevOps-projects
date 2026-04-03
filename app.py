from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Kubernetes(K8s)!"

healthy = True

@app.route("/health")
def health():
    if healthy:
        return "OK", 200
    else:
        return "FAIL", 500

@app.route("/break")
def break_app():
    global healthy
    healthy = False
    return "App is now broken"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)