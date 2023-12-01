from app import db
from flask import render_template, flash, redirect, url_for, abort, request
from app.bp_backlash import bp_backlash
from app.bp_backlash.model_backlash import Shimming


@bp_backlash.route('/backlash', methods=['GET', 'POST'])
def do_backlash():

    if request.method == "POST":

        pinion_1 = request.form.get('input_voorkant')
        backlash_1 = request.form.get('input_achterkant1')
        backlash_2 = request.form.get('input_achterkant2')
        backlash_3 = request.form.get('input_achterkant3')
        backlash_4 = request.form.get('input_achterkant4')

        pinion_abs_1 = abs(4.5-float(pinion_1))
        pinion_abs_2 = abs(2.6-float(pinion_1))

        if pinion_abs_1 <= pinion_abs_2:
            pinion = 4.5-float(pinion_1)
        else:
            pinion = 2.6-float(pinion_1)


        backlash_values = [backlash_1, backlash_2, backlash_3, backlash_4]

        backlash_good_values = [25, 26, 27, 28, 29, 30, 31, 32, 33]
        backlash_medium_values = [20, 21, 22, 23, 24, 34, 35]
        good_values = []
        medium_values = []
        bad_values = []

        for backlash_value in backlash_values:
            if 35 < int(backlash_value) or int(backlash_value) < 20:
                try:
                    bad_values.append(backlash_value)
                        

                except Exception as e:  # pragma: no cover
                    # if this fails we do not care, but we certainly do not want to block
                    # someone logging in
                    print('Error: {}'.format(e))


        for backlash_value in backlash_values:
            for backlash_good_value in backlash_good_values:
                try:
                    print(int(backlash_value) , int(backlash_good_value))
                    if int(backlash_value) == int(backlash_good_value):
                        print('is good')
                        good_values.append(backlash_value)
                        

                except Exception as e:  # pragma: no cover
                    # if this fails we do not care, but we certainly do not want to block
                    # someone logging in
                    print('Error: {}'.format(e))

        for backlash_value in backlash_values:
            for backlash_medium_value in backlash_medium_values:
                try:

                    if int(backlash_value) == int(backlash_medium_value):
                        print('is medium')
                        medium_values.append(backlash_value)


                except Exception as e:  # pragma: no cover
                    # if this fails we do not care, but we certainly do not want to block
                    # someone logging in
                    print('Error: {}'.format(e))

        
                    
        print('good values:', good_values)
        print('medium values:', medium_values)
        print('bad values:', bad_values)

        print('backlashvalues', backlash_values)

        print('meting: ', pinion_1, 'load: ', pinion)

        return render_template('backlash/backlash_solution.html', meting=pinion_1, load=round(pinion))
        

    return render_template('backlash/backlash.html', title='Backlash')

@bp_backlash.route('/backlash_solution', methods=['GET', 'POST'])
def do_backlash_solution():

    pass

    #return render_template('backlash/backlash.html', title='Backlash')



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



