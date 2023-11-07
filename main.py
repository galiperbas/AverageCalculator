sum = 0
go_on = True
num_list = []

while go_on :
    num = float(input("enter a number to calculate the average..:"))

    if num == 1010:
        go_on = False
    else:
        num_list.append(num)

for i in num_list:
    sum = sum + i

result = sum / len(num_list)

print(f"the average of {num_list} is {result}")