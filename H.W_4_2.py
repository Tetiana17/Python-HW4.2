my_list = [6]
new_list = 0
for el in range(len(my_list)):
    if el % 2 == 0:
        new_list += my_list[el]
if len(my_list) > 0:
    last_el = my_list[-1]
else:
    last_el = 0

result = new_list * last_el
print(result)
