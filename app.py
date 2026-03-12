from flask import Flask, render_template, request
import os
from predict import predict_image

app = Flask(__name__)

UPLOAD_FOLDER = "static"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["file"]

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)

    file.save(filepath)

    label, confidence = predict_image(filepath)

    return render_template("result.html",
                           prediction=label,
                           confidence=confidence,
                           image=filepath)


if __name__ == "__main__":
    app.run(debug=True)