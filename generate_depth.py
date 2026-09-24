from PIL import Image, ImageFilter, ImageDraw, ImageChops

# Load image
img = Image.open('assets/portrait.png').convert('RGBA')
w, h = img.size

# Extract alpha
alpha = img.split()[3]

# 1. Base depth: the silhouette blurred (dome effect)
base_depth = alpha.filter(ImageFilter.GaussianBlur(radius=40))

# 2. Face depth: a blob where the face is, blurred
face_blob = Image.new('L', img.size, 0)
f_draw = ImageDraw.Draw(face_blob)
# Estimate face position (upper center)
f_draw.ellipse([w*0.25, h*0.1, w*0.75, h*0.6], fill=255)
face_blob = face_blob.filter(ImageFilter.GaussianBlur(radius=50))

# 3. Combine them using screen (lighter of the two)
depth_map = ImageChops.screen(base_depth, face_blob)

# 4. Mask the depth map so the background is completely black (farthest)
depth_map = Image.composite(depth_map, Image.new('L', img.size, 0), alpha)

depth_map.save('assets/portrait-depth.png')
print("Depth map generated.")
