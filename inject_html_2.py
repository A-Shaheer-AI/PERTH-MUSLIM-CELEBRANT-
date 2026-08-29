import re

HTML_PATH = r"C:\projetcs\index.html"
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Add Image to Mobile Formalities
m_form_marker = '<section id="m-formalities" class="m-page-section px-4 py-4 space-y-4">'
m_form_img = '\n        <img src="images/nikah_rivervale.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_form_marker in html and "images/nikah_rivervale.webp" not in html.split(m_form_marker)[1][:200]:
    html = html.replace(m_form_marker, m_form_marker + m_form_img)

# Add Image to Mobile Wills
m_wills_marker = '<section id="m-wills" class="m-page-section px-4 py-4 space-y-4">'
m_wills_img = '\n        <img src="images/wills.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_wills_marker in html and "images/wills.webp" not in html.split(m_wills_marker)[1][:200]:
    html = html.replace(m_wills_marker, m_wills_marker + m_wills_img)

# Ensure mobile services also got it, just in case
m_services_marker = '<section id="m-services" class="m-page-section px-4 py-4 space-y-3.5">'
m_services_img = '\n        <img src="images/islamic_ceremony.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_services_marker in html and "images/islamic_ceremony.webp" not in html.split(m_services_marker)[1][:200]:
    html = html.replace(m_services_marker, m_services_marker + m_services_img)
    
with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injections successful!")
