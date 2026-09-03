import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

# 1. Remove SHG Logo
# The desktop logo looks like:
# <div class="w-12 h-12 rounded-full bg-islamic-900 border-[3px] border-gold-500 shadow-md flex items-center justify-center shrink-0">
#   <span class="text-gold-200 font-bold text-sm tracking-tighter">SHG</span>
# </div>
html = re.sub(r'<div class="[^"]*rounded-full[^"]*">\s*<span class="[^"]*tracking-tighter[^"]*">SHG</span>\s*</div>', '', html)

# 2. Fix the Arabic Ayah text
# We will match the entire div and replace its contents.
full_arabic = "وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّقَوْمٍ يَتَفَكَّرُونَ"

# Desktop:
html = re.sub(r'(<div class="text-islamic-800 text-2xl font-bold[^>]*>).*?(</div>)', r'\1' + full_arabic + r'\2', html, flags=re.DOTALL)

# Mobile:
html = re.sub(r'(<div class="text-islamic-800 text-base font-bold[^>]*>).*?(</div>)', r'\1' + full_arabic + r'\2', html, flags=re.DOTALL)


with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
