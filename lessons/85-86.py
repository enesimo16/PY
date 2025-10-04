import statistics

data=[10,20,30,30,40,10,20,50,20]

print(statistics.harmonic_mean(data))
print(statistics.mean(data)) # ortalamayı alır.
print(statistics.median(data)) #tekse tam orta değer çift ise medyanını alır.
print(statistics.mode(data)) # en çok hangi sayı var ise o fakat aynı sayıda varsa ilk olanı gösterr.

print(statistics.pstdev(data)) #standart sapma
print(statistics.pvariance(data))