from flask.app import Flask
from flask.helpers import total_seconds
from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from ..models import Comment, User

class UpdateProfile(FlaskForm):
    username = StringField('Username', validators = [Required(), Length(min = 2, max = 20)])
    email = StringField('Email', validators = [Required(), Email()])
    pic = FileField('Update Profile Picture', validators = [FileAllowed(['png', 'jpg', 'jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationError('Username taken. We like uniqueness.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email = email.data).first()
            if user:
                raise ValidationError('Email taken. We like uniqueness.')

class ResetForm(FlaskForm):
    email = StringField('Email', validators = [Required(), Email()])
    submit = SubmitField('Reset Password')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is None:
            raise ValidationError('Sorry! No such Email. Try Registering, thank you 😄.')

class ResetPassword(FlaskForm):
    password = PasswordField('Password', validators = [Required()])
    confirm_password = PasswordField('Confirm Password', validators = [Required(), EqualTo()])
    submit = SubmitField('Reset Password')

class BlogForm(FlaskForm):
    title = StringField('Title', validators = [Required()])
    body = TextAreaField('Write Something', validators = [Required()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators = [Required()])
    submit = SubmitField('Post')