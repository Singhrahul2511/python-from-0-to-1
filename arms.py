def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    armstrong_sum = sum(int(digit)**power for digit in num_str)  
    return armstrong_sum == num
armstrong_numbers = [num for num in range(1, 5000) if is_armstrong_number(num)]
print("Armstrong numbers from 1 to 5000:")
print(armstrong_numbers)


