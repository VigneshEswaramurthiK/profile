import os
import re
from PIL import Image

# 1. Extract white lines from doodle
def extract_white_lines(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    for item in data:
        # Calculate brightness
        brightness = (item[0] + item[1] + item[2]) / 3
        if brightness > 150:
            # Keep as white, use brightness as alpha for smooth anti-aliasing
            alpha = int((brightness - 150) / 105 * 255)
            new_data.append((255, 255, 255, alpha))
        else:
            new_data.append((255, 255, 255, 0))
            
    img.putdata(new_data)
    img.save(out_path, "PNG")

doodle_src = r"C:\Users\vigne\.gemini\antigravity\brain\1d1be08c-d630-43f8-ba9d-04873a877219\vignesh_doodle_1790175680046.jpg"
doodle_dest = "assets/doodle.png"
extract_white_lines(doodle_src, doodle_dest)

# 2. Fix HTML classes to ensure dark theme works
def fix_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove bootstrap classes that conflict with dark theme
    html = html.replace('class="d-flex flex-column h-100 bg-light"', 'class="d-flex flex-column h-100"')
    html = html.replace('class="d-flex flex-column h-100 bg-white"', 'class="d-flex flex-column h-100"')
    html = html.replace('class="d-flex flex-column bg-light"', 'class="d-flex flex-column"')
    
    html = html.replace('bg-light', 'bg-transparent')
    html = html.replace('bg-white', 'bg-transparent')
    html = html.replace('text-dark', 'text-light')
    html = html.replace('text-muted', 'text-light')
    
    # Replace profile images with the doodle in the tracker
    html = re.sub(r'assets/profile\d*\.png', 'assets/doodle.png', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

for page in ['contact.html', 'projects.html', 'resume.html']:
    fix_html(page)
