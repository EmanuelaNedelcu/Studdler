from flask import Flask

app = Flask(__name__)

@pp.route('/')
def server():
    return "Hello from Studdler"

if __name__ == '__main__':
    app.run()

