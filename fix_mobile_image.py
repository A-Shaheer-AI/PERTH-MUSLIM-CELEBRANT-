import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

# Remove the incorrectly placed image in the header
bad_img_header = '<img src="images/certificate.webp" class="w-full h-auto rounded-2xl shadow-sm border border-slate-100 mb-4">\n          <h2 class="font-title font-bold text-sm text-islamic-950">About Sheikh Hisham Gad</h2>'
good_header = '<h2 class="font-title font-bold text-sm text-islamic-950">About Sheikh Hisham Gad</h2>'
html = html.replace(bad_img_header, good_header)

# Insert it above the correct h3 in the Mobile Home page card
m_home_about_marker = '<h3 class="font-title font-bold text-sm text-islamic-950">About Sheikh Hisham Gad</h3>'
m_home_about_img = '<img src="images/certificate.webp" class="w-full h-auto rounded-xl shadow-sm border border-slate-100 mb-3">\n          '
if 'mb-3">\n          <h3 class="font-title font-bold text-sm text-islamic-950">About Sheikh Hisham Gad</h3>' not in html:
    html = html.replace(m_home_about_marker, m_home_about_img + m_home_about_marker)

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
