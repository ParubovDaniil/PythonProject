from flask import Flask

app = Flask(__name__)

storage = {}

@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])

    storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number

    return f"Добавлена трата {number} руб. за {day}.{month}.{year}"

@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    if year not in storage:
        return f"Нет данных за {year} год"

    total = sum(
        sum(day_values.values())
        for month_values in storage[year].values()
        for day_values in [month_values]  # Для читаемости
    )
    return f"Суммарные траты за {year} год: {total} руб."

@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    if year not in storage or month not in storage[year]:
        return f"Нет данных за {month}.{year}"

    total = sum(storage[year][month].values())
    return f"Суммарные траты за {month}.{year}: {total} руб."

if __name__ == "__main__":
    app.run(debug=True)