some = 0 # Изначально ноль
while some < 10: # Работает пока меньше 10
  some += 1 # В каждой итерации увеличиваем на 1
  if some % 2 == 0: # Если четное, то пропускаем число
    continue # Пропуск итерации
  print("Значение равно: ", some) # Вывод в консоль