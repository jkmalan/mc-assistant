from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from app.main.models import  User
from app.main.forms import SigninForm, SignupForm

site = Blueprint('site', __name__, template_folder='../../web/site')


@site.route('/', methods=['GET'])
def home():
    return render_template('site_home.html')


@site.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('dash.home'))

    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.password != form.password.data:
            return redirect(url_for('site.signin'))

        session_count = user.session_count + 1
        user.update(session_login=True, session_count=session_count)
        login_user(user, remember=form.remember.data)

        navigate = request.args.get('next')
        if not navigate:
            navigate = url_for('dash.home')

        return redirect(navigate)
    return render_template('site_signin.html', form=form)


@site.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('dash.home'))

    form = SignupForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    password=form.password.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    phone=form.phone.data)
        user.create()

        return redirect(url_for('site.signin'))
    return render_template('site_signup.html', form=form)


@site.route('/signout', methods=['GET'])
@login_required
def signout():
    user = User.query.find_one(current_user.uuid)

    session_login = user.session_login
    session_count = user.session_count - 1
    if session_count == 0:
        session_login = False
    user.update(session_login=session_login, session_count=session_count)
    logout_user()

    return render_template('site_signout.html')
