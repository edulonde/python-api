from flask import Blueprint, render_template

blueprint = Blueprint("funcionalidades", __name__)


@blueprint.route('/funcionalidades')
def show_page_funcionalidades():
    return render_template('funcionalidades.html')