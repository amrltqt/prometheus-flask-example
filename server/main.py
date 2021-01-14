import os
from flask import Flask, render_template, redirect
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/buy')
def buy():
    return redirect('/')

if __name__ == "__main__":
    app.run(host=os.environ["APP_HOST"], port=os.environ["APP_PORT"])