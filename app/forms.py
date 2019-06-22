from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, BooleanField, SubmitField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, regexp
from wtforms.fields.html5 import TelField



class Addcard(FlaskForm):
    character= StringField('Персонаж', validators=[DataRequired()])
    xml= FileField('XML-файл', validators=[DataRequired()])
    submit= SubmitField('Сохранить')
