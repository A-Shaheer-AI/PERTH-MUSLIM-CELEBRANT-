import re

HTML_PATH = r"C:\projetcs\index.html"
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

slider_html = """
          <!-- Image Slider Gallery -->
          <div class="w-full overflow-x-auto snap-x snap-mandatory flex gap-4 py-4 scrollbar-hide -mx-4 px-4" style="scrollbar-width: none;">
            <img src="images/hero.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/civil_overseas.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/islamic_ceremony.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/nikah_rivervale.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/sheikh_solo.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/certificate.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/grooms_father.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
            <img src="images/wills.webp" class="snap-center shrink-0 w-[80vw] h-64 object-cover rounded-2xl shadow-md border border-slate-100">
          </div>
"""

m_test_marker = '<div id="m-page-sheet-testimonials" class="page-sheet hidden absolute inset-0 bg-[#fbfbf9] z-40 flex flex-col">'
if m_test_marker in html:
    parts = html.split(m_test_marker)
    content_marker = '<div class="flex-grow overflow-y-auto p-4 space-y-3.5">'
    if content_marker in parts[1] and "<!-- Image Slider Gallery -->" not in parts[1]:
        new_part = parts[1].replace(content_marker, content_marker + '\n' + slider_html)
        html = parts[0] + m_test_marker + new_part

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)
