from flask import Flask, render_template

from blueprint.sobre import blueprint as sobre
from blueprint.funcionalidades import blueprint as funcionalidades
from blueprint.blog import blueprint as blog

app = Flask(__name__)

app.register_blueprint(sobre)
app.register_blueprint(funcionalidades)
app.register_blueprint(blog)


@app.route('/')
def show_page_index():
    return render_template('index.html')



