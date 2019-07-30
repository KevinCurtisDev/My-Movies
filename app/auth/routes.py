from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required,  current_user
from app.auth.forms import RegistrationForm
from app.auth.forms import LoginForm
from app.auth import authentication as at
from app.auth.models import User


@at.route('/register', methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.email.data,
            password=form.password.data)
        flash('Registration Successful')
        return redirect(url_for('authentication.signin_user'))
    return render_template('register.html', form=form)


@at.route('/login', methods=['GET', 'POST'])
def signin_user():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(user_email=login_form.email.data).first()
        if not user or not user.check_password(login_form.password.data):
            flash('Invalid login, try again')
            return redirect(url_for('authentication.signin_user'))

        login_user(user, login_form.stay_loggedin.data)
        return redirect(url_for('main.index'))
    return render_template('login.html', login_form=login_form)

@at.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.index'))