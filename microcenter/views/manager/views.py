from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required

route = Blueprint('manager', __name__)
