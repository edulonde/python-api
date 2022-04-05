from flask import Blueprint, render_template

blueprint = Blueprint("sobre", __name__)


@blueprint.route('/sobre')
def show_page_sobre():
    return render_template('sobre.html')
