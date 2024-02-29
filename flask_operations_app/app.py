from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/operation", methods=["POST"])
def op_numbers():
    data = request.get_json()
    op = data.get("operation", "sum")
    a = data.get("a")
    b = data.get("b")
    if op == "sum":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        result = a / b
    else:
        return jsonify({"error": "Invalid operation"}), 200
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
