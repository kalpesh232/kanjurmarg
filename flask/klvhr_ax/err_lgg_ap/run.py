from flask import Flask, jsonify, request
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)

# ---------- LOGGING SETUP ----------
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

handler = RotatingFileHandler(
    os.path.join(LOG_DIR, "app.log"),
    maxBytes=1_000_000,
    backupCount=3
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

app.logger.handlers.clear()
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)
app.logger.propagate = False

# PROOF LOG
app.logger.info("Application started")

# ---------- CUSTOM ERROR ----------
class InvalidUsage(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    app.logger.warning(error.message)
    return jsonify({"error": error.message}), error.status_code

@app.errorhandler(404)
def not_found(e):
    app.logger.warning("404 Not Found")
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def server_error(e):
    app.logger.error("Internal Server Error", exc_info=True)
    return jsonify({"error": "Internal Server Error"}), 500

# ---------- ROUTES ----------
@app.route("/health", methods=["GET"])
def health():
    app.logger.info("Health endpoint called")
    return jsonify({"status": "OK"})

@app.route("/divide", methods=["POST"])
def divide():
    app.logger.info("/divide called")

    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if a is None or b is None:
        raise InvalidUsage("Both 'a' and 'b' are required")

    if b == 0:
        raise InvalidUsage("Cannot divide by zero")

    result = a / b
    app.logger.info(f"Result: {result}")
    return jsonify({"result": result})

# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
