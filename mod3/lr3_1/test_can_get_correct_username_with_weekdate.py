from flask import Flask
from datetime import datetime
from freezegun import freeze_time

app = Flask(__name__)

weekdays_tuple = (
    "Хорошего понедельника",
    "Хорошего вторника",
    "Хорошей среды",
    "Хорошего четверга",
    "Хорошей пятницы",
    "Хорошей субботы",
    "Хорошего воскресенья"
)

WEEKDAY_GREETINGS = weekdays_tuple

@app.route('/hello_world/<name>')
def hello_world(name):
    weekday_num = datetime.today().weekday()
    greeting = WEEKDAY_GREETINGS[weekday_num]
    return f"Привет, {name}. {greeting}!"

def get_weekday_greeting(day):
    return WEEKDAY_GREETINGS[day]


def test_can_get_correct_username_with_weekday():
    with freeze_time("2024-03-04"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошего понедельника"

    with freeze_time("2024-03-05"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошего вторника"

    with freeze_time("2024-03-06"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошей среды"

    with freeze_time("2024-03-07"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошего четверга"

    with freeze_time("2024-03-08"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошей пятницы"

    with freeze_time("2024-03-09"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошей субботы"

    with freeze_time("2024-03-10"):
        assert get_weekday_greeting(datetime.today().weekday()) == "Хорошего воскресенья"

def test_handles_weekday_in_username():
    with freeze_time("2024-03-06"):
        assert hello_world("Хорошей среды") == "Привет, Хорошей среды. Хорошей среды!"

if __name__ == '__main__':
    app.run(debug=True)