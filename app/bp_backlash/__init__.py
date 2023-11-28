from flask import Blueprint

bp_backlash = Blueprint('bp_backlash', __name__, cli_group="backlash")

from . import views_backlash
