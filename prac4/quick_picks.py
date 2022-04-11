import random
pick = int(input('How many quick picks?'))
my_list = range(45)
for a in range(pick):
    print(random.sample(my_list,6))