from flask import Blueprint, redirect, render_template, url_for, request

site = Blueprint('site', __name__, template_folder='../../web/site')


@site.route('/', methods=['GET'])
def home():
    return render_template('site_home.html')
