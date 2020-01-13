from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user

from microcenter.core import permission
from microcenter.models.users import User

route = Blueprint('associate', __name__)


@route.route('/', methods=['GET', 'POST'])
@route.route('/home', methods=['GET', 'POST'])
@permission(roles=['associate', 'manager'])
def home():
    return render_template('associate/home.html')


@route.route('/signout', methods=['GET'])
@permission(roles=['associate', 'manager'])
def signout():
    user = User.query.get(current_user.uuid)

    session_login = user.session_login
    session_count = user.session_count - 1
    if session_count == 0:
        session_login = False
    user.update(session_login=session_login, session_count=session_count)
    logout_user()

    return render_template('associate/signout.html')


@route.route('/account', methods=['GET', 'POST'])
@permission(roles=['associate', 'manager'])
def account():
    return render_template('associate/account.html')
