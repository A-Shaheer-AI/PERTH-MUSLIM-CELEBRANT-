import re

HTML_PATH = r"C:\projetcs\index.html"
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# First replace everything with sheikh_solo
html = html.replace('sheikh_hisham_home.webp', 'sheikh_solo.webp')

# Now fix the two specific instances that should be grooms_father
target_img = '<img width="800" height="1000" src="images/sheikh_solo.webp" loading="lazy" class="w-full h-full object-cover" alt="Sheikh Hisham Gad authorized Islamic marriage celebrant Perth">'
replacement_img = '<img width="800" height="1000" src="images/grooms_father.webp" loading="lazy" class="w-full h-full object-cover" alt="Sheikh Hisham Gad authorized Islamic marriage celebrant Perth">'

html = html.replace(target_img, replacement_img)

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
