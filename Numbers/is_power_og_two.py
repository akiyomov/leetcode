def is_power_of_two(num: int) -> bool:
    bit_count = 0
    while num != 0:
        bit_count += num & 1
        num = num >> 1
    return bit_count == 1

print(is_power_of_two(16))