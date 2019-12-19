from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

dash = Blueprint('dash', __name__, template_folder='../../web/dash', url_prefix='/dash')


@dash.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template('dash_home.html')
