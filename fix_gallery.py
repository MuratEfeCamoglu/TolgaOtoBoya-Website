with open('tolga-oto-boya-new.html', encoding='utf-8') as f:
    text = f.read()

# Fix item 0: tall, audi-a4-yan.jpeg -> Unsplash + data-category
text = text.replace(
    'gallery-item tall reveal" onclick="openLightbox(0)">\n        <img src="images/audi-a4-yan.jpeg" alt="Audi A4 Yan">',
    'gallery-item tall reveal" data-category="pasta-cila" onclick="openLightbox(0)">\n        <img src="https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=800&q=80" alt="Pasta Cila - Ayna Parlakligi">'
)

# Fix item 4: wide, bmw -> Unsplash + data-category
text = text.replace(
    'gallery-item wide reveal" onclick="openLightbox(4)">\n        <img src="images/bmw-3-serisi.jpeg" alt="BMW 3 Serisi">',
    'gallery-item wide reveal" data-category="boya-koruma" onclick="openLightbox(4)">\n        <img src="https://images.unsplash.com/photo-1547744152-14d985cb937f?w=1200&q=80" alt="PPF Boya Koruma Filmi">'
)

with open('tolga-oto-boya-new.html', 'w', encoding='utf-8') as f:
    f.write(text)

remaining = ['images/audi-a4-yan.jpeg', 'images/bmw-3-serisi.jpeg']
for r in remaining:
    print(f'{"Still exists" if r in text else "REMOVED"}: {r}')

print('Done!')
