from flask import Flask, render_template

app = Flask(__name__)

# Trasa pro hlavní stránku
@app.route("/")
def hlavni_stranka():
    # Zobrazí soubor 'index.html' ze složky 'templates'
    return render_template("index.html")

# Nová trasa pro registrační stránku
@app.route("/register")
def registrace():
    # Zobrazí soubor 'register.html' ze složky 'templates'
    return render_template("register.html")