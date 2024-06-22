from app import db
from app.bp_user import bp_user
from app.bp_user.model_user import User
from flask import render_template, flash, redirect, url_for, abort, request
from sqlalchemy import desc, asc


@bp_user.route('/register', methods=['GET', 'POST'])
def do_register():
    if request.method == 'POST':
        username = request.form.get('input_username')


        user = User()
        user.username = username

        db.session.add(user)
        db.session.commit()
        flash('Account created.', 'OK')
        return redirect(url_for('bp_general.do_home'))


    return render_template('user/register.html', title='Registreer')

@bp_user.route('/user_list')
def do_user_list():
    users = User.query.order_by(asc(User.id)).all()
    return render_template('user/user_list.html', users=users, title='Gebruiker Lijst')



