from flask_wtf import FlaskForm  # type: ignore
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
    )
    submit = SubmitField(
        label="Login",
    )
