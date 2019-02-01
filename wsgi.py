from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Auskunft Blutgruppen für Vampire!"

@application.route('/auskunft')
def auskunft():
    user = {'person': 'Miguel'}
    return '''
<html>
    <head>
        <title>Blutgruppenauskunft</title>
    </head>
    <body>
        <h1>Hello, ''' + user['person'] + '''!</h1>
    </body>
</html>'''

if __name__ == "__main__":
    application.run()
