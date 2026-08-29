import re

HTML_PATH = r"C:\projetcs\index.html"
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# Mobile Overseas
m_overseas_marker = '<div id="m-page-sheet-overseas" class="page-sheet hidden absolute inset-0 bg-[#fbfbf9] z-40 flex flex-col">'
if m_overseas_marker in html:
    parts = html.split(m_overseas_marker)
    content_marker = '<div class="flex-grow overflow-y-auto p-4 space-y-4 text-base text-slate-500 leading-relaxed">'
    if content_marker in parts[1]:
        new_part = parts[1].replace(content_marker, content_marker + '\n            <img src="images/civil_overseas.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100 mb-4">\n')
        html = parts[0] + m_overseas_marker + new_part

# Mobile Visas
m_visas_marker = '<div id="m-page-sheet-visas" class="page-sheet hidden absolute inset-0 bg-[#fbfbf9] z-40 flex flex-col">'
if m_visas_marker in html:
    parts = html.split(m_visas_marker)
    content_marker = '<div class="flex-grow overflow-y-auto p-4 space-y-4 text-base text-slate-500 leading-relaxed">'
    if content_marker in parts[1]:
        new_part = parts[1].replace(content_marker, content_marker + '\n            <img src="images/certificate.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100 mb-4">\n')
        html = parts[0] + m_visas_marker + new_part

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("Overlay injections successful!")
