from flask import Blueprint, redirect, render_template, url_for, request

dash = Blueprint('dash', __name__,
                 static_folder='../../web/static',
                 template_folder='../../web/dash',
                 url_prefix='/dash')


@dash.route('/', methods=['GET', 'POST'])
def home():
    return render_template('dash_home.html')
