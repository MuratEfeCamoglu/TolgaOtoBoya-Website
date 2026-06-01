with open('tolga-oto-boya-new.html', encoding='utf-8') as f:
    text = f.read()

# Find the gallery-grid section and replace with expanded gallery
cat_labels = {
    'pasta-cila': 'Pasta Cila',
    'oto-boya': 'Oto Boya',
    'boya-koruma': 'Boya Koruma',
    'far-temizleme': 'Far Temizleme',
}

# All 24 images with categories - varied layout
# (idx, src, alt, category, extra_class)
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
    (13, 'images/galeri-14.jpeg',  'Pasta Cila Parlatma',           'pasta-cila',    ''),
    (14, 'images/galeri-15.jpeg',  'Oto Boya Çalışma',              'oto-boya',      ''),
    (15, 'images/galeri-16.jpeg',  'Seramik Kaplama',               'boya-koruma',   ''),
    (16, 'images/galeri-17.jpeg',  'Far Parlatma',                  'far-temizleme', ''),
    (17, 'images/galeri-18.jpeg',  'Pasta Cila Sonuç',              'pasta-cila',    'tall'),
    (18, 'images/galeri-19.jpeg',  'Oto Boya Kaput',                'oto-boya',      ''),
    (19, 'images/galeri-20.jpeg',  'PPF Koruma Filmi',              'boya-koruma',   ''),
    (20, 'images/galeri-21.jpeg',  'Far Temizleme Profesyonel',     'far-temizleme', ''),
    (21, 'images/galeri-22.jpeg',  'Pasta Cila Mükemmel Sonuç',     'pasta-cila',    ''),
    (22, 'images/galeri-23.jpeg',  'Oto Boya Tam İş',               'oto-boya',      'wide'),
    (23, 'images/galeri-24.jpeg',  'Boya Koruma Nano',              'boya-koruma',   ''),
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
    13: 'Pasta Cila — Parlatma',
    14: 'Oto Boya — Profesyonel Boya',
    15: 'Seramik Kaplama — Nano',
    16: 'Far Parlatma — UV Koruma',
    17: 'Pasta Cila — Mükemmel Sonuç',
    18: 'Oto Boya — Kaput Boya',
    19: 'PPF Boya Koruma Filmi',
    20: 'Far Temizleme — Profesyonel',
    21: 'Pasta Cila — Ayna Yüzey',
    22: 'Oto Boya — Tam Araç Boya',
    23: 'Boya Koruma — Nano Teknoloji',
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

import re
old_grid_pattern = re.compile(r'<div class="gallery-grid">.*?</div>\s*</section>', re.DOTALL)
match = old_grid_pattern.search(text)
if match:
    text = text[:match.start()] + new_grid + text[match.end():]
    print(f'Gallery updated: {len(items)} photos added')
else:
    print('ERROR: gallery-grid not found')

with open('tolga-oto-boya-new.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Saved!')
