from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user

from microcenter.core import permission

route = Blueprint('manager', __name__)


@route.route('/', methods=['GET', 'POST'])
@route.route('/home', methods=['GET', 'POST'])
@permission(roles=['manager'])
def home():
    return render_template('manager/home.html')


@route.route('/schedule', methods=['GET', 'POST'])
@permission(roles=['manager'])
def schedule():
    return render_template('manager/schedule.html')
