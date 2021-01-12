import matplotlib.pyplot as plt
import numpy as np

n, m = map(int, input().split())

beginning_inventory = 3
lead_time = 2
total_demand = 0
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8
shortage_day = 0
np.random.seed(0)
ending_inventory_g = []
for cycle in range(10):
    print("Cycle number: ", cycle)
    for day in range(1, n+1):
        print("Day-", day)
        lead_time -= 1

        if lead_time == -1:
            print("Filling at leed time: ", -1)
            beginning_inventory += order_quantity
            order_quantity = -1

        print("Beginning Inventory: ", beginning_inventory)
        demand = np.random.choice(a=[0, 1, 2, 3, 4], p=[
                                  0.10, 0.25, 0.35, 0.21, 0.09])
        print("Demand-", demand)
        total_demand = demand + shortage_quantity
        if total_demand > beginning_inventory:
            shortage_quantity = total_demand-beginning_inventory
            ending_inventory = 0
            shortage_day += 1
        else:
            ending_inventory = beginning_inventory-total_demand
            shortage_quantity = 0

        print("ending inventory: ", ending_inventory)
        print("Shortage: ", shortage_quantity)
        print("Lead Time: ", lead_time)
        ending_inventory_g.append(ending_inventory)
        beginning_inventory = ending_inventory

        if day == n:
            order_quantity = m - beginning_inventory
            lead_time = np.random.choice(a=[1, 2, 3], p=[0.6, 0.3, 0.1])
        print("Ordered quantity: ", order_quantity)
        print()

print("Average ending inventory:", sum(
    ending_inventory_g)/len(ending_inventory_g))
print("Number of days of shortage:", shortage_day)

plt.plot(range(1, 10*n+1), ending_inventory_g)
plt.show()
