import datetime

from flask import Blueprint, render_template

blueprint = Blueprint("funcionalidades", __name__)


@blueprint.route('/funcionalidades')
def show_page_funcionalidades():
    hora = datetime.datetime.now()
    return render_template('funcionalidades.html', hora=hora)

