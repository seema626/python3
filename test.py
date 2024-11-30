# Simple_intrest calculation
def Simple_intrest(p, n, r):
    i = (p*n*r)/100
    amt = p + i
    return {"intrest": i,"amount": amt}

# Take input from userto console
p = float(input("please enter principle in INR: "))
n = float(input("please enter Number of year :" ))
r = float(input("please enter rate of intrest in %p.a. :"))

# Calculate intrest and amount
results = Simple_intrest(p, n, r)

#print the results
print(results)