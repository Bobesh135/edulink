from flask import Flask
from jinja2 import Template # Je lepší to mít nahoře

app = Flask(__name__)

# Data zůstávají stejná
data_zaku = {
    "studenti": [
        {"id": 1, "jmeno": "Petr Novák", "znamky": [1, 2, 1, 3]},
        {"id": 2, "jmeno": "Jana Svobodová", "znamky": [3, 2, 2]},
        {"id": 3, "jmeno": "Tomáš Marek", "znamky": [1, 1, 1, 1, 2]},
        {"id": 4, "jmeno": "Alena Veselá", "znamky": [2, 1, 2, 1]},
    ]
}

# --- ZDE JE NOVÝ VZHLED ---
html_sablona = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Edulink ✨</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

    <style>
        /* Základní nastavení pro celou stránku */
        body {
            font-family: 'Poppins', sans-serif; /* Použijeme nové písmo */
            background-color: #f0f2f5; /* Světle šedé pozadí */
            color: #333;
            margin: 0;
            padding: 2em;
        }

        /* Kontejner pro vycentrování obsahu */
        .container {
            max-width: 800px;
            margin: 0 auto; /* Automaticky vycentruje */
        }

        /* Hlavní nadpis */
        h1 {
            color: #1877f2; /* Modrá barva */
            font-size: 2.5em; /* Větší písmo */
            text-align: center; /* Vycentrovat */
            margin-bottom: 0.5em;
        }

        /* Kartička pro jednoho žáka */
        .zak {
            background-color: white;
            border-radius: 12px; /* Více zakulacené rohy */
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); /* Jemný stín */
            transition: transform 0.2s; /* Animace při najetí myší */
        }
        
        /* Efekt při najetí myší na kartičku */
        .zak:hover {
            transform: translateY(-5px); /* Lehce se zvedne */
        }

        /* Jméno žáka */
        .jmeno {
            font-size: 1.3em;
            font-weight: 600; /* Tlustší písmo */
            color: #050505;
            margin-bottom: 8px;
        }

        /* Známky */
        .znamky {
            font-size: 1.1em;
            color: #65676b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Edulink</h1>
        
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
