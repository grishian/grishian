from flask import render_template
from app.bp_backlash import bp_backlash
#from app.bp_user.model_user import User


@bp_backlash.route('/backlash')
def do_backlash():

    return render_template('backlash/backlash.html', title='Backlash')
