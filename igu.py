import tkinter as tk
from tkinter import messagebox

# Kullanıcı bilgileri
users = {
    "admin": {"password": "1234", "role": "admin"},
    "calisan": {"password": "4321", "role": "calisan"}
}

def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in users and users[username]["password"] == password:
        role = users[username]["role"]
        messagebox.showinfo("Giriş Başarılı", f"{role.capitalize()} paneline yönlendiriliyorsunuz.")
        root.destroy()
        if role == "admin":
            admin_panel()
        else:
            calisan_panel()
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

# Giriş ekranı
root = tk.Tk()
root.title("Tatlıcı Uygulaması - Giriş")
root.geometry("300x200")

tk.Label(root, text="Kullanıcı Adı:").pack(pady=5)
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Şifre:").pack(pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Giriş", command=login).pack(pady=10)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox





import tkinter as tk
from tkinter import messagebox

# Masalar
tables = {i: {"adisyon_acik": False, "siparisler": [], "toplam": 0} for i in range(1, 21)}

# Menü
menu = {
    "Dilim Tatlı": 80,
    "Kap Tatlı": 80,
    "Makaron": 120,
    "Soda": 25,
    "Meyveli Soda": 30,
    "Su": 10
}

root = tk.Tk()
root.title("Çalışan Paneli - TRITAT")
root.geometry("1000x800")
root.configure(bg="#f5f5f5")

secilen_masa = tk.IntVar()
secilen_masa.set(0)

# --- RENKLER ---
soft_red = "#f28b82"
soft_green = "#81c995"
soft_blue = "#a0c4ff"
soft_orange = "#ffb77d"
soft_purple = "#c59aff"
soft_gray = "#d3d3d3"
highlight_color = "#ffd966"

# --- ALT PANEL BUTON GÜNCELLEME ---
def update_buttons():
    masa_no = secilen_masa.get()
    for btn in alt_buttons:
        if btn["text"] == "Adisyon Aç":
            btn.configure(state="normal", bg=soft_blue)
        else:
            if masa_no != 0 and tables[masa_no]["adisyon_acik"]:
                btn.configure(state="normal", bg=alt_colors[btn["text"]], fg="white")
            else:
                btn.configure(state="disabled", bg=soft_gray, fg="white")
    update_masa_buttons_color()

# --- MASA RENKLERİ VE SEÇİLİ MASA ---
def update_masa_buttons_color():
    for m_no, btn in masa_buttons.items():
        if secilen_masa.get() == m_no:
            btn.configure(bg=highlight_color)  # Seçili masa vurgusu
        else:
            if tables[m_no]["adisyon_acik"]:
                btn.configure(bg=soft_red, fg="white")
            else:
                btn.configure(bg=soft_green, fg="white")

# --- MASA BİLGİSİ ---
def masa_bilgisi():
    masa_no = secilen_masa.get()
    if masa_no == 0:
        return
    masa = tables[masa_no]
    info = f"Masa {masa_no}:\nAdisyon Açık: {masa['adisyon_acik']}\nToplam: {masa['toplam']} TL\nSiparişler:\n"
    for sip in masa["siparisler"]:
        info += f"{sip['adet']} x {sip['urun']} = {sip['tutar']} TL\n"
    messagebox.showinfo(f"Masa {masa_no} Bilgi", info)

# --- ADİSYON AÇ ---
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
    messagebox.showinfo("Başarılı", f"Masa {masa_no} için yeni adisyon açıldı.")

# --- SİPARİŞ EKLE ---
def siparis_ekle():
    masa_no = secilen_masa.get()
    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        messagebox.showwarning("Uyarı", "Önce adisyon açmalısınız!")
        return

    ekle_window = tk.Toplevel(root)
    ekle_window.title(f"Masa {masa_no} Sipariş Ekle")
    ekle_window.geometry("300x200")
    ekle_window.configure(bg="#f0f0f0")
    
    tk.Label(ekle_window, text="Ürün:", bg="#f0f0f0").pack(pady=5)
    urun_var = tk.StringVar()
    urun_var.set(list(menu.keys())[0])
    tk.OptionMenu(ekle_window, urun_var, *menu.keys()).pack(pady=5)
    
    tk.Label(ekle_window, text="Adet:", bg="#f0f0f0").pack(pady=5)
    adet_var = tk.IntVar()
    adet_var.set(1)
    tk.Entry(ekle_window, textvariable=adet_var, width=5).pack(pady=5)

    def ekle():
        urun = urun_var.get()
        adet = adet_var.get()
        tutar = menu[urun] * adet
        masa["siparisler"].append({"urun": urun, "adet": adet, "tutar": tutar})
        masa["toplam"] += tutar
        messagebox.showinfo("Başarılı", f"{adet} adet {urun} eklendi. Toplam: {masa['toplam']} TL")
        ekle_window.destroy()

    tk.Button(ekle_window, text="Ekle", command=ekle, bg=soft_green, fg="white", width=15, height=2).pack(pady=10)

# --- SİPARİŞ SİL ---
def siparis_sil():
    masa_no = secilen_masa.get()
    masa = tables[masa_no]
    if not masa["siparisler"]:
        messagebox.showinfo("Bilgi", "Bu masada sipariş yok.")
        return

    sil_window = tk.Toplevel(root)
    sil_window.title(f"Masa {masa_no} Sipariş Sil")
    sil_window.geometry("300x150")
    sil_window.configure(bg="#f0f0f0")
    
    tk.Label(sil_window, text="Silinecek sipariş numarası:", bg="#f0f0f0").pack(pady=5)
    sip_var = tk.IntVar()
    sip_var.set(1)
    tk.Spinbox(sil_window, from_=1, to=len(masa["siparisler"]), textvariable=sip_var, width=5).pack(pady=5)

    def sil():
        idx = sip_var.get() - 1
        silinen = masa["siparisler"].pop(idx)
        masa["toplam"] -= silinen["tutar"]
        messagebox.showinfo("Başarılı", f"{silinen['urun']} silindi. Yeni toplam: {masa['toplam']} TL")
        sil_window.destroy()

    tk.Button(sil_window, text="Sil", command=sil, bg=soft_red, fg="white", width=15, height=2).pack(pady=10)

# --- HESABI KAPAT ---
def hesap_kapat():
    masa_no = secilen_masa.get()
    masa = tables[masa_no]
    if not masa["adisyon_acik"]:
        messagebox.showinfo("Bilgi", "Bu masada açık adisyon yok.")
        return
    toplam = masa["toplam"]
    masa["adisyon_acik"] = False
    masa["siparisler"] = []
    masa["toplam"] = 0
    update_buttons()
    messagebox.showinfo("Hesap Kapatıldı", f"Masa {masa_no} hesabı kapatıldı. Toplam: {toplam} TL")

# --- MASA GRUPLARI ---
masa_groups = {
    "Ön Bahçe": [1,2,3,4],
    "Ön": [5,6,7],
    "Arka": [8,9,10,11,12,13,14],
    "Arka Bahçe": [15,16,17,18,19,20]
}

masa_buttons = {}

for group_name, masalar in masa_groups.items():
    frame = tk.LabelFrame(root, text=group_name, bg="#e0f7fa", fg="#006064", font=("Arial", 12, "bold"), padx=10, pady=10)
    frame.pack(pady=5, fill="x", padx=10)
    for i, m in enumerate(masalar):
        btn = tk.Button(frame, text=f"Masa {m}", width=10, height=3,
                  bg=soft_green, fg="white",
                  command=lambda m=m: [secilen_masa.set(m), update_buttons()])
        btn.grid(row=0, column=i, padx=5, pady=5)
        masa_buttons[m] = btn

# --- ALT PANEL BUTONLARI ---
alt_panel = tk.Frame(root, bg="#fafafa", pady=20)
alt_panel.pack(pady=15)

alt_colors = {
    "Sipariş Ekle": soft_green,
    "Sipariş Sil": soft_red,
    "Siparişleri Göster": soft_orange,
    "Hesabı Kapat": soft_purple
}

alt_buttons = []

button_specs = [
    ("Adisyon Aç", adisyon_ac),
    ("Sipariş Ekle", siparis_ekle),
    ("Sipariş Sil", siparis_sil),
    ("Siparişleri Göster", masa_bilgisi),
    ("Hesabı Kapat", hesap_kapat)
]

for i, (text, func) in enumerate(button_specs):
    btn = tk.Button(alt_panel, text=text, width=18, height=3, bg=soft_gray, fg="white", state="disabled")
    btn.grid(row=i//3, column=i%3, padx=15, pady=15)
    btn.configure(command=func)
    alt_buttons.append(btn)

root.mainloop()



