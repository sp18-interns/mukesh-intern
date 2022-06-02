"""

Purpose: Compute and compare meal plans

"""


def find_cost_per_meal(total_cost, num_meals, flex):
    per_meal = (total_cost - flex)/num_meals
    return per_meal

pm1 = find_cost_per_meal(6480, 23, 100)
pm2 = find_cost_per_meal(6480, 21, 200)

if pm1 < pm2:
    print ("First meal plan is better")
    print ("Cost per meal is", pm1)
else:
    print ("Second meal plan is better")
    print ("Cost per meal is", pm2)
    