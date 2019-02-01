from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Auskunft Blutgruppen für Vampire!"

@app.route('/auskunft')
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
    app.run()
