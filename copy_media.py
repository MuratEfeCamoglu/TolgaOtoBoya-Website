import shutil, os

src = 'Resimler'
os.makedirs('images', exist_ok=True)
os.makedirs('videos', exist_ok=True)

# Map source filenames -> clean destination names + category
image_map = [
    ('WhatsApp Image 2026-05-21 at 15.07.19.jpeg',      'images/galeri-01.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-05-21 at 15.07.19 (1).jpeg',  'images/galeri-02.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-05-21 at 15.07.21.jpeg',      'images/galeri-03.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-05-21 at 15.07.21 (1).jpeg',  'images/galeri-04.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-05-21 at 15.07.44.jpeg',      'images/galeri-05.jpeg', 'boya-koruma'),
    ('WhatsApp Image 2026-05-21 at 15.07.45.jpeg',      'images/galeri-06.jpeg', 'boya-koruma'),
    ('WhatsApp Image 2026-05-21 at 15.08.50.jpeg',      'images/galeri-07.jpeg', 'far-temizleme'),
    ('WhatsApp Image 2026-05-21 at 15.08.51.jpeg',      'images/galeri-08.jpeg', 'far-temizleme'),
    ('WhatsApp Image 2026-05-21 at 15.09.06.jpeg',      'images/galeri-09.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-05-21 at 15.09.07.jpeg',      'images/galeri-10.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-05-21 at 15.09.07 (1).jpeg',  'images/galeri-11.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-05-21 at 15.09.07 (2).jpeg',  'images/galeri-12.jpeg', 'boya-koruma'),
    ('WhatsApp Image 2026-05-21 at 15.09.07 (3).jpeg',  'images/galeri-13.jpeg', 'far-temizleme'),
    # April images as extras
    ('WhatsApp Image 2026-04-16 at 15.06.54.jpeg',      'images/galeri-14.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-04-16 at 15.06.54 (1).jpeg',  'images/galeri-15.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-04-16 at 15.06.54 (2).jpeg',  'images/galeri-16.jpeg', 'boya-koruma'),
    ('WhatsApp Image 2026-04-16 at 15.06.54 (3).jpeg',  'images/galeri-17.jpeg', 'far-temizleme'),
    ('WhatsApp Image 2026-04-16 at 15.06.55.jpeg',      'images/galeri-18.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (1).jpeg',  'images/galeri-19.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (2).jpeg',  'images/galeri-20.jpeg', 'boya-koruma'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (3).jpeg',  'images/galeri-21.jpeg', 'far-temizleme'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (4).jpeg',  'images/galeri-22.jpeg', 'pasta-cila'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (5).jpeg',  'images/galeri-23.jpeg', 'oto-boya'),
    ('WhatsApp Image 2026-04-16 at 15.06.55 (6).jpeg',  'images/galeri-24.jpeg', 'boya-koruma'),
]

video_map = [
    ('WhatsApp Video 2026-05-21 at 15.08.50.mp4', 'videos/tanitim-video-1.mp4'),
    ('WhatsApp Video 2026-05-21 at 15.08.51.mp4', 'videos/tanitim-video-2.mp4'),
]

for src_name, dst, cat in image_map:
    src_path = os.path.join(src, src_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst)
        print(f'Copied: {src_name} -> {dst} [{cat}]')
    else:
        print(f'MISSING: {src_name}')

for src_name, dst in video_map:
    src_path = os.path.join(src, src_name)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst)
        print(f'Copied video: {src_name} -> {dst}')
    else:
        print(f'MISSING video: {src_name}')

print('\nDone!')
