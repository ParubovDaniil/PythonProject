from flask import Flask

app = Flask(__name__)

@app.route("/max_number/<path:numbers>")
def max_number(numbers: str) -> str:
    number = max([int(item) for item in numbers.split('/')])
    return f"Max : <i>{number}</i>"

if __name__ == "__main__":
    app.run(debug=True)