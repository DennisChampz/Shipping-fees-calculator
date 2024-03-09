weight=41.5
print ("weight="+str(weight))
#ground shipping
if weight <= 2:
  cost=weight1.50+20;
elif weight >2 and weight <=6:
  cost=weight3.00+20;
elif weight >6 and weight <10:
  cost=weight4.00+20;
else:
  cost=weight4.75+20;
print("ground shipping="+str(cost))

#ground shipping premium
premium_cost = 125.00
print("ground shipping premium="+str(premium_cost))

#drone shipping
if weight <= 2:
  drone_shipping=weight4.50+0;
elif weight >2 and weight <=6:
  drone_shipping=weight9.00+0;
elif weight >6 and weight <10:
  drone_shipping=weight12.00+0;
else:
  drone_shipping=weight14.75+0;
print("drone shipping="+str(drone_shipping))
print("")
print("if it is a 4.8 pound package, the cheapest method is ground shipping, costing $34.40")
print("")
print("if it is a 41.5 pound package,the cheapest method is ground shipping premium, costing $125.00")
