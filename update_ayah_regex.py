import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

# Replace Arabic Text
html = re.sub(r'وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً', 
              r'وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّقَوْمٍ يَتَفَكَّرُونَ', html)

# Replace Desktop English text
html = re.sub(r'"And He put between you love and compassion;\s*most surely there are signs in this for a people who reflect."', 
              r'"And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy. Indeed in that are signs for a people who give thought."', html)

# Replace Mobile English text
html = re.sub(r'"And He has put between you love and compassion..."', 
              r'"And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy. Indeed in that are signs for a people who give thought."', html)

# Fix missing rtl tags on the new long arabic text (it's already handled if the old text had it, but let's just make sure)
html = html.replace('<div class="text-islamic-800 text-2xl font-bold">', '<div class="text-islamic-800 text-2xl font-bold leading-relaxed" lang="ar" dir="rtl">')
html = html.replace('<div class="text-islamic-800 text-base font-bold">', '<div class="text-islamic-800 text-base font-bold leading-relaxed" lang="ar" dir="rtl">')

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
