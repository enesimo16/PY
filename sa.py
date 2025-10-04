
import json
import locale
import sys
from datetime import datetime
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

# --- Bölge ve para biçimi (TR) ---
try:
    locale.setlocale(locale.LC_ALL, '')
except locale.Error:
    # Windows'ta TR kurulumu yoksa yine de çalışsın
    pass

APP_TITLE = "Harcama Takip"
DATA_FILE = Path(__file__).with_name("expenses.json")


# ------------------ Veri Katmanı ------------------ #
class ExpenseStore:
    """JSON dosyasında şu yapıyla saklar:
    {
        "YYYY-MM-DD": [
            {"amount": 50.0, "desc": "Market"},
            {"amount": 30.0, "desc": "Çay"}
        ],
        ...
    }
    """
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.data = {}  # dict[str, list[dict]]
        self.load()

    def load(self):
        if self.file_path.exists():
            try:
                self.data = json.loads(self.file_path.read_text(encoding="utf-8"))
            except Exception:
                # Dosya bozuksa yedekle ve sıfırla
                backup = self.file_path.with_suffix(".corrupt.json")
                try:
                    self.file_path.replace(backup)
                except Exception:
                    pass
                self.data = {}
        else:
            self.data = {}

    def save(self):
        try:
            self.file_path.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")
        except Exception as e:
            messagebox.showerror("Kayıt Hatası", f"Veri kaydedilemedi:\n{e}")

    def add_expense(self, date_str: str, amount: float, desc: str):
        if not date_str:
            date_str = today_str()
        self.data.setdefault(date_str, [])
        self.data[date_str].append({"amount": float(amount), "desc": desc.strip()})
        self.save()

    def iter_expenses(self):
        """Tüm kayıtları (date, amount, desc) olarak tarih sırasıyla döndürür."""
        for date_str, items in sorted(self.data.items()):
            for item in items:
                yield date_str, float(item.get("amount", 0.0)), item.get("desc", "")

    def get_daily_total(self, date_str: str) -> float:
        total = 0.0
        for d, amt, _ in self.iter_expenses():
            if d == date_str:
                total += amt
        return total

    def get_monthly_total(self, year_month: str) -> float:
        # year_month: "YYYY-MM"
        total = 0.0
        for d, amt, _ in self.iter_expenses():
            if d.startswith(year_month):
                total += amt
        return total


# ------------------ Yardımcılar ------------------ #
def today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def current_year_month() -> str:
    return datetime.now().strftime("%Y-%m")


def money_fmt(value: float) -> str:
    # Basit TL formatı; locale yoksa fallback
    try:
        # locale.currency bazen para işaretini ekler; biz "TL" istiyoruz
        return f"{locale.format_string('%.2f', value, grouping=True)} TL"
    except Exception:
        return f"{value:,.2f} TL".replace(",", ".")


# ------------------ UI: Ana Uygulama ------------------ #
class ExpenseApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry("540x640")
        self.minsize(420, 560)

        # ttk tema
        self.style = ttk.Style()
        if "clam" in self.style.theme_names():
            self.style.theme_use("clam")

        # Global font boyutları
        default_font = ("Segoe UI", 11)
        self.option_add("*Font", default_font)

        # Renk ve padding
        self.pad = 12

        # Veri deposu
        self.store = ExpenseStore(DATA_FILE)

        # Üst çerçeve - içerik alanı
        container = ttk.Frame(self, padding=self.pad)
        container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        for i in range(1):
            container.grid_rowconfigure(i, weight=1)
            container.grid_columnconfigure(i, weight=1)

        # Ekranların tutulduğu dict
        self.frames = {}

        # Ekranları oluştur
        for F in (MainScreen, AddExpenseScreen, StatsScreen):
            frame = F(parent=container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainScreen")

        # Üst menü (isteğe bağlı)
        self._build_menu()

        # Pencere kapatılırken kaydet
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _build_menu(self):
        menubar = tk.Menu(self)
        app_menu = tk.Menu(menubar, tearoff=0)
        app_menu.add_command(label="Ana Ekran", command=lambda: self.show_frame("MainScreen"))
        app_menu.add_separator()
        app_menu.add_command(label="Çıkış", command=self.on_close)
        menubar.add_cascade(label="Uygulama", menu=app_menu)
        self.config(menu=menubar)

    def show_frame(self, name: str):
        frame = self.frames[name]
        # Ekrana gelmeden önce güncellemek isteyenler için hook
        if hasattr(frame, "on_before_show"):
            try:
                frame.on_before_show()
            except Exception:
                pass
        frame.tkraise()

    def refresh_totals_everywhere(self):
        # Ana ekrandaki toplamları güncelle
        main = self.frames.get("MainScreen")
        if main:
            main.update_totals_labels()

    def on_close(self):
        try:
            self.store.save()
        finally:
            self.destroy()


# ------------------ UI: Ana Ekran ------------------ #
class MainScreen(ttk.Frame):
    def __init__(self, parent, controller: ExpenseApp):
        super().__init__(parent, padding=controller.pad)
        self.controller = controller

        # Üst kısım: Aylık ve Günlük toplam
        totals_box = ttk.Frame(self)
        totals_box.grid(row=0, column=0, sticky="ew", pady=(0, controller.pad))
        totals_box.grid_columnconfigure(0, weight=1)
        totals_box.grid_columnconfigure(1, weight=1)

        self.month_total_var = tk.StringVar(value="Aylık Toplam: 0 TL")
        self.day_total_var = tk.StringVar(value="Günlük Toplam: 0 TL")

        month_lbl = ttk.Label(totals_box, textvariable=self.month_total_var, font=("Segoe UI", 16, "bold"))
        day_lbl = ttk.Label(totals_box, textvariable=self.day_total_var, font=("Segoe UI", 16, "bold"))

        month_lbl.grid(row=0, column=0, sticky="w", padx=(0, 8))
        day_lbl.grid(row=0, column=1, sticky="e", padx=(8, 0))

        # Orta alan: Büyük butonlar
        buttons_box = ttk.Frame(self)
        buttons_box.grid(row=1, column=0, sticky="nsew", pady=(controller.pad, controller.pad))
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Boşluk için bir esnek frame
        spacer_top = ttk.Frame(buttons_box)
        spacer_top.grid(row=0, column=0, sticky="nsew")
        buttons_box.grid_rowconfigure(0, weight=1)

        btn_expense = ttk.Button(buttons_box, text="Harcama", command=lambda: controller.show_frame("AddExpenseScreen"))
        btn_stats = ttk.Button(buttons_box, text="İstatistik", command=lambda: controller.show_frame("StatsScreen"))

        btn_expense.grid(row=1, column=0, pady=(0, 10), ipadx=20, ipady=16, sticky="n")
        btn_stats.grid(row=2, column=0, ipadx=20, ipady=16, sticky="n")

        spacer_bottom = ttk.Frame(buttons_box)
        spacer_bottom.grid(row=3, column=0, sticky="nsew")
        buttons_box.grid_rowconfigure(3, weight=1)

        # Alt bilgi
        footer = ttk.Label(self, text="Veriler otomatik kaydedilir • " + str(DATA_FILE.name))
        footer.grid(row=2, column=0, sticky="ew")

        self.update_totals_labels()

    def on_before_show(self):
        # Ana ekrana her dönüşte toplamları tazele
        self.update_totals_labels()

    def update_totals_labels(self):
        store = self.controller.store
        m_total = store.get_monthly_total(current_year_month())
        d_total = store.get_daily_total(today_str())
        self.month_total_var.set(f"Aylık Toplam: {money_fmt(m_total)}")
        self.day_total_var.set(f"Günlük Toplam: {money_fmt(d_total)}")


# ------------------ UI: Harcama Ekle ------------------ #
class AddExpenseScreen(ttk.Frame):
    def __init__(self, parent, controller: ExpenseApp):
        super().__init__(parent, padding=controller.pad)
        self.controller = controller

        title = ttk.Label(self, text="Harcama Ekle", font=("Segoe UI", 18, "bold"))
        title.grid(row=0, column=0, sticky="w", pady=(0, controller.pad))

        form = ttk.Frame(self)
        form.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Tutar
        ttk.Label(form, text="Tutar (TL):").grid(row=0, column=0, sticky="w", pady=6)
        self.amount_var = tk.StringVar()
        amount_entry = ttk.Entry(form, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, sticky="ew", pady=6)
        form.grid_columnconfigure(1, weight=1)

        # Açıklama
        ttk.Label(form, text="Açıklama:").grid(row=1, column=0, sticky="w", pady=6)
        self.desc_var = tk.StringVar()
        desc_entry = ttk.Entry(form, textvariable=self.desc_var)
        desc_entry.grid(row=1, column=1, sticky="ew", pady=6)

        # Butonlar
        btns = ttk.Frame(self)
        btns.grid(row=2, column=0, sticky="ew", pady=(controller.pad, 0))
        btn_save = ttk.Button(btns, text="Kaydet", command=self._on_save)
        btn_back = ttk.Button(btns, text="Geri", command=lambda: controller.show_frame("MainScreen"))
        btn_save.grid(row=0, column=0, padx=(0, 6))
        btn_back.grid(row=0, column=1)

        # Kısayollar
        self.bind_all("<Return>", lambda e: self._on_save())

    def _on_save(self):
        raw_amount = self.amount_var.get().replace(",", ".").strip()
        desc = (self.desc_var.get() or "").strip()

        # Basit doğrulama
        try:
            amount = float(raw_amount)
        except ValueError:
            messagebox.showwarning("Geçersiz Tutar", "Lütfen sayısal bir tutar giriniz.")
            return

        if amount <= 0:
            messagebox.showwarning("Geçersiz Tutar", "Tutar 0'dan büyük olmalıdır.")
            return

        self.controller.store.add_expense(today_str(), amount, desc)
        self.amount_var.set("")
        self.desc_var.set("")
        self.controller.refresh_totals_everywhere()
        messagebox.showinfo("Kaydedildi", "Harcama başarıyla kaydedildi.")
        self.controller.show_frame("MainScreen")


# ------------------ UI: İstatistik ------------------ #
class StatsScreen(ttk.Frame):
    def __init__(self, parent, controller: ExpenseApp):
        super().__init__(parent, padding=controller.pad)
        self.controller = controller

        header = ttk.Frame(self)
        header.grid(row=0, column=0, sticky="ew", pady=(0, controller.pad))
        header.grid_columnconfigure(0, weight=1)

        title = ttk.Label(header, text="İstatistik", font=("Segoe UI", 18, "bold"))
        title.grid(row=0, column=0, sticky="w")

        btn_back = ttk.Button(header, text="Geri", command=lambda: controller.show_frame("MainScreen"))
        btn_back.grid(row=0, column=1, sticky="e")

        # Aylık/Günlük toplam göstergeleri
        totals_bar = ttk.Frame(self)
        totals_bar.grid(row=1, column=0, sticky="ew", pady=(0, controller.pad))
        totals_bar.grid_columnconfigure(0, weight=1)
        totals_bar.grid_columnconfigure(1, weight=1)

        self.month_total_var = tk.StringVar(value="")
        self.day_total_var = tk.StringVar(value="")

        ttk.Label(totals_bar, textvariable=self.month_total_var, font=("Segoe UI", 12, "bold")).grid(
            row=0, column=0, sticky="w")
        ttk.Label(totals_bar, textvariable=self.day_total_var, font=("Segoe UI", 12, "bold")).grid(
            row=0, column=1, sticky="e")

        # Kayıt listesi (Treeview)
        columns = ("date", "amount", "desc")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=18)
        self.tree.heading("date", text="Tarih")
        self.tree.heading("amount", text="Tutar")
        self.tree.heading("desc", text="Açıklama")

        self.tree.column("date", width=100, anchor="center")
        self.tree.column("amount", width=100, anchor="e")
        self.tree.column("desc", width=280, anchor="w")

        vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)

        self.tree.grid(row=2, column=0, sticky="nsew")
        vsb.grid(row=2, column=1, sticky="ns")

        # Alt bar: toplam kayıt sayısı
        self.footer_var = tk.StringVar(value="")
        footer = ttk.Label(self, textvariable=self.footer_var)
        footer.grid(row=3, column=0, sticky="ew", pady=(controller.pad, 0))

        # Grid weights
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def on_before_show(self):
        self.refresh_table()

    def refresh_table(self):
        # Temizle
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Verileri oku ve tarihine göre sırala (yeni->eski)
        rows = list(self.controller.store.iter_expenses())
        rows.sort(key=lambda x: x[0], reverse=True)

        for date_str, amount, desc in rows:
            self.tree.insert("", "end", values=(date_str, money_fmt(amount), desc))

        # Toplamlar
        m_total = self.controller.store.get_monthly_total(current_year_month())
        d_total = self.controller.store.get_daily_total(today_str())
        self.month_total_var.set(f"Aylık Toplam: {money_fmt(m_total)}")
        self.day_total_var.set(f"Günlük Toplam: {money_fmt(d_total)}")

        self.footer_var.set(f"Toplam Kayıt: {len(rows)}")


# ------------------ Çalıştır ------------------ #
if __name__ == "__main__":
    app = ExpenseApp()
    app.mainloop()