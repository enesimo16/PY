

quiantity=int(input("Enter the number of books you want to order: "))
book_price=105

total_price=quiantity*book_price

if(quiantity>=50):
    discount_rate=0.25
elif(quiantity>=25):
    discount_rate=0.15
elif(quiantity>=10):
    discount_rate=0.10
else:
    discount_rate=0.00
    
discount_amount=total_price*discount_rate

final_price=total_price-discount_amount
print(f"Total price (Before) : {total_price:.2f} TL")
print(f"Discount amount      : {discount_amount:.2f} TL")
print(f"Final price to pay   : {final_price:.1f} TL")