from app import db
from flask import render_template, flash, redirect, url_for, abort, request
from app.bp_backlash import bp_backlash
from app.bp_user.model_user import User


@bp_backlash.route('/backlash')
def do_backlash():

    return render_template('backlash/backlash.html', title='Backlash')

@bp_backlash.route('/calculate_backlash', methods=['GET', 'POST'])
def do_calculate_backlash():



    if request.method == "POST":




        return redirect('https://media.tenor.com/o656qFKDzeUAAAAC/rick-astley-never-gonna-give-you-up.gif')
        


    return render_template('backlash/calculate_backlash.html', title='Bereken backlash')


