from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Hola, Toluca!\r\n", 200, { 'Content-Type': 'text/plain' }

if __name__ == '__main__':
    application.run(debug = True)
