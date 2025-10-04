import math 
import cmath # karmaşık sayılar için.

print(math.log10(100000))
print(math.log1p(9)) # içeridikine 1 ekleyerke eulen sayısı ile hesaplar.
print(math.perm(5)) #permütasyon
print(math.perm(6,2)) #permütasyon
print(math.pow(6,2)) #üs


print("*****************************")

#complex math = cmath

print(cmath.e)
print(-cmath.e)
print(cmath.inf) # karmaşık sayı reel kısım
print(cmath.infj) # karmaşık sayı imajiner kısım
z=cmath.infj
result=7+z
print(result)
print(cmath.sqrt(-4))
print(cmath.isfinite(complex(7,float('inf'))))  # sonsuzluk kontrolü yapar.












