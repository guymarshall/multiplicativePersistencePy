def product(input):
    result = 1

    # get each digit by mid instead of string conversion
    while input > 0:
        result *= input % 10
        input /= 10
    return result

def multiplicative_persistence(user_input):
    steps = 0

    # 10 is smallest double digit number
    while user_input >= 10:
        user_input = product(user_input)
        steps += 1
    return steps

def main():
    ## largest step count discovered = 277777788888899

    highest_steps_count = 0
    highest_steps_number = 0

    # start = 312300000000
    # start = 650000000000
    # start = 2873700000000
    # start = 5740000000000
    # start = 5745600000000
    # start = 6108200000000
    start = 6111000000000
    # finish = 1000000000000000
    finish = 277777788888899

    for number in range(start, finish + 1):
        # print(f"{number}: {multiplicative_persistence(number)}")
        result = multiplicative_persistence(number)
        if result > highest_steps_count:
            highest_steps_count = result
            highest_steps_number = number
        if number % 10000000 == 0:
            print(f"Upto {number} so far: {highest_steps_number}")
    print(f"Highest step count: {highest_steps_number} at {highest_steps_count}")


if __name__ == "__main__":
    main()