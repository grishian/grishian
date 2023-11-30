from app import db
from flask import render_template, flash, redirect, url_for, abort, request
from app.bp_backlash import bp_backlash
from app.bp_backlash.model_backlash import Shimming


@bp_backlash.route('/backlash', methods=['GET', 'POST'])
def do_backlash():

    if request.method == "POST":

        #front1 = request.form.get('input_voorkant')
        

        return redirect('https://media.tenor.com/o656qFKDzeUAAAAC/rick-astley-never-gonna-give-you-up.gif')
        

    return render_template('backlash/backlash.html', title='Backlash')


@bp_backlash.route('/add_shimming', methods=['GET', 'POST'])
def do_add_shimmingh():

    if request.method == "POST":

        pinion_value = request.form.get('pinion_value')
        backlash_value = request.form.get('backlash_value')
        shim_left = request.form.get('shim_left')
        shim_right = request.form.get('shim_right')

        shim = Shimming(
            pinion_value=pinion_value,
            backlash_value=backlash_value,
            shim_left=shim_left,
            shim_right=shim_right
        )

        db.session.add(shim)
        db.session.commit()

    shims = Shimming.query.all()
    
        
        

    return render_template('backlash/add_shimming.html', title='add shimming', shims=shims)



