import re
path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace meta/JSON instances with absolute URL
html = html.replace('"https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&w=800&auto=format&fit=crop"', '"https://sheikhgad.com.au/images/sheikh_hisham_home.jpg"')
# Also handle the HTML entity version
html = html.replace('"https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&amp;w=800&amp;auto=format&amp;fit=crop"', '"https://sheikhgad.com.au/images/sheikh_hisham_home.jpg"')

# Replace inline image instances with relative URL (w=800 and w=400 variants)
html = html.replace('https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&w=800&auto=format&fit=crop', 'images/sheikh_hisham_home.jpg')
html = html.replace('https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&amp;w=800&amp;auto=format&amp;fit=crop', 'images/sheikh_hisham_home.jpg')
html = html.replace('https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&w=400&auto=format&fit=crop', 'images/sheikh_hisham_home.jpg')
html = html.replace('https://images.unsplash.com/photo-1564507592333-c60657eea523?q=80&amp;w=400&amp;auto=format&amp;fit=crop', 'images/sheikh_hisham_home.jpg')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
print('Images updated successfully!')
