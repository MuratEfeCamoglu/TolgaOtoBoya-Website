import re
from collections import Counter

text = open('tolga-oto-boya-new.html', encoding='utf-8').read()

print('=== VIDEO ===')
idx = text.find('<video')
if idx >= 0:
    print(text[idx:idx+250])

print('\n=== GALLERY ITEMS PER CATEGORY ===')
items = re.findall(r'data-category="([\w-]+)"', text)
print(Counter(items))

print('\n=== LOCAL IMAGES USED ===')
imgs = re.findall(r'src="(images/galeri-\d+\.jpeg)"', text)
print(sorted(set(imgs)))

print('\n=== UNSPLASH (should be 0) ===')
unsplash = [x for x in text.split() if 'unsplash.com' in x]
print(len(unsplash), 'found')

print('\n=== VIDEOS ===')
vids = re.findall(r'src="(videos/[^"]+)"', text)
print(vids)
