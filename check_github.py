import urllib.request
import json
url = 'https://api.github.com/repos/A-Shaheer-AI/PERTH-MUSLIM-CELEBRANT-/contents/'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0')
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())
        if isinstance(data, list):
            for item in data:
                print(f"{item['type']}: {item['name']}")
        else:
            print(data)
except Exception as e:
    print(e)
