from flask import Flask
from website import create_app

app = create_app()

@app.route('/')
def home():
    return "Flask app is running!"

if __name__ == '__main__':
    app.run() 