from flask import render_template
from app.bp_general import bp_general
from app.bp_general.models import User

@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    return render_template('general/home.html', title='Home')




