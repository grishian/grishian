import sys
from app import create_app, db
#vergeet hier de blueprints voor de models niet


sys.dont_write_bytecode = True
app = create_app()

#vergeet hier de shellcontext niet


if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')
