from flask import Flask
from datetime import datetime
import sys
import os

app = Flask(__name__)

# Варианты хранения дней недели
weekdays_tuple = (
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья"
)

weekdays_list = [
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья"
]

weekdays_dict = {
    0: "Хорошего понедельника",
    1: "Хорошего вторника",
    2: "Хорошей среды",
    3: "Хорошего четверга",
    4: "Хорошей пятницы",
    5: "Хорошей субботы",
    6: "Хорошего воскресенья"
}

# Сравнение занимаемой памяти
if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
    print(f"Кортеж: {sys.getsizeof(weekdays_tuple)} байт")
    print(f"Список: {sys.getsizeof(weekdays_list)} байт")
    print(f"Словарь: {sys.getsizeof(weekdays_dict)} байт")

WEEKDAY_GREETINGS = weekdays_tuple

@app.route('/hello-world/<name>')
def hello_world_route(name):
    weekday_num = datetime.today().weekday()
    greeting = WEEKDAY_GREETINGS[weekday_num]
    return f"Привет, {name}. {greeting}!"

if __name__ == '__main__':
    app.run(debug=True)