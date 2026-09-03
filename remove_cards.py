import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

bad_block_regex = r'<!-- Celebrant Summary Cards -->\s*<div class="grid grid-cols-2 gap-3">.*?</div>\s*</button>\s*</div>'
# The regex above is a bit brittle, let's use exact strings if possible.
# Actually, the block ends with </div> just before <!-- Welcome text card -->
parts = html.split('<!-- Celebrant Summary Cards -->')
if len(parts) == 2:
    subparts = parts[1].split('<!-- Welcome text card -->')
    if len(subparts) == 2:
        html = parts[0] + '<!-- Welcome text card -->' + subparts[1]

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
