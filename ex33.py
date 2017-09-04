#WHile Loop

max_range = int(input("Enter max_range: >"))
increment_flag = int(input("Enter increment_flag: >"))

def print_list(max_range,increment_flag):
    i = 0;
    numbers = []
    while i < max_range:
        print(f"At the top i is {i}")
        numbers.append(i)
        i += increment_flag
        print("Number now: ", numbers)
        print(f"At the bottom i is {i}")
    for num in numbers:
        print(num)


print_list(max_range,increment_flag)
