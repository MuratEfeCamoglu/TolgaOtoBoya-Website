import re
text = open('tolga-oto-boya-new.html', encoding='utf-8').read()
matches = re.findall(r'<div class="gallery-item.*?data-category="(.*?)".*?<img src="(.*?)" alt="(.*?)"', text, re.DOTALL)
for m in matches:
    if m[0] == 'far-temizleme':
        print(m[1], m[2])
