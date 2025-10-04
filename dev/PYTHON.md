
# 🐍 Python Notları 
  
---  
  
## 1. 📝 Yorum Satırları  
  
- Tek satırlık:  
  ```python  
  # Bu bir yorum  
  ```  
- Çok satırlı:  
  ```python  
  """  
  Bu çok  satırlı bir  yorumdur  """  ```  
---  
  
## 2. 📦 Değişkenler ve Veri Tipleri  
  
### Temel veri tipleri:  
- `int` → Tam sayılar    
- `float` → Ondalıklı sayılar    
- `str` → Metin (karakter dizileri)    
- `bool` → Mantıksal değer (`True`, `False`)  
  
### Tip dönüşümleri:  
```python  
int("5")         # 5  
float("3.14")    # 3.14  
str(10)          # "10"  
bool(0)          # False  
```  
  
---  
  
## 3. 🔁 Girdi ve Çıktı  
  
```python  
ad = input("Adınız nedir? ")   # input her zaman string döner  
print("Merhaba", ad)  
```  
  
---  
  
## 4. ➕ Operatörler  
  
### Aritmetik Operatörler:  
| Operatör | Anlamı        |     |
| -------- | ------------- | --- |
| `+`      | Toplama       |     |
| `-`      | Çıkarma       |     |
| `*`      | Çarpma        |     |
| `/`      | Bölme (float) |     |
| `//`     | Tam bölme     |     |
| `%`      | Mod (kalan)   |     |
| `**`     | Üs alma       |     |
  
### Karşılaştırma:  
```python  
==, !=, <, >, <=, >=  
```  
  
### Mantıksal:  
```python  
and, or, not  
```  
  
---  
  
## 5. 🔀 Koşullu İfadeler (if-elif-else)  
  
```python  
sayi = 5  
if sayi > 0:  
    print("Pozitif")elif sayi < 0:  
    print("Negatif")else:  
    print("Sıfır")```  
  
---  
  
## 6. 🔤 String (Metin) İşlemleri  
  
```python  
ad = "enes"  
print(ad.upper())         # "ENES"  
print(ad.capitalize())    # "Enes"  
print(len(ad))            # 4  
print(ad[0])              # "e"  
print(ad[-1])             # "s"  
```  
  
### Dilimleme (Slicing):  
```python  
ad[1:3]    # "ne"  
ad[:2]     # "en"  
ad[::2]    # "es"  
```  
  
---  
  
## 7. 📚 Listeler (list)  
  
```python  
meyveler = ["elma", "armut", "muz"]  
print(meyveler[0])        # "elma"  
meyveler.append("kiraz")  
meyveler.remove("armut")  
```  
  
### Faydalı list metodları:  
```python  
len(meyveler)  
meyveler.pop()        # Son elemanı çıkarır  
meyveler.sort()       # Sıralar  
meyveler.reverse()    # Ters çevirir  
```  
  
---  
  
## 8. 🔐 Demetler (Tuples)  
  
- Değiştirilemez (immutable) listelerdir.  
  
```python  
renkler = ("kırmızı", "mavi", "yeşil")  
print(renkler[1])  # "mavi"  
```  
  
---  
  
## 9. 🧾 Sözlükler (Dictionaries)  
  
```python  
ogrenci = {"ad": "Enes", "yas": 20}  
print(ogrenci["ad"])       # "Enes"  
ogrenci["okul"] = "BTÜ"  
```  
  
---  
  
## 10. 🔣 Kümeler (Set)  
  
- Tekrar eden değerleri almaz.  
  
```python  
sayilar = {1, 2, 3, 3, 4}  
print(sayilar)  # {1, 2, 3, 4}  
```  
  
---  
  
## 11. ✅ Boolean (Mantıksal Değerler)  
  
```python  
a = True  
b = False  
  
print(a and b)  # False  
print(a or b)   # True  
print(not a)    # False  
```  
  
---  
  
## 12. 🔍 Karakter Karşılaştırmaları  
  
```python  
"a" < "b"         # True  
"abc" == "abc"    # True  
"enes" != "enes"  # False  
```  
  
---  
  
## 13. 🧮 İşlem Önceliği (Önem Sırası)  
  
1. `()` → Parantez içi  
2. `**` → Üs alma  
3. `*`, `/`, `//`, `%`  
4. `+`, `-`  
5. `==`, `!=`, `<`, `>` vs.  
6. `not`  
7. `and`  
8. `or`  
  
---  
  
## 14. 🔎 in & not in Operatörleri  
  
```python  
"a" in "kalem"           # True  
3 not in [1, 2, 4]       # True  
"elma" in ["elma", "armut"]  # True  
```  
  
---  
  
## 15. 🧯 Hatalar ve Tip Kontrolleri  
  
```python  
type(10)         # <class 'int'>  
type("hello")    # <class 'str'>  
type([])         # <class 'list'>  
```  
  
### Temel hata türleri:  
- `NameError` → Tanımsız değişken  
- `TypeError` → Yanlış tür işlemi  
- `ValueError` → Hatalı değer dönüşümü  
  
---  
  
