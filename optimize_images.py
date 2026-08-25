import os
import re
import requests
from io import BytesIO
from PIL import Image

IMAGE_MAPPING = {
    "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?q=80&w=1200&auto=format&fit=crop": "hero_desktop.webp",
    "https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?q=80&w=800&auto=format&fit=crop": "hero_mobile.webp",
    "https://images.unsplash.com/photo-1607190074257-dd4b7af0309f?q=80&w=600&auto=format&fit=crop": "rings.webp",
    "https://images.unsplash.com/photo-1573075037145-21d3f99e46a7?q=80&w=800&auto=format&fit=crop": "overseas.webp",
    "https://images.unsplash.com/photo-1450133064473-71024230f91b?q=80&w=800&auto=format&fit=crop": "signing.webp",
    "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?q=80&w=800&auto=format&fit=crop": "wills.webp"
}

HTML_PATH = r"C:\projetcs\index.html"
IMG_DIR = r"C:\projetcs\images"

def main():
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Download and convert Unsplash images
    for url, filename in IMAGE_MAPPING.items():
        print(f"Downloading {filename}...")
        resp = requests.get(url)
        if resp.status_code == 200:
            img = Image.open(BytesIO(resp.content))
            img.save(os.path.join(IMG_DIR, filename), "WEBP", quality=85)
            # Replace URL in HTML
            # Replace ampersands just in case they are encoded in HTML
            encoded_url = url.replace('&', '&amp;')
            html = html.replace(url, f"images/{filename}")
            html = html.replace(encoded_url, f"images/{filename}")
        else:
            print(f"Failed to download {url}")

    # 2. Convert sheikh_hisham_home.jpg to WebP
    local_img_path = os.path.join(IMG_DIR, "sheikh_hisham_home.jpg")
    local_webp_name = "sheikh_hisham_home.webp"
    if os.path.exists(local_img_path):
        print(f"Converting {local_img_path} to WEBP...")
        img = Image.open(local_img_path)
        img.save(os.path.join(IMG_DIR, local_webp_name), "WEBP", quality=85)
        # Update references in HTML
        html = html.replace("images/sheikh_hisham_home.jpg", f"images/{local_webp_name}")
        html = html.replace("https://sheikhgad.com.au/images/sheikh_hisham_home.jpg", f"https://sheikhgad.com.au/images/{local_webp_name}")

    # 3. Inject width and height into all <img> tags that don't have them
    # For simplicity, we just inject standard 4:5 ratio for most images, and 3:2 for the hero.
    
    def add_dimensions(match):
        img_tag = match.group(0)
        # If it already has width/height, leave it alone
        if 'width=' in img_tag or 'height=' in img_tag:
            return img_tag
        
        src = match.group(1)
        if 'hero' in src:
            return img_tag.replace('<img ', '<img width="1200" height="800" ')
        else:
            return img_tag.replace('<img ', '<img width="800" height="1000" ')
            
    # Regex to find <img ... src="images/...">
    html = re.sub(r'<img[^>]*src=[\"\'](images/[^\"]+)[\"\'][^>]*>', add_dimensions, html)

    # 4. Save HTML
    with open(HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print("Optimization complete!")

if __name__ == "__main__":
    main()
