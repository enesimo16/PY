text="The price is only {price:.2f} to buy {fname}".format(fname="Computer",price=24.999)

print(text)

text2="We do not have {:<10} children"
text3="We do not have {:>10} children"
text4="We do not have {:^10} children"
text5="The temperature is between {:+} and {:+} degrees celcius"

print(text2.format(7))
print(text3.format(7))
print(text4.format(7))
print(text5.format(-4,7))
