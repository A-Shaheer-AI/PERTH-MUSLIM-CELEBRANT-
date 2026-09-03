import urllib.request
try:
    req = urllib.request.Request('https://www.islamicmarriagewa.com.au/')
    req.add_header('User-Agent', 'Mozilla/5.0')
    response = urllib.request.urlopen(req)
    print(f"Status: {response.getcode()}")
    print("Headers:", response.headers)
except Exception as e:
    print("Error:", e)
