print("Aritmetik islem uygulamasina hos geldiniz.")

def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            cycle+=1
            return False
    return True

sayi1=int(input("1.sayiyi giriniz: "))
sayi2=int(input("2.sayiyi giriniz: "))

if sayi1==0 or sayi2 ==0:
    print("Lütfen 0 harici sayilar giriniz!")
else:
    if sayi1>sayi2:
        print("Girdiğiniz 1.sayi , 2. sayidan büyüktür.")
        result1=sayi1/sayi2
        tam_sonuc1=round(result1)
        print("Ve bu iki sayinin bölümü: ", result1, " Yuvarlanmis hali ise: ", tam_sonuc1)
        if tam_sonuc1 < 3:
            print("Bölümden gelen sonuç bir asal sayidir.")
        if tam_sonuc1 < 3 and tam_sonuc1 != 1:
            if asal_mi(tam_sonuc1 ):
                print("Sonuç asal bir sayidir.")
            else:
                print("Sonuç asal bir sayi değildir.")
    elif sayi2>sayi1:
        print("Girdiğiniz 2.sayi, 1.sayidan büyüktür.")
        result2=sayi2 / sayi1
        tam_sonuc2=round(result2)
        print("Ve bu iki sayinin bölümü: ", result2, " Yuvarlanmis hali ise: ", tam_sonuc2)
        if tam_sonuc2 < 3 and tam_sonuc2 != 1:
            print("Bölümden gelen sonuç bir asal sayidir.")
        elif tam_sonuc2 >= 3:
            if asal_mi(tam_sonuc2):
                print("Sonuç asal bir sayidir.")
            else:
                print("Sonuç asal bir sayi değildir.")
    else:
        print("Girdiğiniz 2 sayi birbirine eşittir.")
        result3=sayi2/sayi1
        print("Bu iki sayi birbirine esit oldugundan her zaman bölümleri eşit ve ",result3,"'dir.")
        print("Ayni zamanda bu iki sayinin bölümü ",result3,"olduğudndan asal sayi degildir.")




