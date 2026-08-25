path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

# Fix the broken ones
html = html.replace('width=" 800\ height=\\1000\ ', 'width="800" height="1000" ')
html = html.replace('width=" 800\\ height=\\1000\\', 'width="800" height="1000"')

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
