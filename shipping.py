weight = 41.5

#Ground shipping
if weight <= 2:
  cost_ground = 20 + weight*1.50
elif weight <= 6:
  cost_ground = 20 + weight*3.00
elif weight <= 10:
  cost_ground = 20 + weight*4.00
else:
  cost_ground = 20 + weight*4.75

print("Cost of ground shipping: " + str(cost_ground))

#Premium ground shipping
cost_ground_premium = 125.00

print("Cost of Premium ground shipping: " + str(cost_ground_premium))

#Drone Shipping
if weight <= 2:
  cost_drone = weight*4.50
elif weight <= 6:
  cost_drone = weight*9.00
elif weight <= 10:
  cost_drone = weight*12.00
else:
  cost_drone = weight*14.25

print("Cost of drone shipping: " + str(cost_drone))
