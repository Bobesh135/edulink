from flask import Flask, render_template

app = Flask(__name__)

# Hlavní stránka (beze změny)
@app.route("/")
def hlavni_stranka():
    return render_template("index.html")

# NOVÁ STRÁNKA: Výběr role
@app.route("/vyber-role")
def vyber_role():
    return render_template("role_selection.html")

# NOVÁ STRÁNKA: Registrace učitele (nastavení rozvrhu)
@app.route("/registrace/ucitel/rozvrh")
def registrace_ucitel_rozvrh():
    return render_template("registrace_rozvrh_ucitel.html")

# Zástupné stránky pro ostatní kroky (zatím jen text)
@app.route("/registrace/vyber-skoly")
def vyber_skoly():
    return "Tady bude stránka pro výběr školy textem nebo na mapě."

@app.route("/registrace/rodic/hledej-dite")
def hledej_dite():
    return "Tady bude stránka pro vyhledání dítěte."
    
@app.route("/registrace/reditel/registrace-skoly")
def registrace_skoly():
    return "Tady bude stránka pro registraci školy (jméno, logo)."

# Původní registrační formulář
@app.route("/registrace-formular")
def registrace_formular():
    return render_template("register.html")