price=int(input("Enter the price you seek:"))
inctx=0
ins=0
if price>=72000 and price<150000:
    inctx=0.10*price
    ins=0.15*price
elif price>=150000 and price<200000:
    inctx=0.25*price
    ins=0.20*price
elif price>=200000:
    inctxs=(35/100)*price
    ins=(28/100)*price
else:
    print("Our minimum price should be 72000. Please Enter a valid calue")
print("ON Road price:",price+inctx+ins)
200
