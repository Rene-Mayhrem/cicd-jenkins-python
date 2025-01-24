from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return jsonify({"message": "Hello World"})

@app.route("/health", methods=["GET"])
def health():
  return jsonify({"status":"healthy"})

if __name__ == "__main__":
  app.run(hos="0.0.0.0", port=5000)