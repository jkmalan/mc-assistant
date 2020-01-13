from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

from microcenter.models.users import User, UserRole
from microcenter.forms.forms import SigninForm, SignupForm

route = Blueprint('anonymous', __name__)


@route.route('/', methods=['GET'])
def home():
    return render_template('anonymous/home.html')


@route.route('/signin', methods=['GET', 'POST'])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for('associate.home'))

    form = SigninForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or user.password != form.password.data:
            return redirect(url_for('anonymous.signin'))

        session_count = user.session_count + 1
        user.update(session_login=True, session_count=session_count)
        login_user(user, remember=form.remember.data)

        navigate = request.args.get('next')
        if not navigate:
            navigate = url_for('associate.home')

        return redirect(navigate)
    return render_template('anonymous/signin.html', form=form)


@route.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('associate.home'))

    form = SignupForm()
    if form.validate_on_submit():
        user = User(email=form.username.data + '@microcenter.com',
                    username=form.username.data,
                    password=form.password.data,
                    firstname=form.firstname.data,
                    lastname=form.lastname.data)
        user.create()
        user.assign(roles=['associate'])

        return redirect(url_for('anonymous.signin'))
    return render_template('anonymous/signup.html', form=form)
