path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="https://sheikhgad.com.au/images/', 'src="images/')

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)
