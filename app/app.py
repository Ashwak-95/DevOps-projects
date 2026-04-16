from flask import Flask

app = Flask(__name__)

healthy = True


@app.route("/")
def home():
    if healthy:
        return "Hello from Kubernetes(K8s)!\n"
    return "Service Unavailable\n", 500


@app.route("/live")
def live():
    if healthy:
        return "Yes, Live\n", 200
    return "FAIL\n", 500


@app.route("/ready")
def ready():
    if healthy:
        return "Yes, Ready\n", 200
    return "FAIL", 500


# Break the app (simulate failure)
@app.route("/break")
def break_app():
    global healthy
    healthy = False
    return "App is broken\n"


# Recover the app
@app.route("/fix")
def fix_app():
    global healthy
    healthy = True
    return "App is READY again\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)