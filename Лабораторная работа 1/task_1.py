numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
s, n, f = 0, 0, 0
# TODO заменить значение пропущенного элемента средним арифметическим
for i in range(len(numbers)):
    if numbers[i]:
        s+=numbers[i]
        n+=1
    else: f = i
numbers[f] = s/(n+1)
print("Измененный список:", numbers)
