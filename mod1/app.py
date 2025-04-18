import random
from flask import Flask
from datetime import datetime, timedelta
import os
import re

app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
visits = 0
time_format = '%d.%m.%Y %H:%M:%S'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as book:
        text = book.read()
        return re.findall(r'\b\w+\b', text)

words = get_words_from_file(BOOK_FILE)

@app.route('/hello_world')
def hello():
    return "Привет, мир!"

@app.route('/cars')
def show_cars():
    return ", ".join(cars)

@app.route('/cats')
def random_cat():
    return random.choice(cats)

@app.route('/get_time/now')
def time_now():
    return f"Точное время и дата: {datetime.now().strftime(time_format)}"

@app.route('/get_time/future')
def time_future():
    return f"Время через час: {(datetime.now() + timedelta(hours=1)).strftime(time_format)}"

@app.route('/get_random_word')
def get_random_word():
    return random.choice(words)

@app.route('/counter')
def counter():
    global visits
    visits += 1
    return f"Страница открыта {visits} раз"

if __name__ == "__main__":
    app.run()