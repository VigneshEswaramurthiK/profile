import re

def update_pixi():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add pixi to head
    if 'pixi.min.js' not in html:
        html = html.replace('</head>', '<script src="https://cdnjs.cloudflare.com/ajax/libs/pixi.js/7.3.2/pixi.min.js"></script>\n</head>')

    # 2. Add canvas CSS
    css_to_add = """
            .hero-image-container canvas {
                width: 100%;
                height: 100%;
                object-fit: contain;
                transform: scale(1.1); 
                filter: drop-shadow(0 20px 40px rgba(0,0,0,0.6));
            }
"""
    if 'canvas {' not in html:
        html = html.replace('.hero-image-container img {', css_to_add + '\n            .hero-image-container img {')

    # 3. Replace the entire script block at the end
    script_start = html.find('<script>\n            document.addEventListener("mousemove"')
    script_end = html.find('</script>', script_start) + len('</script>')
    
    if script_start != -1:
        new_script = """<script>
            document.addEventListener("DOMContentLoaded", () => {
                const container = document.getElementById("image-container");
                if (!container) return;
                
                // Clear existing img
                container.innerHTML = "";
                
                // Setup Pixi App
                const app = new PIXI.Application({
                    width: 600,
                    height: 600,
                    backgroundAlpha: 0,
                    resolution: window.devicePixelRatio || 1,
                });
                container.appendChild(app.view);
                
                const imgUrl = "assets/portrait.png";
                const depthUrl = "assets/portrait-depth.png";
                
                PIXI.Assets.load([imgUrl, depthUrl]).then(() => {
                    const sprite = PIXI.Sprite.from(imgUrl);
                    const depthMap = PIXI.Sprite.from(depthUrl);
                    
                    // Scale and position
                    sprite.width = 600;
                    sprite.height = 600;
                    sprite.anchor.set(0.5);
                    sprite.x = 300;
                    sprite.y = 300;
                    
                    depthMap.width = 600;
                    depthMap.height = 600;
                    depthMap.anchor.set(0.5);
                    depthMap.x = 300;
                    depthMap.y = 300;
                    
                    app.stage.addChild(sprite);
                    app.stage.addChild(depthMap);
                    
                    const filter = new PIXI.DisplacementFilter(depthMap);
                    filter.scale.x = 0;
                    filter.scale.y = 0;
                    sprite.filters = [filter];
                    
                    let targetX = 0;
                    let targetY = 0;
                    
                    document.addEventListener('mousemove', (e) => {
                        const rect = app.view.getBoundingClientRect();
                        const mouseX = e.clientX - (rect.left + rect.width / 2);
                        const mouseY = e.clientY - (rect.top + rect.height / 2);
                        
                        const xNorm = mouseX / (window.innerWidth / 2);
                        const yNorm = mouseY / (window.innerHeight / 2);
                        
                        targetX = xNorm * 45; // Max displacement horizontally
                        targetY = yNorm * 45; // Max displacement vertically
                    });
                    
                    document.addEventListener('mouseleave', () => {
                        targetX = 0;
                        targetY = 0;
                    });
                    
                    // Smooth animation loop
                    app.ticker.add(() => {
                        filter.scale.x += (targetX - filter.scale.x) * 0.1;
                        filter.scale.y += (targetY - filter.scale.y) * 0.1;
                    });
                });
            });
        </script>"""
        
        html = html[:script_start] + new_script + html[script_end:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

update_pixi()
