from flask import Flask
from jinja2 import Template

app = Flask(__name__)

# Přidal jsem pár žáků, ať je stránka plnější
data_zaku = {
    "studenti": [
        {"id": 1, "jmeno": "Petr Novák", "znamky": [1, 2, 1, 3]},
        {"id": 2, "jmeno": "Jana Svobodová", "znamky": [3, 2, 2]},
        {"id": 3, "jmeno": "Tomáš Marek", "znamky": [1, 1, 1, 1, 2]},
        {"id": 4, "jmeno": "Alena Veselá", "znamky": [2, 1, 2, 1]},
        {"id": 5, "jmeno": "Lukáš Dvořák", "znamky": [1, 3, 2]},
    ]
}

# --- ZDE JE TVŮJ DESIGN Z FIGMY PŘEVEDENÝ DO KÓDU ---
html_sablona = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Edulink</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

    <style>
        /* Základní nastavení podle tvého designu */
        body {
            font-family: 'Inter', sans-serif; /* Písmo z Figmy */
            background-color: #1E1E1E; /* Tmavé pozadí */
            color: #FFFFFF; /* Bílý text jako základ */
            margin: 0;
            padding: 2em;
        }

        /* Kontejner pro vycentrování obsahu */
        .container {
            max-width: 800px;
            margin: 0 auto;
        }

        /* Hlavní nadpis "Edulink" */
        h1 {
            font-size: 48px; /* Velikost z Figmy */
            font-weight: 600; /* Tloušťka písma */
            text-align: center;
            margin-bottom: 1.5em; /* Větší mezera pod nadpisem */
        }

        /* Kartička pro jednoho žáka */
        .zak {
            background-color: #2D2D2D; /* Barva karty z Figmy */
            border-radius: 10px;      /* Zakulacení rohů z Figmy */
            padding: 25px;
            margin-bottom: 20px;
            /* Modrý stín/záře podle tvého návrhu */
            box-shadow: 0px 0px 15px rgba(0, 119, 255, 0.5);
            border: 1px solid #3A3A3A; /* Jemný okraj */
        }

        /* Jméno žáka */
        .jmeno {
            font-size: 20px;
            font-weight: 600;
            margin-bottom: 10px;
        }

        /* Známky */
        .znamky {
            font-size: 16px;
            color: #AAAAAA; /* Světle šedá pro známky z Figmy */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Edulink</h1>
        
        {% for zak in data["studenti"] %}
            <div class="zak">
                <div class="jmeno">{{ zak.jmeno }}</div>
                <div class="znamky">Známky: {{ zak.znamky | join(', ') }}</div>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def hlavni_stranka():
    template = Template(html_sablona)
    return template.render(data=data_zaku)