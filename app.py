import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import date, timedelta

st.title("Basit Hisse Senedi Fiyat Grafiği")

# Kullanıcının seçebileceği hisseler
hisseler = {
    "Apple": "AAPL",
    "Coca-Cola": "KO"
}

# Açılır menü (selectbox) oluşturma
secilen_hisse_adi = st.selectbox("Lütfen bir hisse senedi seçin:", list(hisseler.keys()))
secilen_sembol = hisseler[secilen_hisse_adi]



# Tarih aralığını belirleme (Son 1 yıl)
bitis_tarihi = date.today()
baslangic_tarihi = bitis_tarihi - timedelta(days=365)

# Veriyi çekme fonksiyonu (hızlandırmak için cache kullanıyoruz)
@st.cache_data
def veri_getir(sembol, baslangic, bitis):
    # yfinance ile veriyi indiriyoruz
    hisse_verisi = yf.download(sembol, start=baslangic, end=bitis)
    return hisse_verisi

# Seçilen hissenin verisini indir
veri = veri_getir(secilen_sembol, baslangic_tarihi, bitis_tarihi)

# Veriyi kontrol edip çizdirme
if not veri.empty:
    # yfinance son sürümlerde sütunları MultiIndex (çoklu yapı) dönebiliyor
    kapanis = veri['Close']
    if isinstance(veri.columns, pd.MultiIndex):
        kapanis = kapanis[secilen_sembol]
        
    # Plotly ile interaktif ve şık çizgi grafik (line chart) oluşturma
    fig = px.line(
        kapanis, 
        title=f"{secilen_hisse_adi} ({secilen_sembol}) Son 1 Yıllık Kapanış Fiyatları",
        labels={"Date": "Tarih", "value": "Kapanış Fiyatı (USD)"}
    )
    
    # Grafiği daha şık hale getirmek için görünüm ayarları
    fig.update_layout(
        xaxis_title="Tarih",
        yaxis_title="Kapanış Fiyatı (USD)",
        hovermode="x unified", # Fare üzerine gelince eksendeki detayları gösterir
        showlegend=False,
        title_font_size=20,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    # Çizgi rengini ve kalınlığını ayarlama (Plotly klasik mavisi)
    fig.update_traces(line_color="#1f77b4", line_width=3)
    
    # Streamlit üzerinde gösterme (use_container_width sayesinde grafiği ekrana yayar)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Veri çekilemedi veya seçilen tarih aralığında veri yok.")
