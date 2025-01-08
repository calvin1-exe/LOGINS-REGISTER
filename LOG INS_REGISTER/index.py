from flask import Flask
from website import create_app

app = create_app()

@app.route('/')
def home():
    return "Hello from Flask!"

# Vercel requires this
app.debug = True 