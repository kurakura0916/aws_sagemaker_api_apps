from flask import Flask, render_template, request

from lib.categorical_classifier import categorical_classifier

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        data = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width
        }

        responses = categorical_classifier(data)
        result = responses["body"]

        return render_template("prediction.html", result=result)

    elif request.method == "GET":
        return render_template("index.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
