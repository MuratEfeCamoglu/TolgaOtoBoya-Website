with open('tolga-oto-boya-new.html', encoding='utf-8') as f:
    text = f.read()

# ── 1. Swap video: tanitim-video-2.mp4 as primary ──
old_video = '''          <source src="videos/tanitim-video-1.mp4" type="video/mp4">
          <source src="videos/tanitim-video-2.mp4" type="video/mp4">'''
new_video = '''          <source src="videos/tanitim-video-2.mp4" type="video/mp4">
          <source src="videos/tanitim-video-1.mp4" type="video/mp4">'''

if old_video in text:
    text = text.replace(old_video, new_video, 1)
    print('Video order swapped: video-2 is now primary')
else:
    print('WARNING: video sources not found')

# ── 2. Change poster image (don't use galeri-01 which might be in gallery) ──
text = text.replace('poster="images/galeri-01.jpeg"', 'poster="images/galeri-05.jpeg"', 1)
print('Video poster changed to galeri-05.jpeg')

# ── 3. Remove duplicate gallery images ──
# Duplicates: galeri-14, galeri-20, galeri-21, galeri-22, galeri-23
import re

# We'll rebuild the gallery skipping duplicate images
# Find the gallery-grid block
cat_labels = {
    'pasta-cila': 'Pasta Cila',
    'oto-boya': 'Oto Boya',
    'boya-koruma': 'Boya Koruma',
    'far-temizleme': 'Far Temizleme',
}

# 19 unique images mapped to categories (skip: 14, 20, 21, 22, 23)
items = [
    (0,  'images/galeri-01.jpeg',  'Pasta Cila Çalışması',          'pasta-cila',    'tall'),
    (1,  'images/galeri-02.jpeg',  'Pasta Cila Detay',              'pasta-cila',    ''),
    (2,  'images/galeri-03.jpeg',  'Oto Boya Karoser',              'oto-boya',      ''),
    (3,  'images/galeri-04.jpeg',  'Oto Boya Kapı Boya',            'oto-boya',      ''),
    (4,  'images/galeri-05.jpeg',  'Boya Koruma PPF',               'boya-koruma',   'wide'),
    (5,  'images/galeri-06.jpeg',  'Boya Koruma Seramik',           'boya-koruma',   ''),
    (6,  'images/galeri-07.jpeg',  'Far Temizleme',                 'far-temizleme', ''),
    (7,  'images/galeri-08.jpeg',  'Far Parlatma Sonucu',           'far-temizleme', ''),
    (8,  'images/galeri-09.jpeg',  'Pasta Cila Atölye',             'pasta-cila',    ''),
    (9,  'images/galeri-10.jpeg',  'Oto Boya Tam Karoser',          'oto-boya',      'tall'),
    (10, 'images/galeri-11.jpeg',  'Oto Boya Detay',                'oto-boya',      ''),
    (11, 'images/galeri-12.jpeg',  'Boya Koruma Uygulama',          'boya-koruma',   ''),
    (12, 'images/galeri-13.jpeg',  'Far Temizleme Öncesi Sonrası',  'far-temizleme', 'wide'),
    (13, 'images/galeri-15.jpeg',  'Oto Boya Çalışma',              'oto-boya',      ''),
    (14, 'images/galeri-16.jpeg',  'Seramik Kaplama',               'boya-koruma',   ''),
    (15, 'images/galeri-17.jpeg',  'Far Parlatma',                  'far-temizleme', ''),
    (16, 'images/galeri-18.jpeg',  'Pasta Cila Sonuç',              'pasta-cila',    'tall'),
    (17, 'images/galeri-19.jpeg',  'Oto Boya Kaput',                'oto-boya',      ''),
    (18, 'images/galeri-24.jpeg',  'Boya Koruma Nano',              'boya-koruma',   ''),
]

display_labels = {
    0:  'Pasta Cila — Ayna Parlaklığı',
    1:  'Pasta Cila — Derin Detay',
    2:  'Oto Boya — Tam Karoser',
    3:  'Oto Boya — Kapı & Tampon',
    4:  'Boya Koruma — PPF Uygulama',
    5:  'Boya Koruma — Seramik',
    6:  'Far Temizleme — Sararmış Far',
    7:  'Far Parlatma — Sonuç',
    8:  'Pasta Cila — Atölye',
    9:  'Oto Boya — Tam Araç',
    10: 'Oto Boya — Detay İşlem',
    11: 'Boya Koruma — PPF Detay',
    12: 'Far Temizleme — Öncesi / Sonrası',
    13: 'Oto Boya — Profesyonel Boya',
    14: 'Seramik Kaplama — Nano',
    15: 'Far Parlatma — UV Koruma',
    16: 'Pasta Cila — Mükemmel Sonuç',
    17: 'Oto Boya — Kaput Boya',
    18: 'Boya Koruma — Nano Teknoloji',
}

def build_item(idx, src, alt, cat, cls_extra):
    cls = 'gallery-item'
    if cls_extra:
        cls += ' ' + cls_extra
    cls += ' reveal'
    lbl = display_labels.get(idx, alt)
    cat_label = cat_labels.get(cat, '')
    return f'''      <div class="{cls}" data-category="{cat}" onclick="openLightbox({idx})">
        <img src="{src}" alt="{alt}" loading="lazy">
        <div class="gallery-overlay">
          <div><span class="gallery-tag">{cat_label}</span>
            <div class="gallery-label">{lbl}</div>
          </div>
        </div>
        <div class="gallery-zoom">\U0001f50d</div>
      </div>'''

new_grid = '    <div class="gallery-grid">\n\n'
for item in items:
    new_grid += build_item(*item) + '\n\n'
new_grid += '    </div>\n  </section>'

old_grid_pattern = re.compile(r'<div class="gallery-grid">.*?</div>\s*</section>', re.DOTALL)
match = old_grid_pattern.search(text)
if match:
    text = text[:match.start()] + new_grid + text[match.end():]
    print(f'Gallery rebuilt: {len(items)} unique photos (duplicates removed)')
else:
    print('ERROR: gallery-grid not found')

with open('tolga-oto-boya-new.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Saved!')
