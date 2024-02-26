from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/sum", methods=["POST"])
def sum_numbers():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")
    result = a + b
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
