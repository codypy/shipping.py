def cost_ground_ship(weight):
  if weight <= 2:
    return (weight * 1.50) + 20
  elif (weight > 2) and (weight < 6):
    return (weight * 3.00) + 20
  elif (weight > 6) and (weight < 10):
    return (weight * 4.00) + 20
  elif weight > 10:
    return (weight * 4.75) + 20
  
  
def cost_drone_ship(weight):
  if weight <= 2:
    return (weight * 4.50)
  elif (weight > 2) and (weight < 6):
    return (weight * 9.00)
  elif (weight > 6) and (weight < 10):
    return (weight * 12.00)
  elif weight > 10:
    return (weight * 14.75)
  
  
premium_shipping = 125.00


def cheapest_shipping (weight):
  if cost_ground_ship(weight) < premium_shipping and cost_ground_ship(weight) < cost_drone_ship (weight):
    return "The cheapest method will be ground shipping with a cost of $ " + str(cost_ground_ship (weight))
  elif  premium_shipping < cost_ground_ship (weight) and premium_shipping < cost_drone_ship (weight):
    return "The cheapest method will be premiuim shipping with a cost of $ " + str(premium_shipping)
  else:
    return "The cheapest method will be drone shipping with a cost of $ " + str(cost_drone_ship (weight))
  
print(cheapest_shipping())