num_items = int(input ('Number of item:'))
total = 0
for i in range (num_items):
    price = float(input('Price of Item:'))
    total += price
    if price < 0:
        print('invalid price')
if total >= 100:
    print(f'Total price for {num_items} items is ${total* 0.1}')
else:
    print('Total price for{} items is $ {} '.format(num_items,total))



