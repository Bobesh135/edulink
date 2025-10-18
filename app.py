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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    
    <style>
        html {
            scroll-behavior: smooth; /* Plynulé scrollování */
        }

        body {
            margin: 0;
            padding: 0;
            color: #002B55; 
            background-color: #1E1E1E; /* Základní barva pro novou sekci */
        }
        
        /* === ÚVODNÍ SEKCE (HERO) === */

        .hero-section {
            min-height: 100vh; /* Zajistí, že úvodní sekce zabere celou obrazovku */
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: flex-end; /* Zarovná obsah dolů */
            justify-content: flex-start; /* Zarovná obsah doleva */
            padding: 60px 80px;
            box-sizing: border-box;
        }

        .background-image {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://i.postimg.cc/mkgf4rdr/Mask-group-11.png');
            background-size: cover;
            background-position: center;
            filter: brightness(0.65); 
            z-index: 1;
        }

        .top-bar {
            position: absolute;
            top: 40px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: 20px; 
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 25px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
            font-family: 'Itim', cursive;
            font-size: 22px;
            z-index: 2; /* Musí být nad pozadím */
        }

        .top-bar a {
            text-decoration: none;
            color: #002B55; 
            padding: 8px 15px;
        }
        
        .menu-icon {
            height: 45px;
            display: block;
        }

        .main-content {
            position: relative; /* Změna z absolute */
            z-index: 2;
        }

        .main-content h1 {
            font-family: 'K2D', sans-serif;
            font-size: 5em;
            font-weight: 800;
            margin: 0;
            line-height: 1;
            color: #002B55;
        }

        .main-content p {
            font-family: 'K2D', sans-serif;
            font-size: 1.6em;
            font-weight: 400;
            margin: 10px 0 0 5px;
            color: #002B55;
        }
        
        /* === NOVÁ SEKCE "VÝHODY" === */

        .features-section {
            padding: 80px 40px; /* Vnitřní odsazení sekce */
            text-align: center;
            background-color: #1E1E1E; /* Tmavé pozadí z tvého prvního designu */
        }

        .features-section h2 {
            font-family: 'K2D', sans-serif;
            font-size: 3em;
            color: #FFFFFF;
            margin-bottom: 60px;
        }

        .features-grid {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap; /* Pokud se nevejdou, zalamují se pod sebe */
            max-width: 1200px;
            margin: 0 auto;
        }

        .feature-card {
            background-color: #2D2D2D;
            border-radius: 15px;
            padding: 30px;
            flex-basis: 300px; /* Základní šířka karty */
            flex-grow: 1; /* Karty se roztáhnou, aby vyplnily místo */
            color: #FFFFFF;
            border: 1px solid #3A3A3A;
            box-shadow: 0px 0px 15px rgba(0, 119, 255, 0.1);
        }
        
        .feature-card i {
            font-size: 3em; /* Velikost ikony */
            color: #0077ff; /* Modrá barva pro ikony */
            margin-bottom: 20px;
        }

        .feature-card h3 {
            font-family: 'K2D', sans-serif;
            font-size: 1.5em;
            margin-bottom: 15px;
        }

        .feature-card p {
            font-family: 'Itim', cursive;
            font-size: 1.1em;
            color: #AAAAAA;
            line-height: 1.6;
        }
    </style>
</head>
<body>

    <section class="hero-section">
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
    </section>

    <section class="features-section">
        <h2>Proč si vybrat Edulink?</h2>
        <div class="features-grid">
            <div class="feature-card">
                <i class="fas fa-chart-pie"></i>
                <h3>Přehledné statistiky</h3>
                <p>Veškeré známky a docházka v moderních a srozumitelných grafech.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-bell"></i>
                <h3>Okamžité notifikace</h3>
                <p>Nová známka? Změna v rozvrhu? Vše se ihned dozvíte díky chytrým upozorněním.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-check-circle"></i>
                <h3>Jednoduchost</h3>
                <p>Intuitivní a přehledné rozhraní, ve kterém se nikdo neztratí.</p>
            </div>
        </div>
    </section>

</body>
</html>
"""

@app.route("/")
def hlavni_stranka():
    template = Template(html_sablona)
    return template.render()