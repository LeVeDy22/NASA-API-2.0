from get_result import get_data
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    result_json = get_data("2025-02-02")
    return result_json

if __name__ == "__main__":
    app.run(debug=True)
