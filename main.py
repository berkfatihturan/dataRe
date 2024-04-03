import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# # Excel dosyasını oku
# veri = pd.read_excel("data.xlsx")
#
# # "model" sütunundaki en çok tekrar eden değeri bul
# en_cok_tekrar_eden = veri['Model'].mode()[0]
#
# # En çok tekrar eden değerin tekrar sayısını bul
# tekrar_sayisi = veri['Model'].value_counts()[en_cok_tekrar_eden]
#
# # En çok tekrar eden "model"e sahip olanları seç
# filtre = veri['Model'] == en_cok_tekrar_eden
# en_cok_tekrar_eden_veri = veri[filtre]
#
# # Yeni bir Excel dosyasına yaz
# en_cok_tekrar_eden_veri.to_excel("en_cok_tekrar_eden_veri.xlsx", index=False)
#
# print(f"'model' sütunundaki en çok tekrar eden değere sahip veriler 'en_cok_tekrar_eden_veri.xlsx' dosyasına kaydedildi.")
#
# print(f"'model' sütunundaki en çok tekrar eden değer: {en_cok_tekrar_eden}, Tekrar sayısı: {tekrar_sayisi}")

df = pd.read_excel('en_cok_tekrar_eden_veri.xlsx')

# 2013 yılına ait verileri filtrele
veri_2013 = df[df['Yıl'] == 2013]

# Yıl, fiyat ve model verilerini al
kilometre = veri_2013['Kilometre']
fiyat = veri_2013['Fiyat']
model = veri_2013['Seri']

# Model sütunundaki farklı değerleri al
farkli_modeller = veri_2013['Seri'].unique()

# Her bir model için farklı renkler belirle
renkler = plt.cm.rainbow(range(len(farkli_modeller)))

# Grafik çizimi
plt.figure(figsize=(10, 6))
for i, model in enumerate(farkli_modeller):
    filtre = veri_2013['Seri'] == model
    plt.scatter(kilometre[filtre], fiyat[filtre], color=renkler[i], alpha=0.7, label=model)

plt.title('Kilometre-Fiyat Grafiği (2013)')
plt.xlabel('Kilometre')
plt.ylabel('Fiyat')
plt.grid(True)
plt.legend()
plt.show()