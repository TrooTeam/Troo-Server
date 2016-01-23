import os
import json
from flask import Flask, request, jsonify


webapp = Flask(__name__)


@webapp.route("/api/log_review")
def log_review():
    review = request.get_json()
    print(review)
    return jsonify({})


@webapp.route("/api/handle_query")
def handle_query():
    query = request.get_json()
    print(query)
    return jsonify({})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    webapp.run(host='0.0.0.0', port=port, debug=True)
