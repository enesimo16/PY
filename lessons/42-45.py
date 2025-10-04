#while loop  # else ile de kullanilir.

i=1 #increment
while (i<=7):
    print(i,end=" ")
    if (i==4):
        break #4'ü atlar.
    i+=1
print("\ndone") 


# while (i<=7):
#   print(i,end=" ")
#    if (i==4):
#      continue #4'ten sonra komutları calistirmaz ve sürekli 4 yazar.
#   i+=1
# print("\ndone") 

myNumbers=[70,19,68,52,98,75]
a=0
while(a<len(myNumbers)):
    print(myNumbers[a])
    a+=1
else:
    print("While loop is over.")
print(" ss")


myInputs=[]
b=0
while(b<7):
    input_number=int(input("Enter a integers: "))
    myInputs.append(input_number)
    b+=1
myInputs.sort()
# print(myInputs)  #fakat parantezli gösterir bu olmaması için;
x=0
while(x<7):
    print(myInputs[x])
    x+=1
    
    

start_number=int(input("Enter the start number: "))
end_number=int(input("Enter the end number: "))

while(start_number<end_number):
    if(start_number %2 == 0):
        print(start_number, end=" ")
    start_number+=1
    
while (True):   # ad kısmına boşluk girildikçe tekrar tekrar sorulacak
    name=input("Enter your name: ")
    if (name==""):
        continue
    else:
        break
    
print(f"your name is {name}")





