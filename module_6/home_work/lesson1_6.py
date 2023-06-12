from flask import Flask, render_template


app = Flask(__name__)


@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


@app.errorhandler(404)
def handle_404(e: 404):
    links = []
    for rule in app.url_map.iter_rules():
        links.append((rule, rule.endpoint))
    return render_template("all_links.html", links=links)


if __name__ == '__main__':
    app.run(debug=True)
