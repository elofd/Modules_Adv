from flask import Flask


app = Flask(__name__)


@app.endpoint('test')
def tes_endpoint():
    return 'Test endpoint was called'


if __name__ == '__main__':
    app.run()
