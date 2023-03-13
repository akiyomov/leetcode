# Description: input: 1234, output: 4 3 2 1
def print_digits(num: int) -> None:
    if num == 0:
        return
    while num != 0:
        digit = num % 10
        print(digit)
        num //= 10
    
print_digits(1234)

