import math

y=15 #global scope

def outer():
    x=7    #local scope
    def inner():
        nonlocal x  #nonlocal scope
        x+=12
        print("x in the inner : ",x)
    inner()
    print("x inside the outer: ",x)
outer()

print("*************************************************************")

min_value=min(7,34,19)
max_value=max(9,5,4,8,62)
print(min_value)
print(max_value)

result=abs(-7.19)
print(result)

result2=pow(2,5)
print(result2)

print("*************************************************************")

print(math.e) #sabit sayılar.
print(math.pi)
print(math.acos(0.55)) #trigonometri ifadeleri.
print(math.sin(0.00))
print(math.degrees(8.90)) #dereceye ve radyana çevrim.
print(math.radians(180))
print(math.ceil(1.3)) #üst sayıya yuvarlar.
print(math.floor(7.9)) #alt sayıya yuvarlar.
print(math.sqrt(10)) #karekök hesaplama.
print(math.isqrt(10)) # ondalıksız karekök gösterir.
print(math.trunc(19.77)) #ondalıkları siler.
print(math.remainder(9,2)) #bölümden kalanı verir fakat garip bir sistemi vardır.
print(math.comb(7,4)) #kombinasyon
print(math.copysign(7,-19)) #ilkinin degeri ikincisinin işaretini alır.
p=[3]
q=[1]
print(math.dist(p,q))  #öklid alır.
print(math.erf(0.70))
print(math.erfc(0.70))
print(math.exp(1)) #euler sayisinin katlarini alır.
print(math.expm1(1)) #katından 1 çıkarır.
print(math.fabs(-70.19)) #kayan sayılarda floatlarda mutlak
print(math.factorial(6)) #faktöriyel
print(math.hypot(6,12)) #hipotenüs
print(math.isclose(8.005,8.450,abs_tol=0.4)) #aralarında 0.4 fark varsa true yoksa false, 0.5 yapsaydık true olurdu.
print(math.log(8,2)) #ilki sayı 2.si taban.






