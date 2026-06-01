with open('tolga-oto-boya-new.html', encoding='utf-8') as f:
    text = f.read()

# ── 1. Replace YouTube iframe with local HTML5 video player ──
old_video_div = '''      <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;border-radius:4px;border:2px solid rgba(204,0,0,0.4);">
        <iframe
          src="https://www.youtube.com/embed/dQw4w9WgXcQ?rel=0&modestbranding=1"
          title="Tolga Oto Boya Tanıtım Videosu"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
          loading="lazy"
          style="position:absolute;top:0;left:0;width:100%;height:100%;"
        ></iframe>
      </div>'''

new_video_div = '''      <div style="position:relative;border-radius:4px;border:2px solid rgba(204,0,0,0.4);overflow:hidden;background:#000;">
        <video
          controls
          preload="metadata"
          poster="images/galeri-01.jpeg"
          style="width:100%;display:block;max-height:480px;object-fit:cover;"
        >
          <source src="videos/tanitim-video-1.mp4" type="video/mp4">
          <source src="videos/tanitim-video-2.mp4" type="video/mp4">
          Tarayıcınız video etiketini desteklemiyor.
        </video>
      </div>'''

if old_video_div in text:
    text = text.replace(old_video_div, new_video_div)
    print('Video section updated')
else:
    print('WARNING: Video section not found')

# ── 2. Build new gallery grid with 9 local images ──
gallery_items = [
    # (index, src, alt, category, classes)
    (0, 'images/galeri-01.jpeg', 'Pasta Cila Uygulaması', 'pasta-cila', 'tall'),
    (1, 'images/galeri-02.jpeg', 'Pasta Cila Detay', 'pasta-cila', ''),
    (2, 'images/galeri-03.jpeg', 'Oto Boya Karoser', 'oto-boya', ''),
    (3, 'images/galeri-04.jpeg', 'Far Temizleme', 'far-temizleme', ''),
    (4, 'images/galeri-05.jpeg', 'Boya Koruma PPF', 'boya-koruma', 'wide'),
    (5, 'images/galeri-06.jpeg', 'Oto Boya Atölye', 'oto-boya', 'tall'),
    (6, 'images/galeri-07.jpeg', 'Far Parlatma Sonucu', 'far-temizleme', ''),
    (7, 'images/galeri-08.jpeg', 'Seramik Kaplama', 'boya-koruma', ''),
    (8, 'images/galeri-09.jpeg', 'Tolga Oto Boya Atölye', 'pasta-cila', ''),
]

cat_labels = {
    'pasta-cila': 'Pasta Cila',
    'oto-boya': 'Oto Boya',
    'boya-koruma': 'Boya Koruma',
    'far-temizleme': 'Far Temizleme',
}

gallery_labels = {
    0: 'Pasta Cila — Ayna Parlaklığı',
    1: 'Pasta Cila — Detay',
    2: 'Oto Boya — Tam Karoser',
    3: 'Far Parlatma — Öncesi/Sonrası',
    4: 'Boya Koruma — PPF Uygulama',
    5: 'Oto Boya — Atölye Çalışması',
    6: 'Far Temizleme — Sonuç',
    7: 'Seramik Kaplama — Koruma',
    8: 'Tolga Oto Boya — Aydın',
}

def build_item(idx, src, alt, cat, classes):
    cls_extra = (' ' + classes) if classes else ''
    cat_label = cat_labels.get(cat, '')
    lbl = gallery_labels.get(idx, alt)
    return f'''      <div class="gallery-item{cls_extra} reveal" data-category="{cat}" onclick="openLightbox({idx})">
        <img src="{src}" alt="{alt}" loading="lazy">
        <div class="gallery-overlay">
          <div><span class="gallery-tag">{cat_label}</span>
            <div class="gallery-label">{lbl}</div>
          </div>
        </div>
        <div class="gallery-zoom">🔍</div>
      </div>'''

new_grid_html = '\n    <div class="gallery-grid">\n\n'
for item in gallery_items:
    new_grid_html += build_item(*item) + '\n\n'
new_grid_html += '    </div>'

# Find and replace the entire gallery-grid
import re
old_grid_pattern = re.compile(r'<div class="gallery-grid">.*?</div>\n\s*</section>', re.DOTALL)
match = old_grid_pattern.search(text)
if match:
    # We need to keep the </section> part
    new_grid_with_section = new_grid_html + '\n  </section>'
    text = text[:match.start()] + new_grid_with_section + text[match.end():]
    print('Gallery grid updated with 9 local images')
else:
    print('WARNING: gallery-grid not found')

with open('tolga-oto-boya-new.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Done! File saved.')
