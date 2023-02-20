from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, BooleanField
from wtforms.validators import DataRequired,Email

class LoginForm(FlaskForm):
  username = StringField('username', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])

class EmailPasswordForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])

TodoForm = [
  {"title": "Collector",
       "author": "Fauls",
       "date": 1985,
       "pages": 352
  },
  {"title": "Pride and Prejudice",
      "author": "Austean",
      "date": 1876,
      "pages": 456
   },
   {"title": "Lightning",
    "author": "King",
    "date": 1992,
    "pages": 432
  }
]