from typing import Optional as Opt
from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields.core import Field
from wtforms.fields.numeric import *
from wtforms.fields.simple import *
from wtforms.validators import InputRequired, Email, Optional, ValidationError

app = Flask(__name__)


def number_length(min: int = 0, max: int = 0, message: Opt[str] = None):

    if not message:
        message = 'Число должно быть неотрицательным, а длина - находиться в пределах указанного диапазона'

    def _number_length(form: FlaskForm, field: Field):
        if field.data is not None and len(str(field.data)) < min or len(str(field.data)) > max:
            raise ValidationError(message)

    return _number_length


class NumberLength:
    def init(self, min: int = 0, max: int = 0, message: Opt[str] = None):
        self.min = min
        self.max = max
        self.message = message or 'Число должно быть неотрицательным, а длина - находиться в пределах указанного диапазона'

    def call(self, form: FlaskForm, field: Field):
        if not self.message:
            self.message = 'Число должно быть неотрицательным, а длина - находиться в пределах указанного диапазона'

        if field.data is not None and len(str(field.data)) < self.min or len(str(field.data)) > self.max:
            raise ValidationError(self.message)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(min=10, max=10)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'Успешно зарегестрирован пользователь с {email} используя телефон +7{phone} '

    return f'Неправильнный ввод{form.errors}', 400


if __name__ == '__main__':
    app.run(debug=True)