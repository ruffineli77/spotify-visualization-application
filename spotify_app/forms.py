
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class ContactForm(FlaskForm):
    email = StringField("Email",
                        validators=[DataRequired(), Email()])
    name = StringField("Your name",
                             validators=[DataRequired()])
    content = TextAreaField("Reason for contact",
                             validators=[DataRequired()])
    submit = SubmitField("Send contact information")


# Ill just use regular html forms for now.
