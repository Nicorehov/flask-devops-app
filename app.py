from flask import Flask, render_template
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)