import os 
import preprocessing as pre
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)
app.secret_key = 'very-secret-key'

@app.route('/')
def index():
    p = pre.Preprocessing()
    plt = p.get_missing_values_plot()
    plt.savefig('static/img/missing_values.png')

    return render_template("index.html", name="missing_values.png")

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), '/img/icon.png')


if __name__ == '__main__':
   app.run(debug = True)