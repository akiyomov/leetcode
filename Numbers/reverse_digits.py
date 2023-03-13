def reverse_digits(num: int) -> int:
    if num == 0:
        return 
    result = 0
    while num != 0:
        result*=10
        digit = num % 10
        result += digit
        num //= 10
    return result

print(reverse_digits(123))