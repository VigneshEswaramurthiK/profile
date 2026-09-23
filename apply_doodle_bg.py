import os
import re

css_and_js = """
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #2a0812 0%, #4e1121 100%) !important;
                background-attachment: fixed !important;
                color: #fff !important;
                position: relative;
            }
            .text-muted, .text-dark, .text-secondary { color: #ddd !important; }
            .text-primary { color: #ff9d9d !important; }
            .card { background: rgba(255,255,255,0.05) !important; color: #fff !important; border: 1px solid rgba(255,255,255,0.1) !important; box-shadow: none !important; }
            .navbar { background: transparent !important; position: absolute; width: 100%; z-index: 10; top: 0; }
            .navbar-brand span { color: #fff !important; }
            .navbar-light .navbar-nav .nav-link { color: rgba(255,255,255,0.8); }
            .navbar-light .navbar-nav .nav-link:hover { color: #fff; }
            
            .form-control { background: rgba(255,255,255,0.1); color: #fff; border-color: rgba(255,255,255,0.2); }
            .form-control:focus { background: rgba(255,255,255,0.2); color: #fff; }
            main { padding-top: 100px; position: relative; z-index: 1; } 
            footer { border-top: 1px solid rgba(255,255,255,0.1); background: transparent !important; position: relative; z-index: 1; }
            h1, h2, h3, h4, h5 { color: #fff !important; }
            p, div { color: #eee !important; }
            .text-gradient {
                background: -webkit-linear-gradient(#fff, #eee);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }

            /* Doodle Background Styles */
            .doodle-bg-container {
                position: fixed;
                top: 0;
                left: 0;
                width: 100vw;
                height: 100vh;
                z-index: 0; /* Behind text content */
                pointer-events: none; /* Allows clicking on links above it */
                display: flex;
                justify-content: center;
                align-items: center;
                opacity: 0.15; /* Translucent */
                perspective: 1200px;
                overflow: hidden;
            }
            .doodle-bg-container img {
                width: 110vmin; /* Enlarge the doodle */
                height: 110vmin;
                object-fit: contain;
                transition: transform 0.1s ease-out;
            }
        </style>
"""

js_code = """
        <div class="doodle-bg-container" id="image-container">
            <img id="track-image" src="assets/doodle.png" alt="" />
        </div>
        <script>
            document.addEventListener("mousemove", (e) => {
                const img = document.getElementById("track-image");
                if (!img) return;
                
                // Calculate mouse position relative to center of screen
                const x = e.clientX - window.innerWidth / 2;
                const y = e.clientY - window.innerHeight / 2;
                
                const xNorm = x / (window.innerWidth / 2);
                const yNorm = y / (window.innerHeight / 2);
                
                img.style.transform = `rotateX(${-yNorm * 25}deg) rotateY(${xNorm * 25}deg) scale(1.05)`;
            });
            document.addEventListener("mouseleave", () => {
                const img = document.getElementById("track-image");
                if(img) {
                    img.style.transition = 'transform 0.5s ease-out';
                    img.style.transform = `rotateX(0deg) rotateY(0deg) scale(1)`;
                    setTimeout(() => { img.style.transition = 'transform 0.1s ease-out'; }, 500);
                }
            });
        </script>
"""

def update_page(filename):
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # Remove bg-light, bg-white
    html = html.replace('class="d-flex flex-column h-100 bg-light"', 'class="d-flex flex-column h-100"')
    html = html.replace('class="d-flex flex-column h-100 bg-white"', 'class="d-flex flex-column h-100"')
    html = html.replace('class="d-flex flex-column bg-light"', 'class="d-flex flex-column"')
    
    html = html.replace('bg-light', 'bg-transparent')
    html = html.replace('bg-white', 'bg-transparent')
    html = html.replace('text-dark', 'text-light')
    html = html.replace('text-muted', 'text-light')

    # Add head CSS
    html = html.replace('</head>', css_and_js + '\n</head>')
    
    # Add body JS and doodle container
    html = html.replace('</body>', js_code + '\n</body>')

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

for page in ["contact.html", "projects.html", "resume.html"]:
    update_page(page)
