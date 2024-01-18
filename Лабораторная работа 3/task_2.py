def find_common_participants(s1, s2, d = ","):
    str1 = s1.split(d)
    str2 = s2.split(d)
    l = []
    for i in str1:
        for j in str2:
            if i == j:
                l.append(j)
    return sorted(l)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
