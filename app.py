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
    <link href="https://fonts.googleapis.com/css2?family=Itim&family=K2D:wght@400;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
    
    <style>
        html {
            scroll-behavior: smooth;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'K2D', sans-serif;
            background-color: #FDFBF6; /* Světlé pozadí z tvého návrhu */
        }
        
        /* === ÚVODNÍ SEKCE (HERO) - zůstává stejná === */
        .hero-section {
            min-height: 100vh;
            position: relative;
            overflow: hidden;
            display: flex;
            align-items: flex-end;
            justify-content: flex-start;
            padding: 60px 80px;
            box-sizing: border-box;
            color: #002B55;
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
            z-index: 3;
            color: #002B55;
        }
        .top-bar a { text-decoration: none; color: inherit; padding: 8px 15px; }
        .menu-icon { height: 45px; display: block; }
        
        .main-content { position: relative; z-index: 2; }
        .main-content h1 { font-size: 5em; font-weight: 800; margin: 0; line-height: 1; }
        .main-content p { font-size: 1.6em; font-weight: 400; margin: 10px 0 0 5px; }
        
        /* === NOVÁ SEKCE APLIKACE === */
        .app-section {
            padding: 60px 20px;
            max-width: 1100px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 40px;
        }
        .section-header h2 {
            font-size: 2.5em;
            color: #333;
            margin: 0;
        }
        .section-header p {
            font-size: 1.2em;
            color: #777;
            margin-top: 5px;
        }
        .btn-red {
            background-color: #E57373;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 8px;
            font-family: 'K2D', sans-serif;
            font-size: 1em;
            cursor: pointer;
            margin-top: 15px;
        }
        
        .widgets-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-bottom: 40px;
        }
        
        .widget-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }
        .widget-card h3 {
            margin-top: 0;
            font-size: 1.5em;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .widget-card .fa-solid { color: #555; }
        
        select, input[type="text"] {
            width: 100%;
            padding: 12px;
            border: 2px solid #E0E0E0;
            border-radius: 8px;
            font-family: 'K2D', sans-serif;
            font-size: 1em;
            margin-top: 10px;
        }
        
        .grades-section { text-align: center; }
        
        .grades-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            border-radius: 15px;
            overflow: hidden; /* Aby se stín a radius aplikoval na celou tabulku */
        }
        .grades-table th, .grades-table td {
            padding: 15px;
            text-align: center;
        }
        .grades-table thead {
            background-color: #f9f9f9;
            font-size: 1.1em;
        }
        .grades-table tbody tr:nth-child(even) { background-color: #fcfcfc; }
        .grades-table td:first-child {
            text-align: left;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .grade-box {
            display: inline-block;
            padding: 8px 15px;
            border-radius: 8px;
            color: white;
            font-weight: 700;
        }
        .grade-5 { background-color: #EF5350; } /* Červená */
        .grade-3 { background-color: #FFEE58; color: #333; } /* Žlutá */
        .grade-1 { background-color: #66BB6A; } /* Zelená */
        .grade-2 { background-color: #9CCC65; } /* Světle zelená */
        
        .btn-green {
            background-color: #9CCC65;
            color: white;
            padding: 15px 40px;
            border: none;
            border-radius: 12px;
            font-family: 'K2D', sans-serif;
            font-size: 1.2em;
            font-weight: 700;
            cursor: pointer;
            margin-top: 40px;
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

    <section class="app-section">
        <div class="section-header">
            <h2>Nastavte domácí úkoly</h2>
            <p>Všechny domácí úkoly, testy a známky po ruce, stačí jen pár kliknutí.</p>
            <button class="btn-red">Učitel</button>
        </div>

        <div class="widgets-grid">
            <div class="widget-card">
                <h3><i class="fa-solid fa-book"></i> Domácí Úkoly</h3>
                <select>
                    <option>Přírodopis</option>
                    <option>Dějepis</option>
                </select>
            </div>
            <div class="widget-card">
                <h3><i class="fa-solid fa-file-signature"></i> Testy</h3>
                <select>
                    <option>Čeština</option>
                    <option>Matematika</option>
                </select>
            </div>
            <div class="widget-card">
                <h3><i class="fa-solid fa-triangle-exclamation"></i> Varujte žáky</h3>
                <p>Napsal někdo špatně test? Vůbec nevadí! Stačí jen pár kliků a žáci budou varováni!</p>
            </div>
        </div>

        <div class="grades-section">
            <h2>Známky</h2>
            <p>Zapisování známek nikdy nebylo lehčí!</p>
            <table class="grades-table">
                <thead>
                    <tr>
                        <th>Žák</th>
                        <th>Test</th>
                        <th>Ústní zkoušení</th>
                        <th>Poznámky</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><i class="fa-solid fa-user"></i> Tom</td>
                        <td><span class="grade-box grade-5">5</span></td>
                        <td><span class="grade-box grade-1">1</span></td>
                        <td>M-Učebnice str. 56</td>
                    </tr>
                    <tr>
                        <td><i class="fa-solid fa-user"></i> Anna</td>
                        <td><span class="grade-box grade-3">3</span></td>
                        <td><span class="grade-box grade-3">3</span></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td><i class="fa-solid fa-user"></i> Nuttela</td>
                        <td><span class="grade-box grade-1">1</span></td>
                        <td><span class="grade-box grade-2">2</span></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td><i class="fa-solid fa-user"></i> Lukas</td>
                        <td><span class="grade-box grade-1">1</span></td>
                        <td><span class="grade-box grade-1">1</span></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <button class="btn-green">Začít!</button>
        </div>
    </section>

</body>
</html>
"""

@app.route("/")
def hlavni_stranka():
    template = Template(html_sablona)
    return template.render()