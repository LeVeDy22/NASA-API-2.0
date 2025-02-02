from flask import Flask, render_template, request
from get_result import get_data


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("get_data.html")


@app.route("/result_json", methods=["POST"])
def result_json():
    date = request.form.get("date")
    try:
        return get_data(date=date)
    except ValueError:
        return "Error"

if __name__ == "__main__":
    app.run(debug=True)
