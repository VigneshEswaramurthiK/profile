import re

def update_pages():
    pages_map = {
        'projects.html': 'doodle_projects.png',
        'resume.html': 'doodle_resume.png',
        'contact.html': 'doodle_contact.png'
    }

    css_animation = """
            @keyframes float {
                0% { transform: translateY(0px) scale(1); }
                50% { transform: translateY(-20px) scale(1.02); }
                100% { transform: translateY(0px) scale(1); }
            }
            .animated-doodle {
                animation: float 4s ease-in-out infinite;
            }
    """

    for page, image_name in pages_map.items():
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()

        # Update image source
        html = re.sub(r'src="assets/doodle\.png"', f'src="assets/{image_name}"', html)
        
        # Add animated class to the img
        html = re.sub(r'id="track-image"', 'id="track-image" class="animated-doodle"', html)
        
        # Add CSS keyframes before </style>
        if '@keyframes float' not in html:
            html = html.replace('</style>', css_animation + '\n</style>')

        with open(page, 'w', encoding='utf-8') as f:
            f.write(html)

    # Now fix index.html
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Remove PixiJS script
    html = re.sub(r'<script src="https://cdnjs\.cloudflare\.com/ajax/libs/pixi\.js/.*?</script>', '', html, flags=re.DOTALL)
    
    # Restore hero image container and standard JS tracking
    html = re.sub(r'<div class="hero-image-container" id="image-container">\s*</div>', 
                  '''<div class="hero-image-container" id="image-container" style="perspective: 1000px;">
                            <img id="track-image" class="animated-doodle" src="assets/doodle_home.png" alt="Vignesh Doodle" style="transition: transform 0.1s ease-out; width: 150%; height: 150%; object-fit: contain; filter: drop-shadow(0 20px 40px rgba(0,0,0,0.4));" />
                        </div>''', html)

    # Remove pixi JS block
    html = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded".*?</script>', '', html, flags=re.DOTALL)
    
    # Replace the canvas css block
    html = re.sub(r'\.hero-image-container canvas \{.*?\}', '', html, flags=re.DOTALL)
    
    if '@keyframes float' not in html:
        html = html.replace('</style>', css_animation + '\n</style>')

    # Add back the simple 3D mouse tracking script
    tracking_script = """<script>
            document.addEventListener("mousemove", (e) => {
                const img = document.getElementById("track-image");
                if (!img) return;
                
                const rect = img.getBoundingClientRect();
                const mouseX = e.clientX - (rect.left + rect.width / 2);
                const mouseY = e.clientY - (rect.top + rect.height / 2);
                
                const xNorm = mouseX / (window.innerWidth / 2);
                const yNorm = mouseY / (window.innerHeight / 2);
                
                // Add the rotate on top of the floating animation by doing it via JS style overriding?
                // Actually, overriding transform in JS breaks CSS animation.
                // We should rotate the container, and let the img float.
                const container = document.getElementById("image-container");
                if(container) {
                    container.style.transform = `rotateX(${-yNorm * 25}deg) rotateY(${xNorm * 25}deg)`;
                }
            });
            
            document.addEventListener("mouseleave", () => {
                const container = document.getElementById("image-container");
                if(container) {
                    container.style.transition = 'transform 0.5s ease-out';
                    container.style.transform = `rotateX(0deg) rotateY(0deg)`;
                    setTimeout(() => { container.style.transition = 'transform 0.1s ease-out'; }, 500);
                }
            });
        </script>"""
    
    html = html.replace('</body>', tracking_script + '\n</body>')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_pages()
