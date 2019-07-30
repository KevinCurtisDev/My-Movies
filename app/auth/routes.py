from flask import render_template, url_for, request
from app.auth.forms import RegistrationForm
from app.auth import authentication as at


@at.route('/register')
def register_user():
    form = RegistrationForm()
    return render_template('register.html', form=form)