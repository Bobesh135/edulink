from flask import Flask
from jinja2 import Template

app = Flask(__name__)

# --- TOTO BUDE NOVÁ HTML ŠABLONA PRO ÚVODNÍ STRÁNKU ---
html_sablona = """
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>Edulink</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    
    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
            position: relative;
            overflow: hidden; /* Skryje případné přesahy obrázku */
        }

        /* Pozadí s obrázkem a překrytím */
        .background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://images.unsplash.com/photo-1546410531-bb443e990924?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80');
            background-size: cover;
            background-position: center;
            filter: brightness(0.7); /* Ztmaví obrázek jako na návrhu */
            z-index: -2; /* Posune pod ostatní obsah */
        }

        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(to bottom, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.5) 100%); /* Jemný gradient odshora dolů */
            z-index: -1;
        }

        /* Horní lišta s tlačítky */
        .top-bar {
            position: absolute;
            top: 30px; /* Mezera odshora */
            right: 50px; /* Mezera zprava */
            background-color: rgba(255, 255, 255, 0.9); /* Lehce průhledné pozadí */
            border-radius: 10px;
            padding: 10px 20px;
            display: flex;
            gap: 20px; /* Mezera mezi tlačítky */
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        }

        .top-bar a {
            text-decoration: none;
            color: #333;
            font-weight: 600;
            padding: 8px 15px;
            border-radius: 8px;
            transition: background-color 0.3s;
            display: flex;
            align-items: center;
        }

        .top-bar a:hover {
            background-color: #e0e0e0;
        }
        
        .top-bar a i {
            margin-right: 8px; /* Mezera mezi ikonou a textem */
            color: #1877f2; /* Modrá ikona */
        }

        /* Hlavní obsah uprostřed */
        .main-content {
            text-align: center;
            z-index: 1; /* Zajistí, že je nad obrázkem */
            padding: 20px; /* Odsazení pro mobily */
        }

        .main-content h1 {
            font-size: 4.5em; /* Velké písmo jako na návrhu */
            font-weight: 800; /* Extra tučné */
            margin-bottom: 0.1em;
            color: white;
            text-shadow: 2px 2px 8px rgba(0,0,0,0.5); /* Jemný stín pro čitelnost */
        }

        .main-content p {
            font-size: 1.5em; /* Velikost podnadpisu */
            font-weight: 400;
            max-width: 600px;
            line-height: 1.4;
            color: rgba(255, 255, 255, 0.9);
            text-shadow: 1px 1px 5px rgba(0,0,0,0.3);
        }

        /* Responsivní úpravy pro menší obrazovky */
        @media (max-width: 768px) {
            .top-bar {
                top: 20px;
                right: 20px;
                padding: 5px 10px;
                gap: 10px;
            }
            .top-bar a {
                padding: 5px 10px;
                font-size: 0.9em;
            }
            .main-content h1 {
                font-size: 3em;
            }
            .main-content p {
                font-size: 1.2em;
            }
        }

        @media (max-width: 480px) {
            .top-bar {
                flex-direction: column; /* Tlačítka pod sebou na malých mobilech */
                right: 10px;
                top: 10px;
            }
            .top-bar a {
                justify-content: center;
            }
            .main-content h1 {
                font-size: 2.2em;
            }
            .main-content p {
                font-size: 1em;
            }
        }

    </style>
</head>
<body>
    <div class="background-image"></div>
    <div class="overlay"></div>

    <div class="top-bar">
        <a href="#"><i class="fas fa-user-plus"></i> Registrovat</a>
        <a href="#"><i class="fas fa-sign-in-alt"></i> Přihlásit</a>
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
    return template.render() # Tentokrát nic nepřidáváme, data nejsou potřeba