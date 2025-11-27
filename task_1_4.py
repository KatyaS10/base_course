num = [1, 2, 3, 4, 5]
if len(num) == 0:
    average = 0
else:
    total_sum = sum(num)
    average = total_sum / len(num)
print(f"Массив: {num}")
print(f"Среднее арифметическое: {average}")