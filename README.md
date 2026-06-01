# 🚗 Tolga Oto Boya — Kurumsal Web Sitesi

> Profesyonel araç boyama ve oto detay hizmetleri için hazırlanmış modern, tek sayfalık kurumsal web sitesi.  
> **3.Sanayi, Zeybek, 1518. Sk. No:15 — 09100 Efeler / Aydın**

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Google Fonts](https://img.shields.io/badge/Google_Fonts-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://fonts.google.com/)
[![Google Maps](https://img.shields.io/badge/Google_Maps-4285F4?style=for-the-badge&logo=google-maps&logoColor=white)](https://maps.google.com)

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Teknolojiler](#-teknolojiler)
- [Proje Yapısı](#-proje-yapısı)
- [Hizmetler](#-hizmetler)
- [Sayfa Bölümleri](#-sayfa-bölümleri)
- [Kurulum](#-kurulum)
- [İletişim & Sosyal Medya](#-iletişim--sosyal-medya)
- [Geliştirici](#-geliştirici)

---

## 📌 Proje Hakkında

**Tolga Oto Boya**, 10+ yıllık deneyimiyle Aydın'da profesyonel araç boyama ve oto detay hizmetleri sunan bir atölyenin kurumsal tanıtım sitesidir. Site; sunulan hizmetleri, gerçek iş fotoğraflarını (13+ galeri görseli), atölye tanıtım videosunu ve doğrudan iletişim kanallarını modern bir tasarımla bir araya getirmektedir.

Herhangi bir framework veya build aracı **gerektirmez** — tamamen saf HTML, CSS ve JavaScript ile geliştirilmiştir. Mobil, tablet ve masaüstü cihazlarda eksiksiz çalışır.

---

## ✨ Özellikler

| Özellik | Açıklama |
|---------|----------|
| 🌑 **Dark Tema** | Kırmızı (`#cc0000`) & siyah (`#0a0a0a`) kurumsal renk paleti |
| 📱 **Tam Responsive** | Mobil (≤600px), tablet (≤900px) ve masaüstü için CSS Grid & Flexbox |
| 🖼️ **Lightbox Galeri** | Kategori filtrelemeli, klavye & dokunmatik kaydırma destekli |
| 🎬 **Video Bölümü** | Atölye tanıtım videosu gömülü `<video>` oynatıcı ile |
| 📊 **Animasyonlu Sayaçlar** | Scroll ile tetiklenen `requestAnimationFrame` tabanlı sayaç |
| 🍔 **Hamburger Menü** | Mobil için animasyonlu açılır navigasyon menüsü |
| 👁️ **Scroll Reveal** | `IntersectionObserver` ile sayfa kaydırmasında beliren elementler |
| ⬆️ **Yukarı Dön Butonu** | 400px scroll sonrası görünen, sol alt köşede sabit buton |
| 📍 **Google Maps** | Atölye konumu gömülü harita ile (Efeler/Aydın) |
| 💬 **WhatsApp Hızlı Mesaj** | Hazır mesaj metniyle doğrudan WhatsApp sohbeti açar |
| 📸 **Floating Instagram** | Sağ alt köşede sabit Instagram butonu |
| ⌨️ **Klavye Erişilebilirliği** | Lightbox `Escape`, `←`, `→` kısayol tuşlarını destekler |

---

## 🛠️ Teknolojiler

| Teknoloji | Sürüm / Detay | Kullanım Amacı |
|-----------|---------------|----------------|
| **HTML5** | Semantic — `<section>`, `<nav>`, `<footer>` | Sayfa yapısı, SEO, erişilebilirlik |
| **CSS3** | Vanilla CSS (CSS Grid, Flexbox, Custom Properties) | Tüm stiller, animasyonlar, responsive |
| **JavaScript** | ES6+ (arrow fn, `const/let`, optional chaining) | Galeri, lightbox, menü, sayaç, reveal |
| **Google Fonts** | Bebas Neue · Barlow · Barlow Condensed | Başlık ve gövde tipografisi |
| **Google Maps Embed** | iframe embed API | Konum haritası |
| **IntersectionObserver API** | Native browser API | Scroll reveal + sayaç animasyonu |
| **Touch Events API** | Native browser API | Lightbox'ta mobil kaydırma (swipe) |

---

## 📁 Proje Yapısı

```
TolgaOtoBoya-Website/
│
├── index.html              # Ana sayfa — tüm HTML yapısı + inline CSS + JS
├── style.css               # Harici yardımcı stiller
├── main.js                 # Harici JS (scroll progress, nav, galeri, lightbox)
│
├── images/                 # Galeri görselleri (13 adet .jpeg)
│   ├── galeri-01.jpeg      # Pasta Cila — Ayna Parlaklığı
│   ├── galeri-02.jpeg      # Pasta Cila — Derin Detay
│   ├── galeri-03.jpeg      # Oto Boya — Tam Karoser
│   ├── galeri-04.jpeg      # Oto Boya — Kapı & Tampon
│   ├── galeri-05.jpeg      # Boya Koruma — PPF Uygulama (geniş)
│   ├── galeri-06.jpeg      # Boya Koruma — Seramik
│   ├── galeri-08.jpeg      # Far Temizleme — Sonuç
│   ├── galeri-09.jpeg      # Pasta Cila — Atölye
│   ├── galeri-10.jpeg      # Oto Boya — Tam Araç (uzun)
│   ├── galeri-11.jpeg      # Oto Boya — Detay İşlem
│   ├── galeri-12.jpeg      # Boya Koruma — PPF Detay
│   ├── galeri-13.jpeg      # Far Temizleme — Öncesi/Sonrası (geniş)
│   └── galeri-19.jpeg      # Oto Boya — Kaput Boya
│
├── videos/                 # Atölye tanıtım videoları
│   ├── tanitim-video-1.mp4 # Yedek kaynak
│   └── tanitim-video-2.mp4 # Ana kaynak (öncelikli)
│
├── Resimler/               # Ham / kaynak görseller (yerel)
├── tolga oto boya.txt      # Proje istek notları
│
│   ── Yardımcı Python Scriptleri ──
├── check_far.py
├── copy_media.py
├── expand_gallery.py
├── extract_images.py
├── fix_gallery.py
├── fix_video_gallery.py
├── update_html_media.py
└── verify.py
```

---

## 🔧 Hizmetler

| # | Hizmet | Öne Çıkan Detaylar |
|---|--------|--------------------|
| 01 | **Oto Boya** | Tam karoser & parça boya, kaporta düzleştirme, orijinal renk eşleştirme, UV dayanımlı boya |
| 02 | **Boya Koruma** | Seramik kaplama, PPF (Boya Koruma Filmi), nano teknoloji koruma, UV & asit yağmur koruması |
| 03 | **Pasta Cila** | Makine pastası, tek & çift aşamalı polish, swirl çizik giderme, iç-dış detay temizlik |
| 04 | **Far Temizleme** | Mekanik zımpara & polish, UV kaplama ile koruma, sararma giderme, uzun süreli şeffaflık |

---

## 🗂️ Sayfa Bölümleri

Tek sayfalık yapının (`index.html`) bölümleri ve ID'leri:

| Bölüm | Anchor | İçerik |
|-------|--------|---------|
| **Hero** | `#hero` | Ana başlık, slogan, 500+ müşteri / 10+ yıl / %100 memnuniyet istatistikleri |
| **Tanıtım Videosu** | `#video` | Atölye tanıtım videosu + hizmet listesi özeti |
| **Hizmetlerimiz** | `#hizmetler` | 4 hizmet kartı (hover animasyonlu) |
| **Çalışmalarımız** | `#galeri` | Filtreli lightbox galeri (Tümü / Oto Boya / Pasta Cila / Boya Koruma / Far Temizleme) |
| **Neden Biz?** | `#neden-biz` | 6 öne çıkan özellik (Deneyim, Ekipman, Renk Garantisi, Hızlı Teslimat, Kalite, Konum) |
| **İletişim** | `#iletisim` | Adres (Maps bağlantılı), telefon, WhatsApp, çalışma saatleri + gömülü harita |

---

## 🚀 Kurulum

Herhangi bir bağımlılık kurulumu veya build adımı **gerekmez**.

```bash
# 1. Depoyu klonlayın
git clone https://github.com/MuratEfeCamoglu/TolgaOtoBoya-Website.git

# 2. Proje klasörüne girin
cd TolgaOtoBoya-Website

# 3. index.html'i doğrudan tarayıcıda açın
#    — ya da VS Code Live Server eklentisi ile çalıştırın (önerilir)
```

> **Not:** `images/` ve `videos/` klasörleri büyük medya dosyaları içerdiğinden Git geçmişinde yer almıyor olabilir. Bu klasörleri yerel olarak manuel ekleyiniz.

---

## 📞 İletişim & Sosyal Medya

| Kanal | Bilgi / Link |
|-------|-------------|
| 📍 **Adres** | [3.Sanayi, Zeybek, 1518. Sk. No:15, 09100 Efeler / Aydın](https://maps.google.com/?q=3.+Sanayi+Zeybek+1518.+Sk.+No:15+Efeler+Aydin) |
| 📞 **Telefon** | [0505 968 85 09](tel:+905059688509) |
| 💬 **WhatsApp** | [Mesaj Gönder](https://wa.me/905059688509?text=Merhaba%2C%20Tolga%20Oto%20Boya%20hakk%C4%B1nda%20bilgi%20almak%20istiyorum.) |
| 📸 **Instagram** | [@tolga.camoglu](https://www.instagram.com/tolga.camoglu) |
| 🕐 **Çalışma Saatleri** | Pzt – Cmt: 08:30 – 19:00 · Pazar: Kapalı |

---

## 👨‍💻 Geliştirici

Bu proje **[MuratEfeCamoglu](https://github.com/MuratEfeCamoglu)** tarafından geliştirilmiştir.

---

## 📄 Lisans

Bu proje özel kullanım amaçlıdır. Tüm hakları saklıdır © 2025 Tolga Oto Boya — Efeler / Aydın.
