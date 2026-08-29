import os
from PIL import Image

IMG_DIR = r"C:\projetcs\images"

# Mapping of old filenames to new sanitized webp filenames
RENAME_MAP = {
    "Civil Marriage Ceremony with Overseas Couple.JPG": "civil_overseas.webp",
    "Islamic Bride and Groom.jpg": "hero.webp",  # Likely the hero image
    "islamic marriage ceremony.webp": "islamic_ceremony.webp",
    "Nikah Ceremony in Rivervale Masjid.JPG": "nikah_rivervale.webp",
    "Sheikh Hisham Gad Marriage Celebrant.jpg": "sheikh_solo.webp",
    "Sheikh Hisham with Bride and Groom with Marriage Certificate.JPG": "certificate.webp",
    "Sheikh Hisham with Groom's Father.JPG": "grooms_father.webp",
    "wills.webp": "wills.webp"
}

def process_images():
    for old_name, new_name in RENAME_MAP.items():
        old_path = os.path.join(IMG_DIR, old_name)
        new_path = os.path.join(IMG_DIR, new_name)
        
        if not os.path.exists(old_path):
            print(f"Skipping {old_name}, not found.")
            continue
            
        print(f"Processing {old_name} -> {new_name}")
        try:
            img = Image.open(old_path)
            
            # Convert to RGB if necessary (e.g. RGBA)
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
                
            # Resize if too large (max 1200px width/height)
            MAX_SIZE = 1200
            if img.width > MAX_SIZE or img.height > MAX_SIZE:
                img.thumbnail((MAX_SIZE, MAX_SIZE), Image.Resampling.LANCZOS)
                
            img.save(new_path, "WEBP", quality=80)
            
            # Remove original if it has a different name
            if old_name != new_name:
                os.remove(old_path)
                
        except Exception as e:
            print(f"Error processing {old_name}: {e}")

if __name__ == "__main__":
    process_images()
    print("Done processing images.")
