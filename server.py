from flask import Flask, request, jsonify
from werkzeug import secure_filename
import random

app = Flask(__name__)


@app.route('/result557578', methods=["POST"])
def load_file():
    if request.method == "POST":
        file = request.files["file"]
        if bool(file.filename):
            filename = secure_filename(file.filename)
            file.save(filename)
            data = jsonify({"res": str(random.randint(1, 3))})
            print(23)
            return data


if __name__ == '__main__':
    app.run(host='0.0.0.0')
