from flask import Flask

app = Flask(__name__)

healthy = True


@app.route("/")
def home():
    return "Hello from Kubernetes(K8s)!"


@app.route("/live")
def live():
    if healthy:
        return "Yes, Live", 200
    return "FAIL", 500


@app.route("/ready")
def ready():
    if healthy:
        return "Yes, Ready", 200
    return "FAIL", 500


# Break the app (simulate failure)
@app.route("/break")
def break_app():
    global healthy
    healthy = False
    return "App is now broken"


# Recover the app
@app.route("/fix")
def fix_app():
    global healthy
    healthy = True
    return "App is READY again"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)