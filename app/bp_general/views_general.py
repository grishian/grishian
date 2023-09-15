from flask import render_template
from app.bp_general import bp_general

@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    return render_template('general/home.html', title='Home')

