from flask import Flask
from jinja2 import Template

app = Flask(__name__)

html_sablona = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Edulink</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Itim&family=K2D:wght@400;800&display=swap" rel="stylesheet">
    
    <style>
        body {
            margin: 0;
            padding: 0;
            min-height: 100vh;
            color: white;
            position: relative;
            overflow: hidden;
            display: flex; /* Pomůže s zarovnáním */
        }

        /* Pozadí s tvým obrázkem a překrytím */
        .background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            /* ZDE JE VLOŽENÝ TVŮJ ODKAZ NA POZADÍ */
            background-image: url('https://i.postimg.cc/mkgf4rdr/Mask-group-11.png');
            background-size: cover;
            background-position: center;
            filter: brightness(0.9); /* Lehce ztmavíme, aby vynikl text */
            z-index: -1;
        }

        /* Horní lišta - vycentrovaná */
        .top-bar {
            position: absolute;
            top: 40px;
            left: 50%; /* Posuneme o 50% šířky obrazovky */
            transform: translateX(-50%); /* Vrátíme o 50% vlastní šířky - tím se vycentruje */
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 10px;
            display: flex;
            align-items: center; /* Zarovná položky vertikálně na střed */
            gap: 15px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
            font-family: 'Itim', cursive; /* Font z tvého návrhu */
            font-size: 18px;
        }

        .top-bar a {
            text-decoration: none;
            color: #333;
            padding: 8px 15px;
        }
        
        /* Ikonka uprostřed menu */
        .menu-icon {
            height: 35px; /* Uprav velikost podle potřeby */
            display: block;
        }

        /* Hlavní obsah - vlevo dole */
        .main-content {
            position: absolute;
            bottom: 60px;
            left: 80px;
            z-index: 1;
        }

        .main-content h1 {
            font-family: 'K2D', sans-serif; /* Font z tvého návrhu */
            font-size: 5em;
            font-weight: 800; /* Extra tučné */
            margin: 0;
            line-height: 1;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }

        .main-content p {
            font-family: 'K2D', sans-serif;
            font-size: 1.6em;
            font-weight: 400;
            margin: 10px 0 0 5px; /* Malé odsazení od hlavního nadpisu */
            color: rgba(255, 255, 255, 0.9);
            text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
        }

        /* Úpravy pro menší obrazovky */
        @media (max-width: 768px) {
            .main-content {
                left: 40px;
                bottom: 40px;
            }
            .main-content h1 { font-size: 3.5em; }
            .main-content p { font-size: 1.2em; }
            .top-bar { top: 20px; }
        }
    </style>
</head>
<body>
    <div class="background-image"></div>

    <div class="top-bar">
        <a href="#">Registrovat</a>
        <img src="https://i.postimg.cc/XJ8St5gX/Chat-GPT-Image-18-10-2025-22-42-10-1.png" class="menu-icon" alt="logo">
        <a href="#">Přihlásit</a>
    </div>

    <div class="main-content">
        <h1>Edulink</h1>
        <p>Přehledná aplikace, kde všichni vidí vše</p>
    </div>

</body>
</html>
"""

@app.route("/")
def hlavni_stranka():
    template = Template(html_sablona)
    return template.render()