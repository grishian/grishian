import sys
from app import create_app, db
from app.bp_general.models import User
#vergeet hier de blueprints voor de models niet


sys.dont_write_bytecode = True
app = create_app()

#vergeet hier de shellcontext niet
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
