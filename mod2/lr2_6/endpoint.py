import os

from flask import Flask

app = Flask(__name__)


@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str) -> str:
    abs_path = os.path.abspath(relative_path)
    with open(abs_path, "r", encoding="utf-8") as file:
        text = file.read(size)
        result_size = len(file.read())
    return (f'Путь до файла: <b>{abs_path}</b> Количество символов в файле:'
            f' {result_size}<br>Первые {size} символов файла: {text}')


if __name__ == "__main__":
    app.run(debug=True)