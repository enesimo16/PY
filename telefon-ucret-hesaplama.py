
minutes=int(input("Enter the call duration in minutes: "))

fixed_fee=50
free_minutes=4
extra_fee_per_minute=5

if(minutes<=free_minutes):
    total_cost=fixed_fee
else:
    extra_minutes=minutes-free_minutes
    total_cost=fixed_fee+(extra_minutes*extra_fee_per_minute)
    
print(f"Total cost for a {minutes} - minute call: {total_cost} TL")
    