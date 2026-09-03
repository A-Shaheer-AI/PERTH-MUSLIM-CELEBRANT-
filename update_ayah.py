import re

path = r'C:\projetcs\index.html'
with open(path, 'r', encoding='utf-8') as f: 
    html = f.read()

desktop_block = '''          <!-- Quote overlay -->
          <div class="max-w-4xl mx-auto px-6 -mt-10 relative z-20">
            <div class="bg-white rounded-2xl shadow-xl p-8 border border-slate-100 text-center space-y-4">
              <div class="text-islamic-800 text-2xl font-bold">وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً</div>
              <p class="font-title text-lg text-slate-800 italic leading-relaxed">
                "And He put between you love and compassion; most surely there are signs in this for a people who reflect."
              </p>
              <div class="text-sm text-gold-600 uppercase font-black tracking-widest">— Surah Al-Rum, Verse 21</div>
            </div>
          </div>'''

desktop_block_new = '''          <!-- Quote overlay -->
          <div class="max-w-4xl mx-auto px-6 -mt-10 relative z-20">
            <div class="bg-white rounded-2xl shadow-xl p-8 border border-slate-100 text-center space-y-4">
              <div class="text-islamic-800 text-2xl font-bold leading-relaxed" lang="ar" dir="rtl">وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّقَوْمٍ يَتَفَكَّرُونَ</div>
              <p class="font-title text-lg text-slate-800 italic leading-relaxed">
                "And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy. Indeed in that are signs for a people who give thought."
              </p>
              <div class="text-sm text-gold-600 uppercase font-black tracking-widest">— Surah Al-Rum, Verse 21</div>
            </div>
          </div>'''

mobile_block = '''          <!-- Quran Verse Card -->
          <div class="bg-white rounded-xl border border-slate-100 shadow-sm p-4 text-center space-y-1.5">
            <div class="text-islamic-800 text-base font-bold">وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً</div>
            <p class="text-base italic text-slate-500 leading-relaxed font-title">
              "And He has put between you love and compassion..."
            </p>
            <div class="text-[10px] font-bold text-gold-600 tracking-wider uppercase">— Surah Al-Rum: Verse 21</div>
          </div>'''

mobile_block_new = '''          <!-- Quran Verse Card -->
          <div class="bg-white rounded-xl border border-slate-100 shadow-sm p-4 text-center space-y-2.5">
            <div class="text-islamic-800 text-base font-bold leading-relaxed" lang="ar" dir="rtl">وَمِنْ آيَاتِهِ أَنْ خَلَقَ لَكُم مِّنْ أَنفُسِكُمْ أَزْوَاجًا لِّتَسْكُنُوا إِلَيْهَا وَجَعَلَ بَيْنَكُم مَّوَدَّةً وَرَحْمَةً ۚ إِنَّ فِي ذَٰلِكَ لَآيَاتٍ لِّقَوْمٍ يَتَفَكَّرُونَ</div>
            <p class="text-sm italic text-slate-500 leading-relaxed font-title">
              "And of His signs is that He created for you from yourselves mates that you may find tranquility in them; and He placed between you affection and mercy. Indeed in that are signs for a people who give thought."
            </p>
            <div class="text-[10px] font-bold text-gold-600 tracking-wider uppercase">— Surah Al-Rum: Verse 21</div>
          </div>'''

if desktop_block in html:
    html = html.replace(desktop_block, desktop_block_new)
else:
    print("Desktop block not found perfectly, trying regex")
    
if mobile_block in html:
    html = html.replace(mobile_block, mobile_block_new)
else:
    print("Mobile block not found perfectly, trying regex")

with open(path, 'w', encoding='utf-8') as f: 
    f.write(html)
