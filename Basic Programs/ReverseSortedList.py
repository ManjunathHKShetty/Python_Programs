numbers = [2,3,4,6,8,9]
sorted_list = []

def reverse_sort():
    while numbers:
        max_number = numbers[0]
        for i in numbers:
            if i > max_number:
                max_number = i

        sorted_list.append(max_number)
        numbers.remove(max_number)
    return sorted_list


print(f"Reversed Sorted List:{reverse_sort()}")