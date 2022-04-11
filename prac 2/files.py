# 1 and 2
def part_1():
    out_file = open('name.txt',"w")
    out_file.write('Bob')
    out_file.close()
    out_file = open('name.txt',"r")
    name = out_file.read()
    print(f'Your name is {name} ')
# 3 and 4
def part_2():
    out_file_2 = open('numbers.txt','r')
    total_number = 0
    for i in out_file_2.readlines(3):
        a = int(i)
        total_number += a
    print(total_number)
    out_file_2.close()



out_file_3 = open('numbers.txt','r')
for all_lines in out_file_3.readlines(6):
    print(all_lines)
out_file_3.close()

part_2()

part_1()

