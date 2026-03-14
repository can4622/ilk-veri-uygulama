# 📈 Canlı Hisse Senedi Analiz Paneli

Bu proje, global şirketlerin (Apple, Coca-Cola vb.) anlık borsa verilerini API üzerinden çekerek, kullanıcıya temiz ve interaktif bir çizgi grafik sunan Python tabanlı bir web uygulamasıdır. Amacı, ham finansal veriyi hızlıca işleyip son kullanıcı için anlaşılır bir arayüze (Dashboard) dönüştürmektir.


## 🛠️ Kullanılan Teknolojiler
* **Python:** Ana programlama dili.
* **Streamlit:** Hızlı ve modern web arayüzü (UI) tasarımı.
* **yfinance & Pandas:** Canlı borsa verilerinin çekilmesi ve veri manipülasyonu.
* **Plotly:** İnteraktif ve dinamik grafik oluşturma.

## 💻 Nasıl Çalıştırılır?
Projeyi bilgisayarına indirdikten sonra terminale şu iki komutu yazman yeterli:

```bash
pip install -r requirements.txt
streamlit run app.py
