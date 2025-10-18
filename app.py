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
            /* ZMĚNA ZDE: "fixed" zajistí, že menu zůstane na místě při scrollování */
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
            z-index: 1000; /* Zvýšíme z-index, aby bylo vždy úplně nahoře */
            color: #002B55;
        }
        .top-bar a { text-decoration: none; color: inherit; padding: 8px 15px; }
        .menu-icon { height: 45px; display: block; }
        
        .main-content { position: relative; z-index: 2; }
        .main-content h1 { font-size: 5em; font-weight: 800; margin: 0; line-height: 1; }
        .main-content p { font-size: 1.6em; font-weight: 400; margin: 10px 0 0 5