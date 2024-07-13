my_list = [6]
new_list = 0
#перебираємо елементи зі списку
for el in range(len(my_list)):
#перевіряємо чи індекс елемента є парним
    if el % 2 == 0:
        new_list += my_list[el]
#якщо так додаємо в новий лист
if len(my_list) > 0:
#знаходимо останній елемент
    last_el = my_list[-1]
else:
    last_el = 0
#перемножуємо
result = new_list * last_el
print(result)
