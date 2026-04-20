# 🛰️ WebReconX

**Gelişmiş Web Keşif & Güvenlik Analiz Aracı (Eğitim Amaçlı)**

---

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)
![Type](https://img.shields.io/badge/Tool-Recon%20%26%20Scanner-orange)
![Use](https://img.shields.io/badge/Use-Educational-important)

---

## 📌 Proje Hakkında

**WebReconX**, web hedefleri üzerinde çok yönlü keşif (reconnaissance) ve temel güvenlik analizi yapabilen Python tabanlı bir araçtır.

Araç, tek bir hedef üzerinde aşağıdaki işlemleri otomatik olarak gerçekleştirebilir:

* IP çözümleme ve Reverse DNS
* Cloudflare koruma tespiti
* Admin panel keşfi
* Port tarama ve servis analizi
* URL crawling (site haritalama)
* Parametre analizi

---

## 🚀 Özellikler

### 🌐 Hedef Analizi

* Domain veya direkt IP ile çalışabilir
* Otomatik IP çözümleme
* Reverse DNS desteği

---

### 🛡️ Cloudflare Tespiti

* Hedef IP, Cloudflare IP aralıkları ile karşılaştırılır
* Koruma varsa kullanıcıya uyarı verilir

---

### 🔎 Admin Panel Tarayıcı

* Wordlist tabanlı dizin taraması
* `/admin`, `/panel`, `/login` gibi path’leri dener
* 404 dışındaki yanıtları analiz eder

---

### 🚪 Port Tarama & Servis Analizi

* Kritik portlar üzerinde tarama yapar
* Açık portları tespit eder
* Her port için olası zafiyet açıklaması sunar

Örnek:

```id="port"
[+] Port 22 - SSH Brute force, weak keys
```

---

### 🕷️ URL Crawler

* Site içindeki linkleri otomatik toplar
* Maksimum 500 URL sınırı
* Aynı domain içindeki sayfaları filtreler

---

### 🔍 Parametre Analizi

* URL’lerdeki GET parametrelerini tespit eder
* Örnek:

```id="param"
example.com/page.php?id=1
```

---

### 📁 Filtreleme Sistemi

* URL’leri uzantıya göre filtreleme
* Örnek:

  * `.php`
  * `.html`

---

## 🛠️ Gereksinimler

```bash id="install"
pip install requests colorama user_agent beautifulsoup4
```

---

## 📂 Dosya Yapısı

```id="structure"
test.py
Wordlist.txt
founded_urls.txt
filtered_urls.txt
found_parameters.txt
```

---

## ⚙️ Kullanım

```bash id="run"
python test.py
```

---

## 🧪 Çalışma Akışı

1. Hedef site veya IP girilir
2. Sistem:

   * IP çözümleme yapar
   * Cloudflare kontrolü yapar
3. Admin panel taraması başlatılır
4. Port taraması yapılır
5. URL crawling başlar
6. Parametre analizi yapılır
7. Sonuçlar dosyalara kaydedilir

---

## 🧠 Çalışma Mantığı

### 1. IP & DNS Analizi

* `socket` kullanılarak IP çözülür
* Reverse lookup yapılır

---

### 2. Panel Keşfi

* Wordlist üzerinden brute dizin taraması
* HTTP response analiz edilir

---

### 3. Port Tarama

* `socket.connect_ex()` ile port kontrolü
* Açık portlar raporlanır

---

### 4. Crawling

* `BeautifulSoup` ile link extraction
* `urljoin` ile normalize edilir

---

### 5. Parametre Tespiti

* `urlparse` ve `parse_qs` ile analiz edilir

---

## ⚡ Geliştirme Planı

* [ ] Multi-threading (daha hızlı tarama)
* [ ] Proxy desteği
* [ ] Banner grabbing stabil hale getirme
* [ ] XSS / SQLi otomatik test modülü
* [ ] JSON / rapor export sistemi
* [ ] Subdomain tarama
* [ ] GUI arayüz

---

## 👨‍💻 Geliştirici

**Troll**

NOTE: *Iyi Avlar Arkadaslar*
