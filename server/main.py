import os
from flask import Flask, render_template, redirect
from flask.globals import request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')

buying = metrics.counter(
    'buy_request', 'A user have buyed the product',
    labels={'status': lambda r: r.status_code, 'path': lambda: request.path}
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buy/<product_id>')
@buying
def buy(product_id=''):
    return redirect('/')

if __name__ == "__main__":
    app.run(host=os.environ["APP_HOST"], port=os.environ["APP_PORT"])