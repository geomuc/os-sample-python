from flask import Flask
from flask import render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Auskunft Blutgruppen für Vampire!"

@application.route('/auskunft')
def auskunft():
    name= "Markus"
    return render_template('auskunft.html', name=name)

if __name__ == "__main__":
    application.run()
