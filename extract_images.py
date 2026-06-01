import re, base64, os

with open('tolga-oto-boya.html', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'<img\s+src="(data:image/(\w+);base64,([^"]+))"\s+alt="([^"]*)"', re.DOTALL)
matches = list(pattern.finditer(text))

os.makedirs('images', exist_ok=True)

names = [
    'audi-a4-yan',
    'audi-a4-onden',
    'audi-a4-ic-mekan',
    'audi-a4-yan-2',
    'bmw-3-serisi',
    'mercedes-c-serisi',
    'toyota-yaris-kirmizi-arka',
    'toyota-yaris-kirmizi-onden',
    'tolga-oto-boya-atolye'
]

new_text = text
for i, m in enumerate(matches):
    full_src = m.group(1)
    ext = m.group(2)
    b64data = m.group(3).replace('\n', '').replace('\r', '').strip()
    alt = m.group(4)
    name = names[i] if i < len(names) else f'image-{i}'
    fname = f'images/{name}.{ext}'
    try:
        img_data = base64.b64decode(b64data)
        with open(fname, 'wb') as f2:
            f2.write(img_data)
        print(f'Saved: {fname} ({len(img_data)//1024}KB) - alt: {alt}')
        new_text = new_text.replace(full_src, fname, 1)
    except Exception as e:
        print(f'Error {name}: {e}')

with open('tolga-oto-boya-new.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print('\nDone! Images extracted, new HTML saved as tolga-oto-boya-new.html')
