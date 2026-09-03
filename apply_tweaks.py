import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

# 1. Desktop Services page image fix
# Remove the bad block
html = re.sub(r'<div class="max-w-7xl mx-auto px-6 lg:px-8 py-10">\s*<img src="images/islamic_ceremony\.webp"[^>]+>\s*</div>', '', html)

# Inject after the header
header_block = '''<h1 class="font-title text-4xl font-bold">Services & Counselling</h1>
          <p class="mt-2 text-gold-200 font-bold tracking-wider uppercase text-xs">Tailored options for your legal and spiritual journey</p>
        </div>'''

good_img_block = header_block + '''
        
        <div class="max-w-5xl mx-auto px-6 lg:px-8 mt-16 -mb-8">
          <img src="images/islamic_ceremony.webp" class="w-full h-auto rounded-3xl shadow-xl border border-slate-100">
        </div>'''

html = html.replace(header_block, good_img_block)

# 2. Mobile Home Page: Add certificate.webp above "About Hisham Gad"
m_about_marker = '<h2 class="font-title font-bold text-sm text-islamic-950">About Sheikh Hisham Gad</h2>'
m_about_img = '<img src="images/certificate.webp" class="w-full h-auto rounded-2xl shadow-sm border border-slate-100 mb-4">\n          '
if 'images/certificate.webp" class="w-full h-auto' not in html:
    html = html.replace(m_about_marker, m_about_img + m_about_marker)

# 3. Logo graphic: Remove the SHG logo from nav bar.
# Desktop Logo
html = re.sub(r'<div class="w-8 h-8 rounded-full bg-islamic-900 text-gold-400 flex items-center justify-center font-title font-bold text-lg shadow-sm border border-gold-600/30">\s*S\s*</div>', '', html)
# Mobile Logo
html = re.sub(r'<div class="w-7 h-7 rounded-full bg-islamic-900 text-gold-400 flex items-center justify-center font-title font-bold text-sm shadow-sm border border-gold-600/30">\s*S\s*</div>', '', html)

# 4. Mobile About Me and Overseas couple sections: Keep images full size (not cropped)
# The mobile About me has a w-24 h-24 rounded-full overflow-hidden mx-auto ...
html = re.sub(r'<div class="w-24 h-24 rounded-full overflow-hidden mx-auto border-2 border-gold-500 shadow-sm">\s*<img width="800" height="1000" src="images/grooms_father\.webp" loading="lazy" class="w-full h-full object-cover"', 
              r'<div class="w-full mx-auto border border-slate-200 rounded-xl overflow-hidden shadow-sm">\n            <img src="images/grooms_father.webp" loading="lazy" class="w-full h-auto"', html)

# Mobile Overseas overlay has: <img src="images/civil_overseas.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100 mb-4">
html = html.replace('src="images/civil_overseas.webp" class="w-full h-48 object-cover', 'src="images/civil_overseas.webp" class="w-full h-auto')

# Might as well do Visa overlay too, just in case they want it full size.
html = html.replace('src="images/certificate.webp" class="w-full h-48 object-cover', 'src="images/certificate.webp" class="w-full h-auto')

# 5. Education section: Change text.
old_edu = "Quran and Tajweed"
new_edu = "Weekly classes Saturdays after Maghrib in summer and after Isha in winters"
html = html.replace(old_edu, new_edu)

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
