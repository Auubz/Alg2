import decimal

Sale1 = "1.40"
Sale2 = "2.30"

sd1 = decimal.Decimal(Sale1)
sd2 = decimal.Decimal(Sale2)

Result = (sd1 + sd2)

print ("The toal sale price is $" + str(Result))