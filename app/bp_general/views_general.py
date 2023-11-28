from flask import render_template
from app.bp_general import bp_general
from app.bp_user.model_user import User

@bp_general.route('/')
@bp_general.route('/index')
def do_home():
    users = User.query.all()

    return render_template('general/home.html', title='Home', users=users)




