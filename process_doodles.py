import os
from PIL import Image

def extract_white_lines(img_path, out_path):
    img = Image.open(img_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    for item in data:
        # Calculate brightness
        brightness = (item[0] + item[1] + item[2]) / 3
        if brightness > 120:
            # Keep as white, use brightness as alpha
            alpha = int(min(255, max(0, (brightness - 120) / 135 * 255)))
            new_data.append((255, 255, 255, alpha))
        else:
            new_data.append((255, 255, 255, 0))
            
    img.putdata(new_data)
    img.save(out_path, "PNG")
    print(f"Saved {out_path}")

doodles = {
    "doodle_home.png": r"C:\Users\vigne\.gemini\antigravity\brain\1d1be08c-d630-43f8-ba9d-04873a877219\doodle_home_1790221531747.jpg",
    "doodle_projects.png": r"C:\Users\vigne\.gemini\antigravity\brain\1d1be08c-d630-43f8-ba9d-04873a877219\doodle_projects_1790221651115.jpg",
    "doodle_resume.png": r"C:\Users\vigne\.gemini\antigravity\brain\1d1be08c-d630-43f8-ba9d-04873a877219\doodle_resume_1790221730086.jpg",
    "doodle_contact.png": r"C:\Users\vigne\.gemini\antigravity\brain\1d1be08c-d630-43f8-ba9d-04873a877219\doodle_contact_1790221806187.jpg"
}

for name, path in doodles.items():
    extract_white_lines(path, f"assets/{name}")
