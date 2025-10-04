import tkinter as tk
from tkinter import messagebox, simpledialog

# MASALAR
tables = {i: {"adisyon_acik": False, "siparisler": [], "toplam": 0} for i in range(1, 21)}

# GÜNLÜK CİRO
gunluk_ciro = 0

menu = {
    # Dilim Tatlılar
    "Dilim Tatlı": 80,
    "Dark Velvet": 80,
    "Red Velvet": 80,
    "Frambuazlı Trileçe": 80,
    "Çikolatalı Trileçe": 80,
    "Karamelli Trileçe": 80,
    "Soğuk Kadayıf": 80,
    "Tiramisu": 80,
    
    # Kap Tatlılar
    "Kap Tatlı": 80,
    "Antep Fıstıklı M.": 80,
    "Lotuslu M.": 80,
    "Muzlu M.": 80,
    "Çilekli M.":80,
    "İtalyan Karamelli M.": 80,
    "Profiterol": 80,
    "Supangle": 80,
    "Sütlaç": 80,
    
    # İçecekler
    "Soda": 25,
    "Meyveli Soda": 30,
    "Su": 10
}

root = tk.Tk()
root.title("Çalışan Paneli - TRITAT")
root.geometry("1200x700")  # Ekran boyutu küçültüldü
root.resizable(False, False)
root.configure(bg="#f5f5f5")

secilen_masa = tk.IntVar()
secilen_masa.set(0)

# RENKLER
soft_red = "#f28b82"
soft_green = "#81c995"
soft_blue = "#a0c4ff"
soft_orange = "#ffb77d"
soft_purple = "#c59aff"
soft_gray = "#d3d3d3"
highlight_color = "#ffd966"
soft_white = "#ffffff"

# ÜST BİLGİ PANELİ
ust_panel = tk.Frame(root, bg="#2c3e50", height=70)  # Yükseklik küçültüldü
ust_panel.pack(fill="x")
ust_panel.pack_propagate(False)

# Logo/Başlık
baslik_frame = tk.Frame(ust_panel, bg="#2c3e50")
baslik_frame.pack(side="left", padx=15, pady=10)  # Padding küçültüldü

tk.Label(baslik_frame, text="TRITAT", font=("Arial", 18, "bold"),  # Font küçültüldü
         bg="#2c3e50", fg="#ecf0f1").pack()
tk.Label(baslik_frame, text="Restoran Yönetim Sistemi", font=("Arial", 8), 
         bg="#2c3e50", fg="#bdc3c7").pack()

# Durum bilgileri
durum_frame = tk.Frame(ust_panel, bg="#2c3e50")
durum_frame.pack(side="left", padx=30, pady=10)  # Padding küçültüldü

def temizle_orta_panel():
    for widget in orta_panel.winfo_children():
        widget.destroy()

def guncelle_durum_bilgileri():
    for widget in durum_frame.winfo_children():
        widget.destroy()
    
    acik_masa_sayisi = sum(1 for masa in tables.values() if masa["adisyon_acik"])
    
    bilgi_frame1 = tk.Frame(durum_frame, bg="#2c3e50")
    bilgi_frame1.pack(side="top", fill="x")
    
    tk.Label(bilgi_frame1, text="Açık Masalar:", font=("Arial", 9), 
             bg="#2c3e50", fg="#bdc3c7").pack(side="left")
    tk.Label(bilgi_frame1, text=f"{acik_masa_sayisi}/20", font=("Arial", 10, "bold"), 
             bg="#2c3e50", fg="#e74c3c").pack(side="left", padx=(5,0))
    
    bilgi_frame2 = tk.Frame(durum_frame, bg="#2c3e50")
    bilgi_frame2.pack(side="top", fill="x")
    
    tk.Label(bilgi_frame2, text="Günlük Ciro:", font=("Arial", 9), 
             bg="#2c3e50", fg="#bdc3c7").pack(side="left")
    tk.Label(bilgi_frame2, text=f"{gunluk_ciro} TL", font=("Arial", 10, "bold"), 
             bg="#2c3e50", fg="#27ae60").pack(side="left", padx=(5,0))

guncelle_durum_bilgileri()

# Seçili masa bilgisi
secili_masa_frame = tk.Frame(ust_panel, bg="#2c3e50")
secili_masa_frame.pack(side="right", padx=15, pady=8)

secili_masa_label = tk.Label(secili_masa_frame, text="Masa Seçilmedi", 
                            font=("Arial", 10, "bold"), bg="#2c3e50", fg="#f39c12")
secili_masa_label.pack()

masa_siparis_label = tk.Label(secili_masa_frame, text="", 
                             font=("Arial", 8), bg="#2c3e50", fg="#ecf0f1")
masa_siparis_label.pack()


def guncelle_secili_masa_bilgisi():
    masa_no = secilen_masa.get()
    if masa_no == 0:
        secili_masa_label.config(text="Masa seçilmedi")
        masa_siparis_label.config(text="")
        return

    masa = tables[masa_no]
    if masa["adisyon_acik"]:
        siparis_sayisi = len(masa["siparisler"])
        toplam_adet = sum(s['adet'] for s in masa["siparisler"])
        secili_masa_label.config(text=f"Masa {masa_no} | Adisyon AÇIK")
        masa_siparis_label.config(text=f"{siparis_sayisi} Sipariş - {toplam_adet} adet - {masa['toplam']} TL")
    else:
        secili_masa_label.config(text=f"Masa {masa_no} | Adisyon Kapalı")
        masa_siparis_label.config(text="")

# ANA CONTAINER
main_container = tk.Frame(root, bg="#f5f5f5")
main_container.pack(fill="both", expand=True, padx=8, pady=8)

# SOL PANEL - MASALAR
sol_panel = tk.Frame(main_container, bg="#f5f5f5", width=450)  # Genişlik küçültüldü
sol_panel.pack(side="left", fill="y", padx=(0,8))
sol_panel.pack_propagate(False)

# SAĞ PANEL - İŞLEMLER VE ORTA ALAN
sag_panel = tk.Frame(main_container, bg="#f5f5f5")
sag_panel.pack(side="right", fill="both", expand=True)

# ORTA PANEL
orta_panel = tk.Frame(sag_panel, bg="#fafafa", relief="ridge", bd=1)
orta_panel.pack(fill="both", expand=True, pady=(0,8))

def temizle_orta_panel():
    for widget in orta_panel.winfo_children():
        widget.destroy()

def siparisleri_goster():
    temizle_orta_panel()
    masa_no = secilen_masa.get()
    if masa_no == 0:
        tk.Label(orta_panel, text="Lütfen bir masa seçin", font=("Arial", 14), bg="#fafafa", fg="gray").pack(pady=50)
        return

    masa = tables[masa_no]
    if not masa["siparisler"]:
        tk.Label(orta_panel, text="Henüz sipariş yok", font=("Arial", 14), bg="#fafafa", fg="gray").pack(pady=50)
        return

    # Başlık
    baslik_frame = tk.Frame(orta_panel, bg="#fafafa")
    baslik_frame.pack(pady=8, fill="x", padx=15)
    
    tk.Label(baslik_frame, text=f"Masa {masa_no} Siparişleri", 
             font=("Arial", 14, "bold"), bg="#fafafa", fg="#2c3e50").pack(side="left")
    
    # Toplam tutar
    if masa["toplam"] > 0:
        tk.Label(baslik_frame, text=f"Toplam: {masa['toplam']} TL", 
                 font=("Arial", 12, "bold"), bg="#fafafa", fg="#e74c3c").pack(side="right")

    # Siparişler listesi
    siparis_frame = tk.Frame(orta_panel, bg="#fafafa")
    siparis_frame.pack(pady=8, fill="both", expand=True, padx=15)
    
    # Başlık satırı
    baslik_kutu = tk.Frame(siparis_frame, bg="#34495e", height=35)
    baslik_kutu.pack(fill="x", pady=(0,3))
    baslik_kutu.pack_propagate(False)
    
    tk.Label(baslik_kutu, text="Adet", font=("Arial", 9, "bold"), 
             bg="#34495e", fg="white", width=6).pack(side="left", padx=8, pady=6)
    tk.Label(baslik_kutu, text="Ürün", font=("Arial", 9, "bold"), 
             bg="#34495e", fg="white", width=22).pack(side="left", padx=8, pady=6)
    tk.Label(baslik_kutu, text="Birim Fiyat", font=("Arial", 9, "bold"), 
             bg="#34495e", fg="white", width=10).pack(side="left", padx=8, pady=6)
    tk.Label(baslik_kutu, text="Toplam", font=("Arial", 9, "bold"), 
             bg="#34495e", fg="white", width=8).pack(side="left", padx=8, pady=6)

    for idx, sip in enumerate(masa["siparisler"]):
        kutu = tk.Frame(siparis_frame, bg=soft_white, bd=1, relief="ridge", height=30)
        kutu.pack(fill="x", pady=1)
        kutu.pack_propagate(False)
        
        # Adet
        tk.Label(kutu, text=f"{sip['adet']}", width=6, font=("Arial", 10), 
                 bg=soft_white, fg="#2c3e50").pack(side="left", padx=8, pady=4)
        
        # Ürün adı
        tk.Label(kutu, text=sip['urun'], width=22, font=("Arial", 10), 
                 bg=soft_white, fg="#2c3e50", anchor="w").pack(side="left", padx=8, pady=4)
        
        # Birim fiyat
        birim_fiyat = sip['tutar'] // sip['adet']
        tk.Label(kutu, text=f"{birim_fiyat} TL", width=10, font=("Arial", 10), 
                 bg=soft_white, fg="#7f8c8d").pack(side="left", padx=8, pady=4)
        
        # Toplam tutar
        tk.Label(kutu, text=f"{sip['tutar']} TL", width=8, font=("Arial", 10, "bold"), 
                 bg=soft_white, fg="#e74c3c").pack(side="left", padx=8, pady=4)


def siparis_ekle():
    """Sipariş ekleme ekranı - geliştirilmiş versiyon"""
    temizle_orta_panel()
    masa_no = secilen_masa.get()
    if masa_no == 0:
        tk.Label(orta_panel, text="Lütfen bir masa seçin", font=("Arial", 14), bg="#fafafa", fg="gray").pack(pady=50)
        return

    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        masa["adisyon_acik"] = True
        masa["siparisler"] = []
        masa["toplam"] = 0
        update_buttons()
        guncelle_secili_masa_bilgisi()
        guncelle_durum_bilgileri()

    # Başlık
    tk.Label(orta_panel, text=f"Masa {masa_no} - Sipariş Ekle", 
             font=("Arial", 14, "bold"), bg="#fafafa", fg="#2c3e50").pack(pady=10)

    # Ana container
    main_siparis_frame = tk.Frame(orta_panel, bg="#fafafa")
    main_siparis_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Sol taraf - menü butonları
    menu_frame = tk.Frame(main_siparis_frame, bg="#fafafa")
    menu_frame.pack(side="left", fill="both", expand=True)

    # Sağ taraf - adet kontrolü ve ekleme
    kontrol_frame = tk.Frame(main_siparis_frame, bg="#e8f4fd", bd=2, relief="ridge", width=200)
    kontrol_frame.pack(side="right", fill="y", padx=(20,0))
    kontrol_frame.pack_propagate(False)

    # Seçili ürün ve adet kontrolü
    tk.Label(kontrol_frame, text="Seçili Ürün:", font=("Arial", 11, "bold"), 
             bg="#e8f4fd", fg="#2c3e50").pack(pady=(10,5))
    
    secili_urun_label = tk.Label(kontrol_frame, text="Ürün seçiniz", 
                                font=("Arial", 10), bg="#e8f4fd", fg="#7f8c8d")
    secili_urun_label.pack(pady=5)

    # Adet kontrolü
    tk.Label(kontrol_frame, text="Adet:", font=("Arial", 11, "bold"), 
             bg="#e8f4fd", fg="#2c3e50").pack(pady=(15,5))

    adet_frame = tk.Frame(kontrol_frame, bg="#e8f4fd")
    adet_frame.pack(pady=5)

    adet_var = tk.IntVar(value=1)
    
    def adet_azalt():
        if adet_var.get() > 1:
            adet_var.set(adet_var.get() - 1)
    
    def adet_arttir():
        if adet_var.get() < 50:
            adet_var.set(adet_var.get() + 1)

    btn_azalt = tk.Button(adet_frame, text="-", width=3, height=1,
                         bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                         command=adet_azalt)
    btn_azalt.pack(side="left", padx=2)

    adet_entry = tk.Entry(adet_frame, textvariable=adet_var, width=5, justify="center",
                         font=("Arial", 12))
    adet_entry.pack(side="left", padx=2)

    btn_arttir = tk.Button(adet_frame, text="+", width=3, height=1,
                          bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                          command=adet_arttir)
    btn_arttir.pack(side="left", padx=2)

    # Toplam tutar
    toplam_label = tk.Label(kontrol_frame, text="Toplam: 0 TL", 
                           font=("Arial", 11, "bold"), bg="#e8f4fd", fg="#e74c3c")
    toplam_label.pack(pady=(15,10))

    # Ekle butonu
    ekle_btn = tk.Button(kontrol_frame, text="Sepete Ekle", width=15, height=2,
                        bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                        state="disabled", cursor="hand2")
    ekle_btn.pack(pady=10)

    # Değişkenler
    secili_urun = {"urun": None, "fiyat": 0}

    def urun_sec(urun, fiyat):
        secili_urun["urun"] = urun
        secili_urun["fiyat"] = fiyat
        secili_urun_label.config(text=f"{urun} - {fiyat} TL")
        ekle_btn.config(state="normal")
        toplam_guncelle()
        
        # Tüm menü butonlarının rengini sıfırla
        for btn in menu_buttons:
            btn.config(relief="raised", bd=2)
        
        # Seçili butonun rengini değiştir
        for btn in menu_buttons:
            if btn["text"].split("\n")[0] == urun:
                btn.config(relief="sunken", bd=3)

    def toplam_guncelle():
        if secili_urun["urun"]:
            toplam = secili_urun["fiyat"] * adet_var.get()
            toplam_label.config(text=f"Toplam: {toplam} TL")

    def siparis_ekle_sepete():
        if not secili_urun["urun"]:
            return
        
        urun = secili_urun["urun"]
        adet = adet_var.get()
        tutar = secili_urun["fiyat"] * adet
        
        masa["siparisler"].append({"urun": urun, "adet": adet, "tutar": tutar})
        masa["toplam"] += tutar
        
        # Başarı mesajı (kısa süre göster)
        mesaj_label = tk.Label(kontrol_frame, text=f"✓ {adet} {urun} eklendi!", 
                              font=("Arial", 9), bg="#e8f4fd", fg="#27ae60")
        mesaj_label.pack(pady=5)
        kontrol_frame.after(2000, mesaj_label.destroy)  # 2 saniye sonra sil
        
        # Adet sıfırla
        adet_var.set(1)
        toplam_guncelle()
        guncelle_durum_bilgileri()
        guncelle_secili_masa_bilgisi()
        update_buttons()

    # Adet değiştiğinde toplam güncelle
    adet_var.trace("w", lambda *args: toplam_guncelle())
    ekle_btn.configure(command=siparis_ekle_sepete)

    # Menü butonları
    colors = [soft_blue, soft_green, soft_orange, soft_purple, "#ff9999", "#99ccff"]
    menu_buttons = []
    
    for i, (urun, fiyat) in enumerate(menu.items()):
        btn = tk.Button(menu_frame, text=f"{urun}\n{fiyat} TL", 
                       width=13, height=2, font=("Arial", 9, "bold"),
                       command=lambda u=urun, f=fiyat: urun_sec(u, f), 
                       bg=colors[i % len(colors)], fg="white",
                       relief="raised", bd=2, cursor="hand2")
        btn.grid(row=i//3, column=i%3, padx=8, pady=8)
        menu_buttons.append(btn)

# MENÜ - Güncellenmiş hali
menu = {
    # Dilim Tatlılar
    "Dilim Tatlı": 80,
    "Dark Velvet": 90,
    "Red Velvet": 90,
    "Frambuazlı Trileçe": 85,
    "Çikolatalı Trileçe": 85,
    "Karamelli Trileçe": 85,
    "Soğuk Kadayıf": 80,
    "Tiramisu": 95,
    
    # Kap Tatlılar
    "Kap Tatlı": 80,
    "Antep Fıstıklı M.": 130,
    "Lotuslu M.": 125,
    "Muzlu M.": 120,
    "Çilekli M.": 125,
    "İtalyan Karamelli M.": 130,
    "Profiterol": 110,
    "Supangle": 90,
    "Sütlaç": 75,
    
    # İçecekler
    "Soda": 25,
    "Meyveli Soda": 30,
    "Su": 10
}

def masa_degistir():
    """Masa değiştirme fonksiyonu - iyileştirilmiş"""
    temizle_orta_panel()
    eski_masa_no = secilen_masa.get()
    if eski_masa_no == 0:
        tk.Label(orta_panel, text="Önce masa seçiniz!", font=("Arial", 14), bg="#fafafa", fg="red").pack(pady=50)
        return
    
    eski_masa = tables[eski_masa_no]
    if not eski_masa["adisyon_acik"]:
        tk.Label(orta_panel, text="Seçili masada açık adisyon yok!", font=("Arial", 14), bg="#fafafa", fg="red").pack(pady=50)
        return
    
    if not eski_masa["siparisler"]:
        tk.Label(orta_panel, text="Seçili masada sipariş yok, masa değiştirilmez!", font=("Arial", 14), bg="#fafafa", fg="red").pack(pady=50)
        return

    # Başlık
    tk.Label(orta_panel, text=f"Masa {eski_masa_no} - Masa Değiştir", 
             font=("Arial", 14, "bold"), bg="#fafafa", fg="#2c3e50").pack(pady=10)

    # Ana container
    main_degistir_frame = tk.Frame(orta_panel, bg="#fafafa")
    main_degistir_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Sol taraf - mevcut masa bilgileri
    bilgi_frame = tk.Frame(main_degistir_frame, bg="#e8f4fd", bd=2, relief="ridge")
    bilgi_frame.pack(side="left", fill="both", expand=True, padx=(0,10))

    tk.Label(bilgi_frame, text=f"Masa {eski_masa_no} Bilgileri", 
             font=("Arial", 12, "bold"), bg="#e8f4fd", fg="#2c3e50").pack(pady=10)

    siparis_sayisi = len(eski_masa["siparisler"])
    toplam_adet = sum(s['adet'] for s in eski_masa["siparisler"])
    
    tk.Label(bilgi_frame, text=f"Sipariş Sayısı: {siparis_sayisi}", 
             font=("Arial", 10), bg="#e8f4fd", fg="#2c3e50").pack(pady=2)
    tk.Label(bilgi_frame, text=f"Toplam Adet: {toplam_adet}", 
             font=("Arial", 10), bg="#e8f4fd", fg="#2c3e50").pack(pady=2)
    tk.Label(bilgi_frame, text=f"Toplam Tutar: {eski_masa['toplam']} TL", 
             font=("Arial", 10, "bold"), bg="#e8f4fd", fg="#e74c3c").pack(pady=5)

    # Siparişler detayı
    tk.Label(bilgi_frame, text="Siparişler:", 
             font=("Arial", 10, "bold"), bg="#e8f4fd", fg="#2c3e50").pack(pady=(10,5))
    
    siparis_detay_frame = tk.Frame(bilgi_frame, bg="#e8f4fd")
    siparis_detay_frame.pack(fill="both", expand=True, padx=10, pady=5)
    
    for sip in eski_masa["siparisler"]:
        tk.Label(siparis_detay_frame, text=f"• {sip['adet']} x {sip['urun']} - {sip['tutar']} TL", 
                 font=("Arial", 9), bg="#e8f4fd", fg="#2c3e50", anchor="w").pack(fill="x")

    # Sağ taraf - masa seçimi
    secim_frame = tk.Frame(main_degistir_frame, bg="#fff0f0", bd=2, relief="ridge", width=300)
    secim_frame.pack(side="right", fill="y")
    secim_frame.pack_propagate(False)

    tk.Label(secim_frame, text="Yeni Masa Seç", 
             font=("Arial", 12, "bold"), bg="#fff0f0", fg="#2c3e50").pack(pady=10)

    # Seçili masa göstergesi
    secili_yeni_masa = tk.IntVar(value=0)
    secili_masa_label = tk.Label(secim_frame, text="Masa seçilmedi", 
                                font=("Arial", 10), bg="#fff0f0", fg="#7f8c8d")
    secili_masa_label.pack(pady=5)

    def yeni_masa_sec(masa_no):
        if tables[masa_no]["adisyon_acik"]:
            secili_masa_label.config(text=f"Masa {masa_no} - DOLU!", fg="red")
            degistir_btn.config(state="disabled")
            secili_yeni_masa.set(0)
        else:
            secili_masa_label.config(text=f"Masa {masa_no} - Uygun", fg="green")
            degistir_btn.config(state="normal")
            secili_yeni_masa.set(masa_no)
        
        # Tüm butonları sıfırla
        for btn in masa_btn_list:
            if btn.winfo_exists():
                btn.config(relief="raised", bd=2)
        
        # Seçili butonu vurgula
        for btn in masa_btn_list:
            if btn.winfo_exists() and btn["text"] == f"Masa {masa_no}":
                btn.config(relief="sunken", bd=3)

    # Masa butonları
    masa_btn_frame = tk.Frame(secim_frame, bg="#fff0f0")
    masa_btn_frame.pack(fill="both", expand=True, padx=10, pady=10)

    masa_btn_list = []
    for i in range(1, 21):
        if i == eski_masa_no:
            continue
        
        row = (i-1) // 4
        col = (i-1) % 4
        
        # Masa durumuna göre renk
        if tables[i]["adisyon_acik"]:
            btn_color = "#ffcccb"  # Açık kırmızı (dolu)
            btn_text_color = "#8b0000"
        else:
            btn_color = "#c8e6c9"  # Açık yeşil (boş)
            btn_text_color = "#2e7d32"
        
        btn = tk.Button(masa_btn_frame, text=f"Masa {i}", 
                       width=8, height=1, font=("Arial", 8),
                       bg=btn_color, fg=btn_text_color,
                       relief="raised", bd=2, cursor="hand2",
                       command=lambda m=i: yeni_masa_sec(m))
        btn.grid(row=row, column=col, padx=2, pady=2)
        masa_btn_list.append(btn)

    # Değiştir butonu
    degistir_btn = tk.Button(secim_frame, text="Masa Değiştir", width=20, height=2,
                            bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                            state="disabled", cursor="hand2")
    degistir_btn.pack(pady=15)

    def masa_degistir_onayli():
        yeni_masa_no = secili_yeni_masa.get()
        if yeni_masa_no == 0:
            return
        
        yeni_masa = tables[yeni_masa_no]
        
        # Masa değiştirme işlemi
        yeni_masa["adisyon_acik"] = True
        yeni_masa["siparisler"] = eski_masa["siparisler"].copy()
        yeni_masa["toplam"] = eski_masa["toplam"]
        
        # Eski masayı temizle
        eski_masa["adisyon_acik"] = False
        eski_masa["siparisler"] = []
        eski_masa["toplam"] = 0
        
        # Yeni masayı seç
        secilen_masa.set(yeni_masa_no)
        
        update_buttons()
        guncelle_secili_masa_bilgisi()
        guncelle_durum_bilgileri()
        siparisleri_goster()
        
        # Başarı mesajı göster
        temizle_orta_panel()
        tk.Label(orta_panel, text="✓ Masa Değiştirme Başarılı!", 
                 font=("Arial", 16, "bold"), bg="#fafafa", fg="green").pack(pady=30)
        tk.Label(orta_panel, text=f"Masa {eski_masa_no} → Masa {yeni_masa_no}", 
                 font=("Arial", 14), bg="#fafafa", fg="#2c3e50").pack(pady=10)
        tk.Label(orta_panel, text=f"Toplam: {yeni_masa['toplam']} TL", 
                 font=("Arial", 12), bg="#fafafa", fg="#e74c3c").pack(pady=5)

    degistir_btn.configure(command=masa_degistir_onayli)

def adisyon_ac():
    masa_no = secilen_masa.get()
    if masa_no == 0:
        messagebox.showwarning("Uyarı", "Önce masa seçiniz!")
        return
    masa = tables[masa_no]
    if masa["adisyon_acik"]:
        messagebox.showinfo("Bilgi", "Bu masada zaten açık bir adisyon var.")
        return
    masa["adisyon_acik"] = True
    masa["siparisler"] = []
    masa["toplam"] = 0
    update_buttons()
    guncelle_secili_masa_bilgisi()
    guncelle_durum_bilgileri()
    siparisleri_goster()
    messagebox.showinfo("Başarılı", f"Masa {masa_no} için yeni adisyon açıldı.")

def siparis_ekle():
    """Sipariş ekleme ekranı - geliştirilmiş versiyon"""
    temizle_orta_panel()
    masa_no = secilen_masa.get()
    if masa_no == 0:
        tk.Label(orta_panel, text="Lütfen bir masa seçin", font=("Arial", 14), bg="#fafafa", fg="gray").pack(pady=50)
        return

    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        masa["adisyon_acik"] = True
        masa["siparisler"] = []
        masa["toplam"] = 0
        update_buttons()
        guncelle_secili_masa_bilgisi()
        guncelle_durum_bilgileri()

    # Başlık
    tk.Label(orta_panel, text=f"Masa {masa_no} - Sipariş Ekle", 
             font=("Arial", 14, "bold"), bg="#fafafa", fg="#2c3e50").pack(pady=10)

    # Ana container
    main_siparis_frame = tk.Frame(orta_panel, bg="#fafafa")
    main_siparis_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Sol taraf - menü butonları
    menu_frame = tk.Frame(main_siparis_frame, bg="#fafafa")
    menu_frame.pack(side="left", fill="both", expand=True)

    # Sağ taraf - adet kontrolü ve ekleme
    kontrol_frame = tk.Frame(main_siparis_frame, bg="#e8f4fd", bd=2, relief="ridge", width=200)
    kontrol_frame.pack(side="right", fill="y", padx=(20,0))
    kontrol_frame.pack_propagate(False)

    # Seçili ürün ve adet kontrolü
    tk.Label(kontrol_frame, text="Seçili Ürün:", font=("Arial", 11, "bold"), 
             bg="#e8f4fd", fg="#2c3e50").pack(pady=(10,5))
    
    secili_urun_label = tk.Label(kontrol_frame, text="Ürün seçiniz", 
                                font=("Arial", 10), bg="#e8f4fd", fg="#7f8c8d")
    secili_urun_label.pack(pady=5)

    # Adet kontrolü
    tk.Label(kontrol_frame, text="Adet:", font=("Arial", 11, "bold"), 
             bg="#e8f4fd", fg="#2c3e50").pack(pady=(15,5))

    adet_frame = tk.Frame(kontrol_frame, bg="#e8f4fd")
    adet_frame.pack(pady=5)

    adet_var = tk.IntVar(value=1)
    
    def adet_azalt():
        if adet_var.get() > 1:
            adet_var.set(adet_var.get() - 1)
    
    def adet_arttir():
        if adet_var.get() < 50:
            adet_var.set(adet_var.get() + 1)

    btn_azalt = tk.Button(adet_frame, text="-", width=3, height=1,
                         bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                         command=adet_azalt)
    btn_azalt.pack(side="left", padx=2)

    adet_entry = tk.Entry(adet_frame, textvariable=adet_var, width=5, justify="center",
                         font=("Arial", 12))
    adet_entry.pack(side="left", padx=2)

    btn_arttir = tk.Button(adet_frame, text="+", width=3, height=1,
                          bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                          command=adet_arttir)
    btn_arttir.pack(side="left", padx=2)

    # Toplam tutar
    toplam_label = tk.Label(kontrol_frame, text="Toplam: 0 TL", 
                           font=("Arial", 11, "bold"), bg="#e8f4fd", fg="#e74c3c")
    toplam_label.pack(pady=(15,10))

    # Ekle butonu
    ekle_btn = tk.Button(kontrol_frame, text="Sepete Ekle", width=15, height=2,
                        bg="#3498db", fg="white", font=("Arial", 10, "bold"),
                        state="disabled", cursor="hand2")
    ekle_btn.pack(pady=10)

    # Değişkenler
    secili_urun = {"urun": None, "fiyat": 0}

    def urun_sec(urun, fiyat):
        secili_urun["urun"] = urun
        secili_urun["fiyat"] = fiyat
        secili_urun_label.config(text=f"{urun} - {fiyat} TL")
        ekle_btn.config(state="normal")
        toplam_guncelle()
        
        # Tüm menü butonlarının rengini sıfırla
        for btn in menu_buttons:
            btn.config(relief="raised", bd=2)
        
        # Seçili butonun rengini değiştir
        for btn in menu_buttons:
            if btn["text"].split("\n")[0] == urun:
                btn.config(relief="sunken", bd=3)

    def toplam_guncelle():
        if secili_urun["urun"]:
            toplam = secili_urun["fiyat"] * adet_var.get()
            toplam_label.config(text=f"Toplam: {toplam} TL")

    def siparis_ekle_sepete():
        if not secili_urun["urun"]:
            return
        
        urun = secili_urun["urun"]
        adet = adet_var.get()
        tutar = secili_urun["fiyat"] * adet
        
        masa["siparisler"].append({"urun": urun, "adet": adet, "tutar": tutar})
        masa["toplam"] += tutar
        
        # Başarı mesajı (kısa süre göster)
        mesaj_label = tk.Label(kontrol_frame, text=f"✓ {adet} {urun} eklendi!", 
                              font=("Arial", 9), bg="#e8f4fd", fg="#27ae60")
        mesaj_label.pack(pady=5)
        kontrol_frame.after(2000, mesaj_label.destroy)  # 2 saniye sonra sil
        
        # Adet sıfırla
        adet_var.set(1)
        toplam_guncelle()
        guncelle_durum_bilgileri()
        guncelle_secili_masa_bilgisi()
        update_buttons()

    # Adet değiştiğinde toplam güncelle
    adet_var.trace("w", lambda *args: toplam_guncelle())
    ekle_btn.configure(command=siparis_ekle_sepete)

    # Menü butonları
    colors = [soft_blue, soft_green, soft_orange, soft_purple, "#ff9999", "#99ccff"]
    menu_buttons = []
    
    for i, (urun, fiyat) in enumerate(menu.items()):
        btn = tk.Button(menu_frame, text=f"{urun}\n{fiyat} TL", 
                       width=13, height=2, font=("Arial", 9, "bold"),
                       command=lambda u=urun, f=fiyat: urun_sec(u, f), 
                       bg=colors[i % len(colors)], fg="white",
                       relief="raised", bd=2, cursor="hand2")
        btn.grid(row=i//3, column=i%3, padx=8, pady=8)
        menu_buttons.append(btn)
        
def siparis_sil():
    """Sipariş silme - geliştirilmiş versiyon"""
    temizle_orta_panel()
    masa_no = secilen_masa.get()
    if masa_no == 0:
        tk.Label(orta_panel, text="Lütfen bir masa seçin", font=("Arial", 12), bg="#fafafa", fg="gray").pack(pady=40)
        return
    
    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        tk.Label(orta_panel, text="Bu masada açık adisyon yok", font=("Arial", 12), bg="#fafafa", fg="gray").pack(pady=40)
        return

    # Başlık
    tk.Label(orta_panel, text=f"Masa {masa_no} - Sipariş Sil", 
             font=("Arial", 14, "bold"), bg="#fafafa", fg="#e74c3c").pack(pady=10)

    if not masa["siparisler"]:
        tk.Label(orta_panel, text="Bu masada silinecek sipariş bulunmuyor.", 
                 bg="#fafafa", font=("Arial", 11), fg="gray").pack(pady=25)
        return

    # Ana container
    main_sil_frame = tk.Frame(orta_panel, bg="#fafafa")
    main_sil_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Sol taraf - siparişler listesi
    siparis_frame = tk.Frame(main_sil_frame, bg="#fafafa")
    siparis_frame.pack(side="left", fill="both", expand=True)

    # Sağ taraf - silme kontrolü
    kontrol_frame = tk.Frame(main_sil_frame, bg="#ffe6e6", bd=2, relief="ridge", width=200)
    kontrol_frame.pack(side="right", fill="y", padx=(20,0))
    kontrol_frame.pack_propagate(False)

    tk.Label(kontrol_frame, text="Seçili Sipariş:", font=("Arial", 11, "bold"), 
             bg="#ffe6e6", fg="#2c3e50").pack(pady=(10,5))
    
    secili_siparis_label = tk.Label(kontrol_frame, text="Sipariş seçiniz", 
                                   font=("Arial", 9), bg="#ffe6e6", fg="#7f8c8d")
    secili_siparis_label.pack(pady=5)

    # Adet kontrolü
    tk.Label(kontrol_frame, text="Silinecek Adet:", font=("Arial", 11, "bold"), 
             bg="#ffe6e6", fg="#2c3e50").pack(pady=(15,5))

    adet_frame = tk.Frame(kontrol_frame, bg="#ffe6e6")
    adet_frame.pack(pady=5)

    silinecek_adet_var = tk.IntVar(value=1)
    
    def adet_azalt():
        if silinecek_adet_var.get() > 1:
            silinecek_adet_var.set(silinecek_adet_var.get() - 1)
    
    def adet_arttir():
        max_adet = secili_siparis.get("max_adet", 1)
        if silinecek_adet_var.get() < max_adet:
            silinecek_adet_var.set(silinecek_adet_var.get() + 1)

    btn_azalt = tk.Button(adet_frame, text="-", width=3, height=1,
                         bg="#e74c3c", fg="white", font=("Arial", 12, "bold"),
                         command=adet_azalt)
    btn_azalt.pack(side="left", padx=2)

    adet_entry = tk.Entry(adet_frame, textvariable=silinecek_adet_var, width=5, justify="center",
                         font=("Arial", 12))
    adet_entry.pack(side="left", padx=2)

    btn_arttir = tk.Button(adet_frame, text="+", width=3, height=1,
                          bg="#27ae60", fg="white", font=("Arial", 12, "bold"),
                          command=adet_arttir)
    btn_arttir.pack(side="left", padx=2)

    # Silinecek tutar
    silinecek_tutar_label = tk.Label(kontrol_frame, text="Silinecek: 0 TL", 
                                    font=("Arial", 11, "bold"), bg="#ffe6e6", fg="#e74c3c")
    silinecek_tutar_label.pack(pady=(15,10))

    # Sil butonu
    sil_btn = tk.Button(kontrol_frame, text="Seçili Adeti Sil", width=15, height=2,
                       bg="#e74c3c", fg="white", font=("Arial", 10, "bold"),
                       state="disabled", cursor="hand2")
    sil_btn.pack(pady=10)

    # Değişkenler
    secili_siparis = {"idx": -1, "max_adet": 1, "birim_fiyat": 0}

    def siparis_sec(idx):
        if idx >= len(masa["siparisler"]):
            return
            
        siparis = masa["siparisler"][idx]
        secili_siparis["idx"] = idx
        secili_siparis["max_adet"] = siparis["adet"]
        secili_siparis["birim_fiyat"] = siparis["tutar"] // siparis["adet"]
        
        secili_siparis_label.config(text=f"{siparis['urun']}\n{siparis['adet']} adet mevcut")
        silinecek_adet_var.set(1)
        sil_btn.config(state="normal")
        silinecek_tutar_guncelle()
        
        # Tüm sipariş butonlarının rengini sıfırla
        for btn in siparis_buttons:
            btn.config(relief="raised", bd=2)
        
        # Seçili butonun rengini değiştir
        siparis_buttons[idx].config(relief="sunken", bd=3)

    def silinecek_tutar_guncelle():
        if secili_siparis["idx"] >= 0:
            tutar = secili_siparis["birim_fiyat"] * silinecek_adet_var.get()
            silinecek_tutar_label.config(text=f"Silinecek: {tutar} TL")

    def siparis_sil_onayli():
        idx = secili_siparis["idx"]
        if idx < 0 or idx >= len(masa["siparisler"]):
            return
        
        siparis = masa["siparisler"][idx]
        silinecek_adet = silinecek_adet_var.get()
        birim_fiyat = siparis["tutar"] // siparis["adet"]
        silinen_tutar = birim_fiyat * silinecek_adet
        
        if silinecek_adet == siparis["adet"]:
            # Tüm ürün siliniyor
            masa["siparisler"].pop(idx)
            mesaj = f"'{siparis['urun']}' tamamen silindi."
        else:
            # Kısmi silme
            masa["siparisler"][idx]["adet"] -= silinecek_adet
            masa["siparisler"][idx]["tutar"] -= silinen_tutar
            mesaj = f"'{siparis['urun']}' ürününden {silinecek_adet} adet silindi."
        
        masa["toplam"] -= silinen_tutar
        
        # Başarı mesajı (kısa süre göster)
        mesaj_label = tk.Label(kontrol_frame, text=f"✓ {mesaj}", 
                              font=("Arial", 8), bg="#ffe6e6", fg="#27ae60", wraplength=180)
        mesaj_label.pack(pady=5)
        kontrol_frame.after(3000, mesaj_label.destroy)  # 3 saniye sonra sil
        
        guncelle_secili_masa_bilgisi()
        guncelle_durum_bilgileri()
        update_buttons()
        siparis_sil()  # Sayfayı yenile

    # Adet değiştiğinde silinecek tutar güncelle
    silinecek_adet_var.trace("w", lambda *args: silinecek_tutar_guncelle())
    sil_btn.configure(command=siparis_sil_onayli)

    # Siparişler listesi
    tk.Label(siparis_frame, text="Silmek istediğiniz siparişe tıklayın:", 
             font=("Arial", 11), bg="#fafafa", fg="#2c3e50").pack(pady=5)

    siparis_buttons = []
    for idx, sip in enumerate(masa["siparisler"]):
        kutu = tk.Frame(siparis_frame, bg=soft_white, bd=1, relief="ridge", height=35)
        kutu.pack(fill="x", pady=2)
        kutu.pack_propagate(False)
        
        # Sipariş bilgisi
        bilgi = f"{sip['adet']} x {sip['urun']} - {sip['tutar']} TL"
        
        # Tıklanabilir buton olarak sipariş
        btn = tk.Button(kutu, text=bilgi, font=("Arial", 10), 
                       bg=soft_white, fg="#2c3e50", anchor="w",
                       relief="raised", bd=2, cursor="hand2",
                       command=lambda i=idx: siparis_sec(i))
        btn.pack(fill="both", expand=True, padx=5, pady=2)
        siparis_buttons.append(btn)

def hesap_kapat():
    global gunluk_ciro
    masa_no = secilen_masa.get()
    if masa_no == 0:
        messagebox.showwarning("Uyarı", "Önce masa seçiniz!")
        return
    
    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        messagebox.showinfo("Bilgi", "Bu masada açık adisyon yok.")
        return
    
    toplam = masa["toplam"]
    if toplam == 0:
        result = messagebox.askyesno("Onay", "Bu masada sipariş yok. Yine de hesabı kapatmak istiyor musunuz?")
        if not result:
            return
    
    result = messagebox.askyesno("Hesap Kapat", f"Masa {masa_no} hesabını kapatmak istediğinizden emin misiniz?\nToplam Tutar: {toplam} TL")
    if result:
        # Ciroya ekle
        gunluk_ciro += toplam
        
        masa["adisyon_acik"] = False
        masa["siparisler"] = []
        masa["toplam"] = 0
        update_buttons()
        guncelle_secili_masa_bilgisi()
        guncelle_durum_bilgileri()
        temizle_orta_panel()
        tk.Label(orta_panel, text="Masa seçiniz veya işlem yapınız", 
                 font=("Arial", 12), bg="#fafafa", fg="gray").pack(pady=40)
        messagebox.showinfo("Hesap Kapatıldı", f"Masa {masa_no} hesabı kapatıldı.\nToplam: {toplam} TL\nGünlük Ciro: {gunluk_ciro} TL")

# MASA GRUPLARI
masa_groups = {
    "Ön Bahçe": [1,2,3,4],
    "Ön": [5,6,7],
    "Arka": [8,9,10,11,12,13,14],
    "Arka Bahçe": [15,16,17,18,19,20]
}

masa_buttons = {}
for group_name, masalar in masa_groups.items():
    frame = tk.LabelFrame(sol_panel, text=group_name, bg="#ecf0f1", fg="#2c3e50", 
                         font=("Arial", 10, "bold"), padx=4, pady=4)
    frame.pack(pady=6, fill="x")
    
    # Masa butonlarını grid ile düzenle
    for i, m in enumerate(masalar):
        btn = tk.Button(frame, text=f"Masa {m}", width=9, height=2,  # Boyut küçültüldü
                        bg=soft_green, fg="white", font=("Arial", 8, "bold"),
                        relief="raised", bd=2, cursor="hand2",
                        command=lambda m=m: [secilen_masa.set(m), update_buttons(), 
                                           guncelle_secili_masa_bilgisi(), siparisleri_goster()])
        
        # Grup başına düzenleme
        if group_name == "Ön Bahçe":
            btn.grid(row=0, column=i, padx=2, pady=2)
        elif group_name == "Ön":
            btn.grid(row=0, column=i, padx=2, pady=2)
        elif group_name == "Arka":
            btn.grid(row=i//4, column=i%4, padx=2, pady=2)
        else:  # Arka Bahçe
            btn.grid(row=i//3, column=i%3, padx=2, pady=2)
        
        masa_buttons[m] = btn

# ALT PANEL - İŞLEM BUTONLARI
alt_panel = tk.Frame(sag_panel, bg="#ecf0f1", relief="ridge", bd=1, height=80)  # Yükseklik küçültüldü
alt_panel.pack(fill="x")
alt_panel.pack_propagate(False)

alt_colors = {
    "Adisyon Aç": soft_blue,
    "Sipariş Ekle": soft_green,
    "Sipariş Sil": soft_red,
    "Siparişleri Göster": soft_orange,
    "Hesabı Kapat": soft_purple,
    "Masa Değiştir": "#ff6b9d"
}

alt_buttons = []
button_specs = [
    ("Adisyon Aç", adisyon_ac),
    ("Sipariş Ekle", siparis_ekle),
    ("Sipariş Sil", siparis_sil),
    ("Siparişleri Göster", siparisleri_goster),
    ("Hesabı Kapat", hesap_kapat),
    ("Masa Değiştir", masa_degistir)
]

for i, (text, func) in enumerate(button_specs):
    btn = tk.Button(alt_panel, text=text, width=15, height=2,  # Boyut küçültüldü
                    bg=soft_gray, fg="white", font=("Arial", 9, "bold"),  # Font küçültüldü
                    relief="raised", bd=2, state="disabled", cursor="hand2")
    btn.grid(row=0, column=i, padx=6, pady=15)  # Padding küçültüldü
    btn.configure(command=func)
    alt_buttons.append(btn)

def update_buttons():
    masa_no = secilen_masa.get()
    
    # Alt panel butonları
    for btn in alt_buttons:
        btn_text = btn["text"]
        if btn_text == "Adisyon Aç":
            if masa_no != 0:
                btn.configure(state="normal", bg=alt_colors[btn_text])
            else:
                btn.configure(state="disabled", bg=soft_gray)
        elif btn_text == "Siparişleri Göster":
            # Siparişleri göster butonu masa seçildiğinde aktif olsun
            if masa_no != 0:
                btn.configure(state="normal", bg=alt_colors[btn_text])
            else:
                btn.configure(state="disabled", bg=soft_gray)
        else:
            # Diğer butonlar için adisyon açık olması gerekli
            if masa_no != 0 and tables[masa_no]["adisyon_acik"]:
                btn.configure(state="normal", bg=alt_colors[btn_text])
            else:
                btn.configure(state="disabled", bg=soft_gray)
    
    # Masa butonları
    for m_no, btn in masa_buttons.items():
        if masa_no == m_no:
            btn.configure(bg=highlight_color, fg="black")
        else:
            if tables[m_no]["adisyon_acik"]:
                btn.configure(bg=soft_red, fg="white")
            else:
                btn.configure(bg=soft_green, fg="white")
                

update_buttons()

if __name__ == "__main__":
    root.mainloop()