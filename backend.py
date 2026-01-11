from flask import Flask, request, jsonify, send_from_directory
from agent import run_agent

app = Flask(__name__, static_folder="frontend", static_url_path="")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    activity = data.get("activity", "").strip()

    if not activity:
        return jsonify({"error": "Activity required"}), 400

    result = run_agent(activity)
    return jsonify(result)

@app.route("/")
def index():
    return send_from_directory("frontend", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("frontend", path)

if __name__ == "__main__":
    app.run(debug=True)
