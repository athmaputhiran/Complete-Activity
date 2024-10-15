item_1 = float(input("What is the price for the first item: "))
item_2 = float(input("What is the price for the second item: "))
item_3 = float(input("What is the price for the third item: "))

total = item_1+item_2+item_3
avg = total/3

#Calculate to 1 decimal places.
"""(round(avg))
avg=(round(avg))
(round(total))
total=(round(total))"""

print(*f"The total cost of the 3 items are S${total} and the average is {avg = : }")
