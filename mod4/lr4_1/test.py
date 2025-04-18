from flask import Flask
from flask_wtf import FlaskForm
from wtforms.fields.numeric import *
from wtforms.fields.simple import *
from wtforms.validators import InputRequired, Email, NumberRange, Optional

app = Flask(__name__)


class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField(validators=[Optional()])


@app.route('/registration', methods=['POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f'Успешно зарегестрирован пользователь {email} с номером телеофна +7{phone} '

    return f'invalid input{form.errors}', 400


if __name__ == '__main__':
    app.run(debug=True)