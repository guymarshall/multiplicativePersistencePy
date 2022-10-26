import numba as nb


@nb.njit
def product(input):
    result = 1

    # get each digit by mid instead of string conversion
    while input > 0:
        result *= input % 10
        input /= 10
    return result


@nb.njit
def multiplicative_persistence(user_input):
    steps = 0

    # 10 is smallest double digit number
    while user_input >= 10:
        user_input = product(user_input)
        steps += 1
    return steps


@nb.njit
def main():
    ## largest step count discovered = 277777788888899

    highest_steps_count = 11
    highest_steps_number = 277777788888899

    number = 0

    while highest_steps_count < 12:
        # print(f"{number}: {multiplicative_persistence(number)}")
        result = multiplicative_persistence(number)
        if result > highest_steps_count:
            highest_steps_count = result
            highest_steps_number = number
        if number % 1000000 == 0:
            print(f"Upto {number} so far with {result} steps")
        number += 1
    print(f"Highest step count: {highest_steps_number} at {highest_steps_count}")


if __name__ == "__main__":
    main()