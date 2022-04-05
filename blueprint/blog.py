from flask import Blueprint, render_template

blueprint = Blueprint("blog", __name__)


@blueprint.route('/blog')
def show_page_blog():
    return render_template('blog.html')