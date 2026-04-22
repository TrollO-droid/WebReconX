# 🛰️ WebReconX

**Gelişmiş Web Keşif & Güvenlik Analiz Aracı (Eğitim Amaçlı)**

---

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Type](https://img.shields.io/badge/Tool-Web%20Recon-orange)
![Version](https://img.shields.io/badge/Version-2.0-important)

---

## 📌 Proje Hakkında

**WebReconX**, tek bir hedef üzerinde çok aşamalı keşif (recon) işlemleri gerçekleştiren, Python tabanlı bir analiz aracıdır.

Araç aşağıdaki süreçleri otomatik olarak yürütür:

* IP çözümleme & Reverse DNS
* Cloudflare koruma tespiti
* Admin panel keşfi (gelişmiş kontrol)
* Port tarama & servis analizi
* URL crawling (maks. 500 URL)
* URL filtreleme
* Parametre (GET) analizi

---

## 🚀 Özellikler

### 🌐 Hedef & Ağ Analizi

* Domain veya IP desteği
* Otomatik IP çözümleme (`socket`)
* Reverse DNS lookup

---

### 🛡️ Cloudflare Tespiti

* Geniş IP range listesi ile kontrol
* Cloudflare arkasındaki hedeflerde kullanıcıya seçim sunar

---

### 🔎 Gelişmiş Admin Panel Tespiti

* Wordlist tabanlı dizin tarama
* Sadece status code değil, içerik analizi yapar:

✔ Login form kontrolü
✔ `<input type="password">` tespiti
✔ Form + password kombinasyonu
✔ Redirect analizleri
✔ 403 → olası panel

---

### 🚪 Port Tarama & Servis Analizi

* Kritik port listesi ile hızlı tarama
* Açık portları tespit eder
* Her port için açıklama sunar

Örnek:

```id="port"
[+] Port 22 - SSH Brute force, weak keys is Open
```

---

### 🕷️ URL Crawler

* Aynı domain içindeki linkleri toplar
* `BeautifulSoup` ile parsing
* Maksimum 500 URL limiti

✔ Tekrar eden URL’leri filtreler
✔ Otomatik dosyaya kayıt

---

### 📁 URL Filtreleme

* Uzantıya göre filtreleme yapılabilir

Örnek:

```id="filter"
.php
.html
```

---

### 🔍 Parametre Analizi

* URL içerisindeki GET parametreleri tespit edilir

Örnek:

```id="param"
site.com/page.php?id=1
```

* Parametreler dosyaya kaydedilebilir
* SQLi / XSS testleri için temel veri sağlar

---

## 🛠️ Gereksinimler

```bash id="install"
pip install requests colorama user_agent beautifulsoup4
```

---

## 📂 Dosya Yapısı

```id="structure"
main.py (veya script dosyan)
Wordlist.txt
founded_urls.txt
filtered_urls.txt
found_parameters.txt
```

---

## ⚙️ Kullanım

```bash id="run"
python main.py
```

---

## 🧪 Çalışma Akışı

1. Hedef (domain veya IP) girilir
2. Sistem:

   * IP çözümleme yapar
   * Reverse DNS kontrol eder
3. Cloudflare tespiti yapılır
4. Admin panel taraması başlar
5. Port taraması gerçekleştirilir
6. URL crawling başlatılır
7. URL filtreleme opsiyonu sunulur
8. Parametre analizi yapılır
9. Sonuçlar dosyalara kaydedilir

---

## 🧠 Teknik Detaylar

### Admin Panel Detection

* Status code + içerik bazlı analiz
* Form input kontrolü
* Redirect parsing

---

### Port Scanning

* `socket.connect_ex()` kullanır
* Timeout ile optimize edilmiştir

---

### Crawling Mekanizması

* BFS mantığı ile çalışır
* `visited_urls` ile tekrarları engeller

---

### Parametre Parsing

* `urlparse` + `parse_qs` kullanılır

---

## ⚡ Geliştirme Planı

* [ ] Multi-threading (hız artışı)
* [ ] Banner grabbing stabil hale getirme
* [ ] Proxy desteği
* [ ] Subdomain keşfi
* [ ] XSS / SQLi otomatik test modülü
* [ ] JSON / rapor çıktısı
* [ ] CLI argüman desteği

---

## ⚠️ Sınırlamalar

* Cloudflare arkasındaki gerçek IP tespit edilmez
* Rate limit durumlarında yavaşlayabilir
* JavaScript tabanlı sitelerde crawling sınırlı olabilir
* CAPTCHA bypass içermez

---

## 👨‍💻 Geliştirici

**Troll**

---

> Bu araç bir exploit aracı değil, bir keşif (recon) aracıdır.
> Gerçek güvenlik analizi, çıkan verilerin doğru yorumlanmasına bağlıdır.
