from app import db
from flask import render_template, flash, redirect, url_for, abort, request
from app.bp_backlash import bp_backlash
from app.bp_user.model_user import User


@bp_backlash.route('/backlash', methods=['GET', 'POST'])
def do_backlash():

    if request.method == "POST":

        #front1 = request.form.get('input_voorkant')
        

        return redirect('https://media.tenor.com/o656qFKDzeUAAAAC/rick-astley-never-gonna-give-you-up.gif')
        

    return render_template('backlash/backlash.html', title='Backlash')


