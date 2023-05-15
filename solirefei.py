from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/identifique')
def identifique():
    return render_template('identifique.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == "__main__":
    app.run(debug=True)