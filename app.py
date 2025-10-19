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
            background-color: #FDFBF6;
        }
        
        /* === ÚVODNÍ SEKCE (HERO) === */
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
            position: fixed;
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
            z-index: 1000;
            color: #002B55;
        }
        .top-bar a { text-decoration: none; color: inherit; padding: 8px 15px; }
        .menu-icon { height: 55px; display: block; }
        
        .main-content { position: relative; z-index: 2; }
        .main-content h1 { font-size: 5em; font-weight: 800; margin: 0; line-height: 1; }
        .main-content p { font-size: 1.6em; font-weight: 400; margin: 10px 0 0 5px; }
        
        /* === SEKCE APLIKACE (SPOLEČNÉ STYLY) === */
        .app-section {
            padding: 80px 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            text-align: center;
            margin-bottom: 50px;
        }
        .section-header h2 {
            font-size: 2.5em;
            font-weight: 800;
            color: #333;
            margin: 0;
        }
        .section-header p {
            font-size: 1.2em;
            color: #777;
            margin-top: 5px;
        }
        
        .role-switcher { display: flex; gap: 15px; margin-bottom: 15px; }
        .btn { color: white; padding: 8px 20px; border: none; border-radius: 8px; font-family: 'K2D', sans-serif; font-size: 0.9em; cursor: pointer; display: inline-block; }
        .btn-teacher { background-color: #E57373; }
        .btn-student { background-color: #0077ff; }

        .app-row { display: flex; align-items: center; gap: 60px; margin-bottom: 60px; }
        .row-text { flex: 1; }
        .row-widget { flex-basis: 50%; }

        .row-text .main-header { font-size: 2.8em; font-weight: 800; margin-bottom: 10px; }
        .row-text .sub-header { font-size: 1.2em; color: #555; line-height: 1.6; }
        
        .widget-item h3 { font-size: 1.6em; font-weight: 700; margin-top: 0; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; }
        .widget-item h3 .fa-chevron-down { font-size: 0.6em; }

        .custom-select { display: flex; align-items: center; padding: 12px 20px; border-radius: 30px; font-size: 1.2em; font-weight: 700; cursor: pointer; }
        .custom-select .fa-solid { font-size: 1.2em; margin-right: 15px; }
        .custom-select .placeholder { color: #999; margin-left: auto; padding-right: 15px; }
        .custom-select .arrow { margin-left: auto; }

        .blue-select { background-color: white; border: 3px solid #002B55; color: #002B55; }
        .blue-select .fa-book { color: #0077ff; }

        .red-select { background-color: white; border: 3px solid #D32F2F; color: #333; }
        .red-select .fa-file-lines { color: #D32F2F; }
        
        /* === SEKCE ZNÁMKY (UČITEL) === */
        .grades-section { text-align: center; margin-top: 80px; }
        .grades-table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-radius: 15px; overflow: hidden; }
        .grades-table th, .grades-table td { padding: 15px; text-align: center; }
        .grades-table thead { background-color: #f9f9f9; font-size: 1.1em; }
        .grades-table tbody tr:nth-child(even) { background-color: #fcfcfc; }
        .grades-table td:first-child { text-align: left; font-weight: 700; display: flex; align-items: center; gap: 15px; }
        .grade-box { display: inline-block; padding: 8px 15px; border-radius: 8px; color: white; font-weight: 700; }
        .grade-5 { background-color: #EF5350; } .grade-3 { background-color: #FFEE58; color: #333; } .grade-1 { background-color: #66BB6A; } .grade-2 { background-color: #9CCC65; }
        .unsigned-note { background-color: transparent; border: 2px solid #D32F2F; color: #D32F2F; padding: 5px 12px; border-radius: 8px; font-weight: 700; font-size: 0.9em; display: inline-block; }
        .btn-green { background-color: #9CCC65; color: white; padding: 15px 40px; border: none; border-radius: 12px; font-family: 'K2D', sans-serif; font-size: 1.2em; font-weight: 700; cursor: pointer; margin-top: 40px; }

        /* === SEKCE PRO ŽÁKA === */
        .student-section { padding: 60px 20px; background-color: #FDFBF6; }
        .student-card { background-color: white; border-left: 5px solid #0077ff; border-radius: 8px; padding: 25px; margin-bottom: 20px; box-shadow: 0 4px 20px rgba(0,0,0,0.08); max-width: 900px; margin-left: auto; margin-right: auto; }
        .student-card h3 { margin-top: 0; color: #002B55; font-size: 1.6em; display: flex; align-items: center; gap: 15px; }
        .student-card ul { list-style: none; padding: 0; }
        .student-card li { padding: 10px 0; border-bottom: 1px solid #eee; font-size: 1.1em; }
        .student-card li:last-child { border-bottom: none; }
        
        /* === SEKCE CHATU === */
        .chat-container {
            background-color: white;
            border-radius: 20px;
            padding: 30px;
            max-width: 900px;
            margin: 0 auto;
            box-shadow: 0 4px 25px rgba(0,0,0,0.08);
        }
        .chat-header {
            text-align: center;
            font-size: 1.5em;
            font-weight: 700;
            color: #333;
            margin-bottom: 25px;
        }
        .chat-messages {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        .message-bubble {
            padding: 12px 20px;
            border-radius: 20px;
            max-width: 70%;
            position: relative;
            color: white;
        }
        .message-bubble .name {
            font-weight: 700;
            margin-bottom: 5px;
        }
        .message-bubble .text {
            line-height: 1.5;
            padding-right: 50px; /* Místo pro čas */
        }
        .message-bubble .timestamp {
            font-size: 0.8em;
            position: absolute;
            bottom: 8px;
            right: 15px;
            color: rgba(255,255,255,0.7);
        }
        .sent {
            background-color: #8BC34A; /* Zelená */
            align-self: flex-end;
            border-bottom-right-radius: 5px;
        }
        .received {
            background-color: #757575; /* Tmavší šedá */
            align-self: flex-start;
            border-bottom-left-radius: 5px;
        }
        
        @media (max-width: 900px) {
            .app-row { flex-direction: column; gap: 40px; text-align: center; }
            .app-row.reversed { flex-direction: column-reverse; }
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
        <div class="app-row">
            <div class="row-text">
                <div class="role-switcher">
                    <div class="btn btn-teacher">Učitel</div>
                    <div class="btn btn-student">Žák</div>
                </div>
                <div class="main-header">Nastavte domácí úkoly</div>
                <p class="sub-header">Připomeňte žákům, že mají domácí úkol! Stačí jen pár kliknutí.</p>
            </div>
            <div class="row-widget">
                <div class="widget-item">
                    <h3>Domácí Úkoly <i class="fa-solid fa-chevron-down"></i></h3>
                    <div class="custom-select blue-select">
                        <i class="fa-solid fa-book"></i>
                        <span>Přírodopis</span>
                        <span class="placeholder">23-MM</span>
                        <i class="fa-solid fa-chevron-down arrow"></i>
                    </div>
                </div>
            </div>
        </div>

        <div class="app-row reversed">
            <div class="row-widget">
                <div class="widget-item">
                    <h3>Testy <i class="fa-solid fa-chevron-down"></i></h3>
                    <div class="custom-select red-select">
                        <i class="fa-solid fa-file-lines"></i>
                        <span>Čeština</span>
                        <span class="placeholder">23.9</span>
                        <i class="fa-solid fa-chevron-down arrow"></i>
                    </div>
                </div>
            </div>
            <div class="row-text" style="text-align: right;">
                 <div class="main-header">Varujte žáky</div>
                 <p class="sub-header">Zapomněli jste oznámit test? Vůbec nevadí! Stačí jen pár kliků a žáci budou oznámeni!</p>
            </div>
        </div>

        <div class="grades-section">
            <h2 style="font-weight: 800;">Známky</h2>
            <p style="color: #555;">Zapisování známek nikdy nebylo lehčí!</p>
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
                        <td><span class="unsigned-note">Nepodepsáno</span></td>
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

    <section class="student-section">
        <div class="app-section">
            <div class="section-header">
                <h2>Přehled</h2>
                <p>Měj přehled o všem, o čem zasníš</p>
            </div>
            
            <div class="student-card">
                <h3><i class="fa-solid fa-clipboard-list"></i> Moje úkoly</h3>
                <ul>
                    <li>Přírodopis: Pracovní sešit str. 34-35 (do 24.10.)</li>
                    <li>Dějepis: Přečíst kapitolu o Karlu IV. (do 26.10.)</li>
                </ul>
            </div>
            <div class="student-card">
                <h3><i class="fa-solid fa-graduation-cap"></i> Moje známky</h3>
                <ul>
                    <li>Čeština - diktát: 2</li>
                    <li>Matematika - pětiminutovka: 1</li>
                    <li>Angličtina - slovíčka: 3</li>
                </ul>
            </div>

            <div class="section-header" style="margin-top: 80px;">
                <h2>Komunikace a debaty</h2>
                <p>Piš si s ostatními, a dozvíš se, co potřebuješ</p>
            </div>
            <div class="chat-container">
                <div class="chat-header">Skupina IV</div>
                <div class="chat-messages">
                    <div class="message-bubble sent">
                        <div class="name">Tom</div>
                        <div class="text">Bude zítra ten film?</div>
                        <div class="timestamp">13:22</div>
                    </div>
                    <div class="message-bubble received">
                        <div class="name">Nutella</div>
                        <div class="text">Ano bude. Těším se! :D</div>
                        <div class="timestamp">13:24</div>
                    </div>
                     <div class="message-bubble received">
                        <div class="name">Marcela (Učitelka)</div>
                        <div class="text">Nezapomeňte si vzít sebou něco dobrého!</div>
                        <div class="timestamp">13:24</div>
                    </div>
                </div>
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