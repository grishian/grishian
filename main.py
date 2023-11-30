import sys
from app import create_app, db
from app.bp_user.model_user import User
from app.bp_backlash.model_backlash import Shimming
#vergeet hier de blueprints voor de models niet


sys.dont_write_bytecode = True
app = create_app()

#vergeet hier de shellcontext niet
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Shimming': Shimming}


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
