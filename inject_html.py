import re

HTML_PATH = r"C:\projetcs\index.html"
with open(HTML_PATH, 'r', encoding='utf-8') as f:
    html = f.read()

slider_html = """
          <!-- Image Slider Gallery -->
          <div class="w-full overflow-x-auto snap-x snap-mandatory flex gap-4 px-4 lg:px-8 py-6 scrollbar-hide" style="scrollbar-width: none;">
            <img src="images/hero.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/civil_overseas.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/islamic_ceremony.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/nikah_rivervale.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/sheikh_solo.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/certificate.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/grooms_father.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
            <img src="images/wills.webp" class="snap-center shrink-0 w-[80vw] md:w-[400px] h-64 object-cover rounded-2xl shadow-md">
          </div>
"""

# Inject Desktop Testimonial Slider
d_test_marker = '<h1 class="font-title text-4xl font-bold">Client Testimonials</h1>'
if d_test_marker in html and "<!-- Image Slider Gallery -->" not in html.split(d_test_marker)[0]:
    html = html.replace(d_test_marker, slider_html + '\n          ' + d_test_marker)

# Inject Mobile Testimonial Slider
m_test_marker = '<h2 class="font-title font-bold text-sm text-islamic-950">Client Reviews'
if m_test_marker in html:
    parts = html.split('<div id="m-page-sheet-testimonials" class="page-sheet hidden absolute inset-0 bg-[#fbfbf9] z-40 flex flex-col">')
    if len(parts) > 1:
        # Insert after header in the mobile overlay
        m_content_marker = '<div class="flex-grow overflow-y-auto p-4 space-y-3">'
        if m_content_marker in parts[1]:
            new_part = parts[1].replace(m_content_marker, m_content_marker + '\n' + slider_html)
            html = parts[0] + '<div id="m-page-sheet-testimonials" class="page-sheet hidden absolute inset-0 bg-[#fbfbf9] z-40 flex flex-col">' + new_part

# Add Image to Desktop Services Page
d_services_marker = '<section id="d-services" class="d-page-section">'
d_services_img = """
          <div class="max-w-7xl mx-auto px-6 lg:px-8 py-10">
            <img src="images/islamic_ceremony.webp" class="w-full h-80 lg:h-[400px] object-cover rounded-3xl shadow-xl border border-slate-100">
          </div>
"""
if d_services_marker in html and "images/islamic_ceremony.webp" not in html.split(d_services_marker)[1][:500]:
    html = html.replace(d_services_marker, d_services_marker + '\n' + d_services_img)

# Add Image to Mobile Services
m_services_marker = '<section id="m-services" class="m-page-section px-4 py-4 space-y-3.5">'
m_services_img = '\n        <img src="images/islamic_ceremony.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_services_marker in html and "images/islamic_ceremony.webp" not in html.split(m_services_marker)[1][:200]:
    html = html.replace(m_services_marker, m_services_marker + m_services_img)

# Add Image to Mobile Formalities
m_form_marker = '<section id="m-formalities" class="m-page-section px-4 py-4 space-y-3.5">'
m_form_img = '\n        <img src="images/nikah_rivervale.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_form_marker in html and "images/nikah_rivervale.webp" not in html.split(m_form_marker)[1][:200]:
    html = html.replace(m_form_marker, m_form_marker + m_form_img)

# Add Image to Mobile Wills
m_wills_marker = '<section id="m-wills" class="m-page-section px-4 py-4 space-y-3.5">'
m_wills_img = '\n        <img src="images/wills.webp" class="w-full h-48 object-cover rounded-2xl shadow-sm border border-slate-100">\n'
if m_wills_marker in html and "images/wills.webp" not in html.split(m_wills_marker)[1][:200]:
    html = html.replace(m_wills_marker, m_wills_marker + m_wills_img)
    
# Add CSS for hiding scrollbar if not present
if ".scrollbar-hide" not in html:
    css_override = ".scrollbar-hide::-webkit-scrollbar { display: none; }\n    .scrollbar-hide { -ms-overflow-style: none; scrollbar-width: none; }"
    html = html.replace("</style>", css_override + "\n  </style>")

with open(HTML_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("Injections successful!")
