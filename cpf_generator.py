import random

def generateCPF(punctuation: bool):
    nine_digits = ''
    digits_sum = 0

    for i in range(9):
        nine_digits += str(random.randint(0, 9))

    count_1 = 10
    for digit in nine_digits:
        digits_sum += int(digit) * count_1
        count_1 -= 1

    rest = (digits_sum * 10) % 11

    first_digit = 0 if rest > 9 else rest

    digits_sum, rest = 0, 0

    count_2 = 11
    for digit in nine_digits:
        digits_sum += int(digit) * count_2
        count_2 -= 1

    digits_sum += first_digit * 2

    rest = (digits_sum * 10) % 11

    second_digit = 0 if rest > 9 else rest

    if punctuation:
        generated_cpf = nine_digits[:3] + '.' + nine_digits[3:6] + '.' + nine_digits[6:9] + \
                    '-' + str(first_digit) + str(second_digit)
    else:
        generated_cpf = nine_digits + str(first_digit) + str(second_digit) 
        
    return generated_cpf