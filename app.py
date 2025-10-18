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
        
        /* === ÚVODNÍ SEKCE (HERO) - beze změny === */
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
        
        /* === PŘEPRACOVANÁ SEKCE APLIKACE === */
        .app-section {
            padding: 80px 40px;
            max-width: 1200px;
            margin: 0 auto;
        }

        /* Nový dvousloupcový layout */
        .app-header-grid {
            display: flex;
            align-items: center;
            gap: 60px; /* Mezera mezi sloupci */
            margin-bottom: 80px;
        }
        
        .header-text {
            flex-basis: 40%; /* Levý sloupec zabere 40% */
        }
        
        .header-widgets {
            flex-basis: 60%; /* Pravý sloupec zabere 60% */
            display: flex;
            flex-direction: column;
            gap: 20px; /* Mezera mezi widgety pod sebou */
        }

        .header-text .main-header {
            font-size: 2.8em;
            font-weight: 800;
            margin-bottom: 10px;
        }

        .header-text .sub-header {
            font-size: 1.2em;
            color: #555;
            line-height: 1.6;
        }
        
        .widget-item h3 {
            font-size: 1.8em;
            margin-top: 0;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .widget-item h3 .fa-chevron-down { font-size: 0.6em; }
        .widget-item p { color: #555; line-height: 1.6; }

        .custom-select {
            display: flex;
            align-items: center;
            padding: 15px 20px;
            border-radius: 12px;
            font-size: 1.2em;
            font-weight: 700;
            cursor: pointer;
        }
        .custom-select .fa-solid { font-size: 1.2em; margin-right: 15px; }
        .custom-select .placeholder { color: #999; margin-left: 10px; }
        .custom-select .arrow { margin-left: auto; }

        .blue-select { background-color: white; border: 3px solid #002B55; color: #002B55; }
        .blue-select .fa-book { color: #0077ff; }

        .red-select { background-color: white; border: 3px solid #D32F2F; color: #333; }
        .red-select .fa-file-lines { color: #D32F2F; }
        
        /* Zbytek stylů pro tabulku zůstává stejný */
        .grades-section { text-align: center; }
        .grades-table { width: 100%; border-collapse: collapse; margin-top: 20px; background: white; box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-radius: 15px; overflow: hidden; }
        .grades-table th, .grades-table td { padding: 15px; text-align: center; }
        .grades-table thead { background-color: #f9f9f9; font-size: 1.1em; }
        .grades-table tbody tr:nth-child(even) { background-color: #fcfcfc; }
        .grades-table td:first-child { text-align: left; font-weight: 700; display: flex; align-items: center; gap: 15px; }
        .grade-box { display: inline-block; padding: 8px 15px; border-radius: 8px; color: white; font-weight: 700; }
        .grade-5 { background-color: #EF5350; } .grade-3 { background-color: #FFEE58; color: #333; } .grade-1 { background-color: #66BB6A; } .grade-2 { background-color: #9CCC65; }
        .btn-green { background-color: #9CCC65; color: white; padding: 15px 40px; border: none; border-radius: 12px; font-family: 'K2D', sans-serif; font-size: 1.2em; font-weight: 700; cursor: pointer; margin-top: 40px; }
        
        /* Responsivní úpravy pro mobily */
        @media (max-width: 900px) {
            .app-header-grid {
                flex-direction: column; /* Sloupce se dají pod sebe */
                gap: 40px;
                text-align: center;
            }
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
        <div class="app-header-grid">
            <div class="header-text">
                <div class="main-header">Nastavte domácí úkoly</div>
                <p class="sub-