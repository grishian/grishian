from flask import Flask, render_template, request, g
import sqlite3

from app.bp_general import bp_general
from app.bp_user.model_user import User

@bp_general.route('/')
@bp_general.route('/index')
def do_home():

    return render_template('general/home.html', title='Home')







